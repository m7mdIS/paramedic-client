import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from api import fetch_patient
from fingerprint import scan_fingerprint


def main():
    print("\n=== PARAMEDIC CLIENT ===")
    print("1. Scan patient fingerprint")
    choice = input("Select option: ")

    if choice != "1":
        print("Invalid option")
        return

    fingerprint_id = scan_fingerprint()

    if fingerprint_id is None:
        print("Lookup aborted")
        return

    fetch_patient(str(fingerprint_id))


if __name__ == "__main__":
    main()
