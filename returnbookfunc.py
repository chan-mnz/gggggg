# ============================================================
# RETURN BOOK FLOW
# ============================================================
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


# ============================================================
# JSON SAVE/LOAD FUNCTIONS
# ============================================================

def load_members():
    """
    Loads member data from members.json if it exists.
    """
    global members

    if not os.path.exists(MEMBERS_FILE):
        print("No member file found. Starting with empty records.")
        members = {}
        return

    try:
        with open(MEMBERS_FILE, "r") as f:
            members = json.load(f)
        print(f"Loaded {len(members)} members from {MEMBERS_FILE}.")
    except json.JSONDecodeError:
        print("Error reading JSON file. Starting with empty records.")
        members = {}


def save_members():
    """
    Saves the current members dictionary to members.json
    """
    with open(MEMBERS_FILE, "w") as f:
        json.dump(members, f, indent=4)
    print("Member data saved.")


def return_book():
    print("\n--- Return a Book ---")

    # TODO: ask for member name
    name = ""
    while (name not in members):
        name = input("Enter your name: ")
        if name not in members:
            print("Member not found. Try again.")
    # TODO: show borrowed books
    borrowed_list = members[name]["borrowed"]
    if len(borrowed_list) == 0:
        print("You have no borrowed books.")
        return

    print("\nYour borrowed books:")
    for book_id in borrowed_list:
        book = catalogue[book_id]
        print(f"- {book_id}: {book['title']} ({book['author']})")
    # TODO: ask which book they want to return
    return_id = ""
    while True:
        return_id = input("Enter the book ID you want to return: ").strip()

        if return_id not in members[name]["borrowed"]:
            print("You did not borrow that book. Try again.")
        else:
            break
    # TODO: update catalogue and member record
    catalogue[return_id]["copies"] += 1
    members[name]["borrowed"].remove(return_id)
    # TODO: save_members()
    save_members()
    return None

