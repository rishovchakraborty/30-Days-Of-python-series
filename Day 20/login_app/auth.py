"""Signup and login helpers for the small Day 20 login app."""

import hashlib

from .storage import load_users, save_users


def _hash_password(password: str) -> str:
    """Return a SHA‑256 hash of the password (simple demo, not production ready)."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def signup() -> None:
    """
    Create a new user and save it to the JSON "database".

    We store:
    {
        "username": {
            "password_hash": "...",
            "email": "user@example.com"
        }
    }
    """
    users = load_users()

    print("\n=== SIGN UP ===")
    username = input("Choose a username: ").strip()

    if username in users:
        print("Username already exists. Please log in instead.")
        return

    email = input("Email: ").strip()
    password = input("Password: ").strip()

    if len(password) < 6:
        print("Password must be at least 6 characters long.")
        return

    users[username] = {
        "password_hash": _hash_password(password),
        "email": email,
    }
    save_users(users)
    print("Account created successfully!")


def login() -> str | None:
    """Log in a user. Return the username if successful, otherwise None."""
    users = load_users()

    print("\n=== LOG IN ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    user = users.get(username)
    if not user:
        print("No such user. Please sign up first.")
        return None

    if user["password_hash"] != _hash_password(password):
        print("Incorrect password.")
        return None

    print(f"Welcome back, {username}!")
    return username

