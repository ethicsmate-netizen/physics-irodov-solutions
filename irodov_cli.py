#!/usr/bin/env python3
"""
I.E. Irodov 'Problems in General Physics' CLI Tool
Interactive Question Bank, Solver, and Test Generator.
"""

import argparse
import sys
import os
import json
import random
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Ensure Windows terminal prints UTF-8 properly
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from backend import db

DIFFICULTY_STARS = {
    1: "[*] Moderate",
    2: "[**] Advanced",
    3: "[***] Olympiad / Master"
}

STATUS_ICONS = {
    "unsolved": "[ ] Unsolved",
    "in_progress": "[-] In Progress",
    "solved": "[x] Solved",
    "starred": "[*] Starred"
}


def print_banner():
    print("=" * 70)
    print("  I.E. IRODOV - PROBLEMS IN GENERAL PHYSICS QUESTION BANK")
    print("=" * 70)


def cmd_list(args):
    catalog_path = Path("data/irodov_catalog.json")
    if not catalog_path.exists():
        print("Catalog file not found.")
        return

    with open(catalog_path, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    print("\n📚 BOOK TABLE OF CONTENTS & QUESTION DISTRIBUTION:\n")
    for part in catalog.get("parts", []):
        print(f"▶ Part {part['id']}: {part['title']} ({part['problem_range']})")
        for ch in part.get("chapters", []):
            print(f"    • {ch['id']} {ch['title']} [Problems {ch['range']}] ({ch['count']} problems)")
        print()


def display_question(q, show_hints=False, show_solution=False, show_answer=True):
    diff = DIFFICULTY_STARS.get(q['difficulty'], f"Level {q['difficulty']}")
    status = STATUS_ICONS.get(q.get('user_status', 'unsolved'), q.get('user_status', 'unsolved'))

    print("\n" + "─" * 70)
    print(f"📖 PROBLEM {q['id']} | Part {q['part_id']} - {q['chapter_title']}")
    print(f"⚡ Difficulty: {diff} | Status: {status}")
    if q.get('tags'):
        print(f"🏷️ Tags: {', '.join(q['tags'])}")
    print("─" * 70)
    print(f"\n{q['statement']}\n")

    if show_hints:
        print("💡 HINTS:")
        for idx, h in enumerate(q.get('hints', []), 1):
            print(f"   {idx}. {h}")
        print()

    if show_answer:
        print("🎯 FINAL ANSWER:")
        print(f"   {q.get('answer', 'N/A')}\n")

    if show_solution:
        print("📝 STEP-BY-STEP SOLUTION:")
        print(f"{q.get('solution', 'N/A')}\n")
    print("─" * 70)


def cmd_get(args):
    q = db.get_question_by_id(args.id)
    if not q:
        print(f"❌ Problem {args.id} not found in question bank.")
        return

    display_question(
        q,
        show_hints=args.hint or args.all,
        show_solution=args.solution or args.all,
        show_answer=True
    )


def cmd_search(args):
    results = db.get_all_questions(
        search=args.query,
        part_id=args.part,
        chapter_id=args.chapter,
        difficulty=args.difficulty,
        status=args.status
    )
    print(f"\n🔍 Search query '{args.query or ''}' returned {len(results)} problem(s):\n")
    for q in results:
        diff = DIFFICULTY_STARS.get(q['difficulty'], '')
        status = STATUS_ICONS.get(q.get('user_status', 'unsolved'), '')
        print(f"• [{q['id']}] {q['chapter_title']} | {diff} | {status}")
        preview = q['statement'].replace('\n', ' ')[:90]
        print(f"   \"{preview}...\"\n")


def cmd_random(args):
    results = db.get_all_questions(
        part_id=args.part,
        chapter_id=args.chapter,
        difficulty=args.difficulty
    )
    if not results:
        print("❌ No matching questions found.")
        return

    q = random.choice(results)
    print("\n🎲 RANDOM CHALLENGE QUESTION:")
    display_question(
        q,
        show_hints=args.hint,
        show_solution=args.solution,
        show_answer=not args.quiz
    )


def cmd_status(args):
    q = db.get_question_by_id(args.id)
    if not q:
        print(f"❌ Problem {args.id} not found.")
        return

    db.set_progress(args.id, status=args.status, notes=args.notes)
    print(f"✅ Problem {args.id} status updated to '{args.status}'.")


def cmd_stats(args):
    stats = db.get_stats()
    print("\n📊 YOUR STUDY PROGRESS:")
    print("─" * 50)
    print(f"Total Problems in Bank: {stats['total_questions']}")
    print(f"Solved:                 {stats['solved']} ({stats['solved']/max(1, stats['total_questions'])*100:.1f}%)")
    print(f"In Progress:            {stats['in_progress']}")
    print(f"Starred for Review:     {stats['starred']}")
    print(f"Unsolved:               {stats['unsolved']}")
    print("─" * 50)
    print("\nPROGRESS BY PART:")
    for p in stats.get("by_part", []):
        solved = p['solved']
        total = p['total']
        pct = (solved / total * 100) if total > 0 else 0
        bar = "█" * int(pct / 5) + "░" * (20 - int(pct / 5))
        print(f"Part {p['part_id']} ({p['part_title'][:30]}): [{bar}] {solved}/{total} ({pct:.0f}%)")
    print()


def cmd_export(args):
    questions = db.get_all_questions(
        part_id=args.part,
        chapter_id=args.chapter,
        difficulty=args.difficulty,
        limit=args.count or 50
    )
    if not questions:
        print("❌ No questions matched the criteria.")
        return

    out_file = args.out or "irodov_worksheet.md"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# I.E. Irodov - Practice Problem Set\n\n")
        f.write(f"*Generated worksheet containing {len(questions)} problem(s).*\n\n---\n\n")

        for idx, q in enumerate(questions, 1):
            f.write(f"### Question {idx} (Irodov {q['id']})\n\n")
            f.write(f"**Topic**: {q['part_title']} > {q['chapter_title']}  \n")
            f.write(f"**Difficulty**: {DIFFICULTY_STARS.get(q['difficulty'], '')}\n\n")
            f.write(f"{q['statement']}\n\n")
            if args.include_hints and q.get('hints'):
                f.write("**Hints:**\n")
                for h in q['hints']:
                    f.write(f"- {h}\n")
                f.write("\n")
            if args.include_answers:
                f.write(f"> **Answer**: {q['answer']}\n\n")
            if args.include_solutions:
                f.write(f"<details><summary>Click for Step-by-Step Solution</summary>\n\n")
                f.write(f"{q['solution']}\n\n")
                f.write("</details>\n\n")
            f.write("---\n\n")

    print(f"✅ Successfully exported {len(questions)} problems to '{out_file}'!")


def main():
    parser = argparse.ArgumentParser(description="I.E. Irodov Question Bank CLI")
    subparsers = parser.add_subparsers(dest="command")

    # list
    subparsers.add_parser("list", help="List all parts and chapters")

    # get
    get_p = subparsers.add_parser("get", help="View a specific problem by ID (e.g. 1.13)")
    get_p.add_argument("id", type=str, help="Problem number (e.g. 1.1, 1.13)")
    get_p.add_argument("--hint", "-H", action="store_true", help="Show hints")
    get_p.add_argument("--solution", "-s", action="store_true", help="Show full solution")
    get_p.add_argument("--all", "-a", action="store_true", help="Show hints and full solution")

    # search
    search_p = subparsers.add_parser("search", help="Search questions by keyword or tag")
    search_p.add_argument("query", nargs="?", default="", type=str, help="Search query")
    search_p.add_argument("--part", "-p", type=int, help="Filter by Part (1-6)")
    search_p.add_argument("--chapter", "-c", type=str, help="Filter by Chapter ID (e.g. 1.1)")
    search_p.add_argument("--difficulty", "-d", type=int, choices=[1, 2, 3], help="Filter by difficulty (1-3)")
    search_p.add_argument("--status", type=str, choices=["unsolved", "in_progress", "solved", "starred"], help="Filter by status")

    # random
    rand_p = subparsers.add_parser("random", help="Get a random practice problem")
    rand_p.add_argument("--part", "-p", type=int, help="Filter by Part (1-6)")
    rand_p.add_argument("--chapter", "-c", type=str, help="Filter by Chapter ID (e.g. 1.1)")
    rand_p.add_argument("--difficulty", "-d", type=int, choices=[1, 2, 3], help="Filter by difficulty (1-3)")
    rand_p.add_argument("--quiz", action="store_true", help="Hide answer for practice test mode")
    rand_p.add_argument("--hint", action="store_true", help="Show hints")
    rand_p.add_argument("--solution", action="store_true", help="Show solution")

    # status
    stat_p = subparsers.add_parser("status", help="Update problem progress status")
    stat_p.add_argument("id", type=str, help="Problem ID (e.g. 1.13)")
    stat_p.add_argument("status", type=str, choices=["unsolved", "in_progress", "solved", "starred"], help="Status to set")
    stat_p.add_argument("--notes", "-n", type=str, default=None, help="Personal notes")

    # stats
    subparsers.add_parser("stats", help="Display study progress statistics")

    # export
    exp_p = subparsers.add_parser("export", help="Export a problem set to Markdown")
    exp_p.add_argument("--part", "-p", type=int, help="Filter by Part")
    exp_p.add_argument("--chapter", "-c", type=str, help="Filter by Chapter")
    exp_p.add_argument("--difficulty", "-d", type=int, choices=[1, 2, 3], help="Filter by difficulty")
    exp_p.add_argument("--count", "-n", type=int, default=10, help="Number of problems to export")
    exp_p.add_argument("--out", "-o", type=str, default="irodov_worksheet.md", help="Output file path")
    exp_p.add_argument("--include-hints", action="store_true", help="Include hints in worksheet")
    exp_p.add_argument("--include-answers", action="store_true", default=True, help="Include final answers")
    exp_p.add_argument("--include-solutions", action="store_true", help="Include full solutions")

    args = parser.parse_args()

    if not args.command:
        print_banner()
        parser.print_help()
        return

    if args.command == "list":
        cmd_list(args)
    elif args.command == "get":
        cmd_get(args)
    elif args.command == "search":
        cmd_search(args)
    elif args.command == "random":
        cmd_random(args)
    elif args.command == "status":
        cmd_status(args)
    elif args.command == "stats":
        cmd_stats(args)
    elif args.command == "export":
        cmd_export(args)


if __name__ == "__main__":
    main()
