import json
import os
# --- SAMPLE CATALOGUE (from Week 1 or simplified version) ---

catalogue = {
    "book_001": {"title": "1984", "author": "George Orwell", "copies": 3},
    "book_002": {"title": "The Hobbit", "author": "J.R.R. Tolkien", "copies": 2},
    "book_003": {"title": "Python Basics", "author": "A. Smith", "copies": 5},
}

# This will be loaded from a JSON file when the program starts.
members = {}

MEMBERS_FILE = "members.json"


def view_member_details():
    print("\n--- View Member Details ---")

    name = input("Enter member name: ").strip()

    if name not in members:
        print("Member not found.")
        return

    profile = members[name]

    print("\n--- Member Profile ---")
    print(f"Name: {name}")
    print(f"Age: {profile['age']}")
    print(f"Membership Type: {profile['membership']}")
    print(f"Books Borrowed: {len(profile['borrowed'])}")

    # Show borrowed books (with titles)
    if profile["borrowed"]:
        print("\nBorrowed Books:")
        for book_id in profile["borrowed"]:
            title = catalogue[book_id]["title"]
            print(f"- {book_id}: {title}")
    else:
        print("No borrowed books.")
