import json
import os
from pathlib import Path

BASE_URL = os.getenv("CYCLOS_BASE_URL", "https://demo.cyclos.org")

# All test users live in test_data/users.json (single source of truth).
USERS = json.loads(
    (Path(__file__).resolve().parent / "test_data" / "users.json").read_text(encoding="utf-8")
)
VALID_USERS = USERS["valid"]
INVALID_USERS = USERS["invalid"]

# Default user for fixtures (e.g. the dashboard fixture); env vars still override.
USERNAME = os.getenv("CYCLOS_USER", VALID_USERS[0]["username"])
PASSWORD = os.getenv("CYCLOS_PASS", VALID_USERS[0]["password"])
