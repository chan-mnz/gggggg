
import json
import os

# --- SAMPLE CATALOGUE (from Week 1 or simplified version) ---

catalogue = {
    "book_001": {"title": "1984", "author": "George Orwell", "copies": 3},
    "book_002": {"title": "The Hobbit", "author": "J.R.R. Tolkien", "copies": 2},
    "book_003": {"title": "Python Basics", "author": "A. Smith", "copies": 5},
}

# This will be loaded from a JSON file when the program starts.

MEMBERS_FILE = "members.json"

def save_members(members):
    """
    Saves the current members dictionary to members.json
    """
    with open(MEMBERS_FILE, "w") as f:
        json.dump(members, f, indent=4)
    print("Member data saved.")

def is_book_available(book_id):
    if book_id in catalogue and catalogue[book_id]["copies"] > 0:
        return True
    return False


def borrow_allowed(member_profile):
    return len(member_profile["borrowed"]) < 3

def borrow_book(members):
    print("\n--- Borrow a Book ---")
    # Ask for member name and validate
    member_name = input("Enter member name: ").strip()
    if member_name not in members:
        print("Member not found.")
        return

    member_profile = members[member_name]

    # Check if member can borrow more books
    if not borrow_allowed(member_profile):
        print("You have reached the maximum borrow limit (3 books).")
        return

    # Ask for book ID
    book_id = input("Enter the book ID you want to borrow: ").strip()

    # Validate book exists
    if book_id not in catalogue:
        print("Invalid book ID.")
        return

    # Validate availability
    if not is_book_available(book_id):
        print(f"'{catalogue[book_id]['title']}' is currently unavailable.")
        return

    # Update catalogue copies
    catalogue[book_id]["copies"] -= 1

    # Append book to member list
    member_profile["borrowed"].append(book_id)

    print(f"You have successfully borrowed '{catalogue[book_id]['title']}'.")

    # Save updates
    save_members(members)
