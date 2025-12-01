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


MEMBERS_FILE = "members.json"


# ============================================================
# JSON SAVE/LOAD FUNCTIONS
# ============================================================



def save_members(members):
    """
    Saves the current members dictionary to members.json
    """
    with open(MEMBERS_FILE, "w") as f:
        json.dump(members, f, indent=4)
    print("Member data saved.")


def return_book(members):
    print("\n--- Return a Book ---")

    #ask for member name
    name = ""
    while (name not in members):
        name = input("Enter your name: ")
        if name not in members:
            print("Member not found. Try again.")
    # show borrowed books
    borrowed_list = members[name]["borrowed"]
    if len(borrowed_list) == 0:
        print("You have no borrowed books.")
        return

    print("\nYour borrowed books:")
    for book_id in borrowed_list:
        book = catalogue[book_id]
        print(f"- {book_id}: {book['title']} ({book['author']})")
    # ask which book they want to return
    return_id = ""
    while True:
        return_id = input("Enter the book ID you want to return: ").strip()

        if return_id not in members[name]["borrowed"]:
            print("You did not borrow that book. Try again.")
        else:
            break
    #update catalogue and member record
    catalogue[return_id]["copies"] += 1
    members[name]["borrowed"].remove(return_id)
    # save_members()
    save_members(members)

