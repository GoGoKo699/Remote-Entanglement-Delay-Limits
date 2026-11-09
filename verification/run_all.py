#!/usr/bin/env python3
"""Run the finite scientific checks from any working directory."""

import json
from pathlib import Path
import subprocess
import sys


def main():
    directory = Path(__file__).resolve().parent
    for name in ("verify_receivers.py", "verify_driven_qubit.py"):
        result = subprocess.run(
            [sys.executable, str(directory / name), "--json"],
            check=True, capture_output=True, text=True,
        )
        report = json.loads(result.stdout)
        print(f"PASS {name}: {report.get('status', 'all assertions passed')}")
    print("Finite scientific checks passed; see the written proofs for uniform statements.")


if __name__ == "__main__":
    main()
