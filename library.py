# ==========================================
# LIBRARY CATALOGUE
# ==========================================
print("test")
catalogue = {
    "book_001": {"title": "1984", "author": "George Orwell", "copies": 3},
    "book_002": {"title": "The Hobbit", "author": "J.R.R. Tolkien", "copies": 2},
    "book_003": {"title": "Python Basics", "author": "A. Smith", "copies": 5}
}


# ==========================================
# MEMBERSHIP SYSTEM
# ==========================================

members = {
    "mem_001": {"name": "Alice", "active": True,  "borrowed": 1},
    "mem_002": {"name": "Ben",   "active": True,  "borrowed": 3},
    "mem_003": {"name": "Cara",  "active": False, "borrowed": 0}
}


def is_member_valid(member_id):
    return member_id in members and members[member_id]["active"]


def borrowing_allowed(current_books):
    return current_books < 3


# ==========================================
# LATE FEE RULES
# ==========================================

BORROW_PERIOD = 14        # days
LATE_FEE_PER_DAY = 0.50   # 50p/day


def days_late(days_borrowed):
    return max(0, days_borrowed - BORROW_PERIOD)


def calculate_late_fee(days_late_value):
    return days_late_value * LATE_FEE_PER_DAY


# ==========================================
# BOOK CHECKER
# ==========================================

def is_book_available(book_id):
    if book_id not in catalogue:
        return False
    return catalogue[book_id]["copies"] > 0


# ==========================================
# BORROW BOOK FEATURE
# ==========================================

def borrow_book(member_id, book_id):
    if not is_member_valid(member_id):
        return "❌ Membership invalid or inactive."

    member = members[member_id]

    if not borrowing_allowed(member["borrowed"]):
        return "❌ Borrowing limit reached (max 3 books)."

    if not is_book_available(book_id):
        return "❌ Book not available."

    catalogue[book_id]["copies"] -= 1
    member["borrowed"] += 1

    return f"✅ {member['name']} borrowed '{catalogue[book_id]['title']}' successfully!"


# ==========================================
# MAIN PROGRAM (MENU)
# ==========================================

def show_menu():
    print("\n===== LIBRARY SYSTEM MENU =====")
    print("1. View Catalogue")
    print("2. Check Book Availability")
    print("3. Borrow a Book")
    print("4. Calculate Late Fee")
    print("5. Exit")
    print("===============================")


def view_catalogue():
    print("\n--- Library Catalogue ---")
    for book_id, info in catalogue.items():
        print(f"{book_id}: {info['title']} by {info['author']} (copies: {info['copies']})")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_catalogue()

        elif choice == "2":
            book_id = input("Enter book ID: ")
            if is_book_available(book_id):
                print("✅ Book is available.")
            else:
                print("❌ Book is NOT available.")

        elif choice == "3":
            member_id = input("Enter member ID: ")
            book_id = input("Enter book ID: ")
            result = borrow_book(member_id, book_id)

if __name__ == "__main__":
    main()