"""Very small text 'dashboard' that shows data after login."""

from .api_client import fetch_random_todo


def show_dashboard(username: str) -> None:
    """Print a short message and some data for the logged‑in user."""
    print(f"\nHello, {username}! This is your mini dashboard.")
    print("Fetching a random TODO item from a public JSON API...")

    todo = fetch_random_todo()
    if not todo:
        return

    print("\n--- Nicely formatted ---")
    print(f"Todo ID   : {todo['id']}")
    print(f"User ID   : {todo['userId']}")
    print(f"Title     : {todo['title']}")
    print(f"Completed : {todo['completed']}")

