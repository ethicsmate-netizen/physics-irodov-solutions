import sqlite3
import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "irodov.db"
CATALOG_PATH = DATA_DIR / "irodov_catalog.json"
QUESTIONS_PATH = DATA_DIR / "questions_seed.json"


def get_connection():
    os.makedirs(DATA_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(force_reseed=False):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS parts (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        short_title TEXT NOT NULL,
        problem_range TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chapters (
        id TEXT PRIMARY KEY,
        part_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        problem_range TEXT NOT NULL,
        count INTEGER NOT NULL,
        FOREIGN KEY (part_id) REFERENCES parts(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id TEXT PRIMARY KEY,
        part_id INTEGER NOT NULL,
        part_title TEXT NOT NULL,
        chapter_id TEXT NOT NULL,
        chapter_title TEXT NOT NULL,
        statement TEXT NOT NULL,
        difficulty INTEGER NOT NULL DEFAULT 2,
        tags TEXT NOT NULL,
        hints TEXT NOT NULL,
        answer TEXT NOT NULL,
        solution TEXT NOT NULL,
        FOREIGN KEY (chapter_id) REFERENCES chapters(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_progress (
        question_id TEXT PRIMARY KEY,
        status TEXT NOT NULL DEFAULT 'unsolved',
        notes TEXT DEFAULT '',
        last_reviewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (question_id) REFERENCES questions(id)
    )
    """)

    conn.commit()

    # Check if data already seeded
    cursor.execute("SELECT COUNT(*) FROM parts")
    parts_count = cursor.fetchone()[0]

    if parts_count == 0 or force_reseed:
        seed_catalog(conn)
        seed_questions(conn)

    conn.close()


def seed_catalog(conn):
    if not CATALOG_PATH.exists():
        print(f"Catalog file missing at {CATALOG_PATH}")
        return

    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    cursor = conn.cursor()
    cursor.execute("DELETE FROM chapters")
    cursor.execute("DELETE FROM parts")

    for part in catalog.get("parts", []):
        cursor.execute(
            "INSERT INTO parts (id, title, short_title, problem_range) VALUES (?, ?, ?, ?)",
            (part["id"], part["title"], part["short_title"], part["problem_range"])
        )
        for ch in part.get("chapters", []):
            cursor.execute(
                "INSERT INTO chapters (id, part_id, title, problem_range, count) VALUES (?, ?, ?, ?, ?)",
                (ch["id"], part["id"], ch["title"], ch["range"], ch["count"])
            )

    conn.commit()
    print("Catalog seeded successfully.")


def seed_questions(conn):
    if not QUESTIONS_PATH.exists():
        print(f"Questions seed file missing at {QUESTIONS_PATH}")
        return

    with open(QUESTIONS_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)

    cursor = conn.cursor()
    cursor.execute("DELETE FROM questions")
    for q in questions:
        cursor.execute("""
        INSERT OR REPLACE INTO questions 
        (id, part_id, part_title, chapter_id, chapter_title, statement, difficulty, tags, hints, answer, solution)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            q["id"],
            q["part_id"],
            q["part_title"],
            q["chapter_id"],
            q["chapter_title"],
            q["statement"],
            q.get("difficulty", 2),
            json.dumps(q.get("tags", [])),
            json.dumps(q.get("hints", [])),
            q.get("answer", ""),
            q.get("solution", "")
        ))

    conn.commit()
    print(f"Seeded {len(questions)} questions into SQLite database.")


def get_all_questions(search=None, part_id=None, chapter_id=None, difficulty=None, status=None, limit=100, offset=0):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT q.*, 
           COALESCE(up.status, 'unsolved') as user_status, 
           COALESCE(up.notes, '') as user_notes 
    FROM questions q
    LEFT JOIN user_progress up ON q.id = up.question_id
    WHERE 1=1
    """
    params = []

    if search:
        query += " AND (q.id LIKE ? OR q.statement LIKE ? OR q.tags LIKE ? OR q.chapter_title LIKE ?)"
        s = f"%{search}%"
        params.extend([s, s, s, s])

    if part_id:
        query += " AND q.part_id = ?"
        params.append(part_id)

    if chapter_id:
        query += " AND q.chapter_id = ?"
        params.append(chapter_id)

    if difficulty:
        query += " AND q.difficulty = ?"
        params.append(difficulty)

    if status and status != "all":
        query += " AND COALESCE(up.status, 'unsolved') = ?"
        params.append(status)

    query += " ORDER BY CAST(SUBSTR(q.id, 1, INSTR(q.id, '.') - 1) AS INTEGER), CAST(SUBSTR(q.id, INSTR(q.id, '.') + 1) AS INTEGER) LIMIT ? OFFSET ?"
    params.extend([limit, offset])

    cursor.execute(query, params)
    rows = cursor.fetchall()
    
    results = []
    for r in rows:
        results.append({
            "id": r["id"],
            "part_id": r["part_id"],
            "part_title": r["part_title"],
            "chapter_id": r["chapter_id"],
            "chapter_title": r["chapter_title"],
            "statement": r["statement"],
            "difficulty": r["difficulty"],
            "tags": json.loads(r["tags"]),
            "hints": json.loads(r["hints"]),
            "answer": r["answer"],
            "solution": r["solution"],
            "user_status": r["user_status"],
            "user_notes": r["user_notes"]
        })

    conn.close()
    return results


def get_question_by_id(question_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT q.*, 
           COALESCE(up.status, 'unsolved') as user_status, 
           COALESCE(up.notes, '') as user_notes 
    FROM questions q
    LEFT JOIN user_progress up ON q.id = up.question_id
    WHERE q.id = ?
    """, (question_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return None

    return {
        "id": row["id"],
        "part_id": row["part_id"],
        "part_title": row["part_title"],
        "chapter_id": row["chapter_id"],
        "chapter_title": row["chapter_title"],
        "statement": row["statement"],
        "difficulty": row["difficulty"],
        "tags": json.loads(row["tags"]),
        "hints": json.loads(row["hints"]),
        "answer": row["answer"],
        "solution": row["solution"],
        "user_status": row["user_status"],
        "user_notes": row["user_notes"]
    }


def set_progress(question_id, status=None, notes=None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT status, notes FROM user_progress WHERE question_id = ?", (question_id,))
    existing = cursor.fetchone()

    current_status = existing["status"] if existing else "unsolved"
    current_notes = existing["notes"] if existing else ""

    new_status = status if status is not None else current_status
    new_notes = notes if notes is not None else current_notes

    cursor.execute("""
    INSERT INTO user_progress (question_id, status, notes, last_reviewed_at)
    VALUES (?, ?, ?, CURRENT_TIMESTAMP)
    ON CONFLICT(question_id) DO UPDATE SET
        status = excluded.status,
        notes = excluded.notes,
        last_reviewed_at = CURRENT_TIMESTAMP
    """, (question_id, new_status, new_notes))

    conn.commit()
    conn.close()


def get_stats():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM questions")
    total_questions = cursor.fetchone()[0]

    cursor.execute("SELECT status, COUNT(*) FROM user_progress GROUP BY status")
    status_counts = {r[0]: r[1] for r in cursor.fetchall()}

    cursor.execute("""
    SELECT q.part_id, q.part_title, COUNT(q.id) as total,
           SUM(CASE WHEN up.status = 'solved' THEN 1 ELSE 0 END) as solved
    FROM questions q
    LEFT JOIN user_progress up ON q.id = up.question_id
    GROUP BY q.part_id, q.part_title
    ORDER BY q.part_id
    """)
    part_stats = [
        {
            "part_id": r["part_id"],
            "part_title": r["part_title"],
            "total": r["total"],
            "solved": r["solved"] or 0
        }
        for r in cursor.fetchall()
    ]

    conn.close()
    return {
        "total_questions": total_questions,
        "solved": status_counts.get("solved", 0),
        "starred": status_counts.get("starred", 0),
        "in_progress": status_counts.get("in_progress", 0),
        "unsolved": total_questions - status_counts.get("solved", 0),
        "by_part": part_stats
    }


if __name__ == "__main__":
    init_db(force_reseed=True)
    stats = get_stats()
    print("Database initialized! Current stats:", json.dumps(stats, indent=2))
