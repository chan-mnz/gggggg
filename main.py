"""
Week 2 – Library Borrowing System
Starter Template Code (Student Version)

Now includes:
- JSON save/load for members
"""

import json
import os
import returnbookfunc
import borrowbookfunc
import viewmemfunc

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


# ============================================================
# TASK 1 – REGISTER A USER (INPUT + VALIDATION)
# ============================================================

def register_member():
    print("\n--- Register New Member ---")

    # TODO: ask for the member's name

    # TODO: validate name is not empty and not already in members

    # TODO: ask for age and validate

    # TODO: ask for membership type

    # TODO: build profile dictionary

    # TODO: add to global members
    # members[name] = profile

    # TODO: save immediately
    # save_members()

    print("TODO: implement register_member()")
    return None


# ============================================================
# SUPPORT FUNCTIONS FOR BORROW FLOW
# ============================================================

def is_book_available(book_id):
    if book_id in catalogue and catalogue[book_id]["copies"] > 0:
        return True
    return False


def borrow_allowed(member_profile):
    return len(member_profile["borrowed"]) < 3


# ============================================================
# TASK 2 – BORROW BOOK FLOW
# ============================================================

def borrow_book():
    borrowbookfunc.borrow_book()


# ============================================================
# RETURN BOOK FLOW
# ============================================================

def return_book():
    returnbookfunc.return_book()


# ============================================================
# VIEW MEMBER DETAILS
# ============================================================

def view_member_details():
    viewmemfunc.view_member_details()


# ============================================================
# MAIN MENU LOOP
# ============================================================

def main_menu():
    while True:
        print("\n=== Library System Menu ===")
        print("1) Register new member")
        print("2) Borrow a book")
        print("3) Return a book")
        print("4) View member details")
        print("5) Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            register_member()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            view_member_details()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


# ============================================================
# ENTRY POINT
# Load JSON and start program
# ============================================================

if __name__ == "__main__":
    load_members()
    main_menu()
    save_members()