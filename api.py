import requests
from config import SERVER_URL

BASE_URL = SERVER_URL


def fetch_patient(fingerprint_id: str):
    """Fetch patient data from backend using fingerprint_id."""
    try:
        resp = requests.get(f"{BASE_URL}/patient/get/{fingerprint_id}", timeout=5)

        if resp.status_code == 200:
            data = resp.json()
            if not data:
                print("❌ No patient found for this fingerprint ID")
                return None

            print("✅ Patient record found")
            print(f"ID: {data.get('id')}")
            print(f"Name: {data.get('name')}")
            print(f"Age: {data.get('age')}")
            print(f"Medical history: {data.get('medical_history')}")
            print(f"Allergies: {data.get('allergies')}")
            print(f"Medications: {data.get('medications')}")
            return data

        print("❌ Backend error:", resp.text)
        return None

    except Exception as exc:  # broad, but CLI needs robust error surfacing
        print("❌ API connection failed:", exc)
        return None