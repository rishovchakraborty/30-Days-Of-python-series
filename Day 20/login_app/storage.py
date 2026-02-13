"""
Storage utilities for the login_app.

Here we use a JSON file as a tiny "database" for users.
"""

import json
from pathlib import Path

# JSON file will live next to this module
BASE_DIR = Path(__file__).parent
USERS_FILE = BASE_DIR / "users.json"


def load_users() -> dict:
    """Load users from the JSON file. If it doesn't exist, return an empty dict."""
    if not USERS_FILE.exists():
        return {}

    with USERS_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_users(users: dict) -> None:
    """Save users dictionary to the JSON file with nice formatting."""
    with USERS_FILE.open("w", encoding="utf-8") as f:
        json.dump(users, f, indent=2)

