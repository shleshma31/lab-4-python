#contact book
import os

FILE_PATH = "contacts.txt"

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    if not name or not phone:
        print("Invalid input")
        return
    with open(FILE_PATH, "a", encoding="utf-8") as f:
        f.write(f"{name},{phone}\n")
    print("Contact added")

def view_contacts():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = f.read().strip()
    except FileNotFoundError:
        print("No contacts file found")
        return
    if not data:
        print("No contacts")
        return
    lines = data.splitlines()
    for i, line in enumerate(lines, 1):
        print(f"{i}. {line}")

def search_contacts():
    q = input("Search name: ").strip().lower()
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            lines = [l.strip() for l in f if l.strip()]
    except FileNotFoundError:
        print("No contacts file found")
        return
    results = [l for l in lines if q in l.split(",")[0].lower()]
    if not results:
        print("No match")
        return
    for i, r in enumerate(results, 1):
        print(f"{i}. {r}")

def menu():
    while True:
        print("\n1. Add\n2. View\n3. Search\n4. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()

#banking system
import os

FILE_PATH = "contacts.txt"

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    if not name or not phone:
        print("Invalid input")
        return
    with open(FILE_PATH, "a", encoding="utf-8") as f:
        f.write(f"{name},{phone}\n")
    print("Contact added")

def view_contacts():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = f.read().strip()
    except FileNotFoundError:
        print("No contacts file found")
        return
    if not data:
        print("No contacts")
        return
    lines = data.splitlines()
    for i, line in enumerate(lines, 1):
        print(f"{i}. {line}")

def search_contacts():
    q = input("Search name: ").strip().lower()
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            lines = [l.strip() for l in f if l.strip()]
    except FileNotFoundError:
        print("No contacts file found")
        return
    results = [l for l in lines if q in l.split(",")[0].lower()]
    if not results:
        print("No match")
        return
    for i, r in enumerate(results, 1):
        print(f"{i}. {r}")

def menu():
    while True:
        print("\n1. Add\n2. View\n3. Search\n4. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()