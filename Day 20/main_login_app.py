"""CLI entry point for the Day 20 login project.
Run this file to try the app.
"""

from login_app.auth import login, signup
from login_app.dashboard import show_dashboard


def main() -> None:
    print("=== Day 20: Login Project with JSON, API & Packages ===")

    while True:
        print("\nChoose an option:")
        print("1. Sign up")
        print("2. Log in")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "1":
            signup()
        elif choice == "2":
            username = login()
            if username:
                show_dashboard(username)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

