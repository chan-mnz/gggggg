# Save Member Data To File Function

def save_member():
    member_id = generate_member_id()
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    mtype = input("Enter Type: ")

    borrowed_books = []  # new members always start with empty list

    # THIS LINE CREATES catalog.txt IF NOT EXISTING
    with open("catalog.txt", "a") as f:
        f.write(f"{member_id}, {name}, {age}, {mtype}, {borrowed_books}\n")

    print("\nSaved Successfully!")
    print(f"Generated ID: {member_id}\n")