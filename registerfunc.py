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

def register_member(members):
    print("\n--- Register New Member ---")

    # -------------------------
    # 1. Ask for the member's name
    # -------------------------
    name = input("Enter member name: ").strip()

    if name == "":
        print("Error: Name cannot be empty.")
        return

    if name in members:
        print("Error: This member already exists.")
        return

    # -------------------------
    # 2. Ask for age
    # -------------------------
    age_input = input("Enter age: ").strip()

    if not age_input.isdigit():
        print("Error: Age must be a number.")
        return

    age = int(age_input)
    if age < 1:
        print("Error: Age must be at least 1.")
        return

    # -------------------------
    # 3. Membership type
    # -------------------------
    print("Membership types available: basic / premium")
    membership = input("Enter membership type: ").strip().lower()

    if membership not in ["basic", "premium"]:
        print("Error: Invalid membership type.")
        return

    # -------------------------
    # 4. Build member profile
    # -------------------------
    profile = {
        "age": age,
        "membership": membership,
        "borrowed": []      # always start empty
    }

    # -------------------------
    # 5. Add to global members + save
    # -------------------------
    members[name] = profile
    save_members(members)

    print(f"Member '{name}' successfully registered.")

