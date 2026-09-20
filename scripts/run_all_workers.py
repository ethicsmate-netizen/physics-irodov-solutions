"""
run_all_workers.py
Runs extraction workers in parallel across multiple processes
for Parts 2, 3, 4, 5, and 6.
"""

from concurrent.futures import ProcessPoolExecutor, as_completed
import subprocess
import sys
import time

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

WORKER_TASKS = [
    {
        "part": 2,
        "name": "Part 2: Thermodynamics & Molecular Physics",
        "cmd": [
            sys.executable, "scripts/pdf_worker.py",
            "--part", "2",
            "--q-start", "68", "--q-end", "97",
            "--a-start", "290", "--a-end", "298",
            "--min-id", "1", "--max-id", "257",
            "--output", "data/part2.json"
        ]
    },
    {
        "part": 3,
        "name": "Part 3: Electrodynamics",
        "cmd": [
            sys.executable, "scripts/pdf_worker.py",
            "--part", "3",
            "--q-start", "98", "--q-end", "158",
            "--a-start", "299", "--a-end", "316",
            "--min-id", "1", "--max-id", "398",
            "--output", "data/part3.json"
        ]
    },
    {
        "part": 4,
        "name": "Part 4: Oscillations and Waves",
        "cmd": [
            sys.executable, "scripts/pdf_worker.py",
            "--part", "4",
            "--q-start", "159", "--q-end", "191",
            "--a-start", "317", "--a-end", "328",
            "--min-id", "1", "--max-id", "238",
            "--output", "data/part4.json"
        ]
    },
    {
        "part": 5,
        "name": "Part 5: Optics",
        "cmd": [
            sys.executable, "scripts/pdf_worker.py",
            "--part", "5",
            "--q-start", "192", "--q-end", "237",
            "--a-start", "329", "--a-end", "342",
            "--min-id", "1", "--max-id", "275",
            "--output", "data/part5.json"
        ]
    },
    {
        "part": 6,
        "name": "Part 6: Atomic and Nuclear Physics",
        "cmd": [
            sys.executable, "scripts/pdf_worker.py",
            "--part", "6",
            "--q-start", "238", "--q-end", "273",
            "--a-start", "343", "--a-end", "353",
            "--min-id", "1", "--max-id", "321",
            "--output", "data/part6.json"
        ]
    }
]


def execute_worker(task):
    start_t = time.time()
    print(f"[*] Starting {task['name']}...")
    res = subprocess.run(task["cmd"], capture_output=True, text=True, encoding="utf-8", errors="replace")
    elapsed = time.time() - start_t
    if res.returncode == 0:
        print(f"[+] Completed {task['name']} in {elapsed:.1f}s")
        return task["part"], True, res.stdout
    else:
        print(f"[-] Failed {task['name']}:\n{res.stderr}")
        return task["part"], False, res.stderr


def main():
    print(f"Launching {len(WORKER_TASKS)} parallel workers...")
    start_all = time.time()
    results = {}

    with ProcessPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(execute_worker, t): t for t in WORKER_TASKS}
        for future in as_completed(futures):
            part, success, out = future.result()
            results[part] = success
            print(f"Task result for Part {part}: {'SUCCESS' if success else 'FAILED'}")

    total_time = time.time() - start_all
    print(f"\nAll parallel worker tasks finished in {total_time:.1f}s.")
    print("Results summary:", results)


if __name__ == "__main__":
    main()
