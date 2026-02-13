"""Tiny API helper using `requests` to fetch a sample TODO in JSON."""

from typing import Any, Dict, Optional

import json

import requests  # third‑party library, installed with: pip install requests


def fetch_random_todo() -> Optional[Dict[str, Any]]:
    """
    Call a public JSON API and return a TODO item.

    This demonstrates:
    - Making an HTTP GET request
    - Getting JSON back from an API
    - Working with the JSON data as a Python dict
    """
    url = "https://jsonplaceholder.typicode.com/todos/1"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # raise error for 4xx / 5xx
    except requests.RequestException as exc:
        print(f"Failed to call API: {exc}")
        return None

    # .json() converts the JSON response body into a Python dict
    todo = response.json()

    print("\n--- Raw JSON from API ---")
    print(json.dumps(todo, indent=2))

    return todo

