def generate_member_id():
    try:
        with open("members.txt", "r") as f:
            lines = f.readlines()


        if len(lines) == 0:
            return "LIB-2025-0001"


        last_id = lines[-1].strip()


        number = int(last_id.split("-")[2])
        new_number = number + 1

        return "LIB-2025-" + str(new_number).zfill(4)

    except FileNotFoundError:

        return "LIB-2025-0001"



new_id = generate_member_id()

with open("members.txt", "a") as f:
    f.write(new_id + "\n")

print("Generated ID:", new_id)
