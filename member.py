import random

class Member:
    def __init__(self):
        self.members=[]

    def add_member(self):
        while True:
            member_id = random.randint(1000000,1999999)
            name = input("Enter member name: ")
            member = {"member_id": member_id, "name": name, "total_borrow_books":0, "borrow_books":{} }
            self.members.append(member)
            print(f"Member '{name}' added successfully!")
            while True:
                choice = input("Add Again ? [Y/N]: ").upper()
                if choice in ("Y", "N"):
                    break
                else :
                    print("Invalid input. Please enter 'Y' or 'N'.")
            if choice == "N":
                break
    
    def view_members(self):
        if not self.members:
            print("No members registered.")
            return
        print("\n--- All Members ---")
        for member in self.members:
            print(f"ID: {member['member_id']}, Name: {member['name']}, Total Borrow Book: {member['total_borrow_books']}")
        print("-------------------")