import random

class Member:
    def __init__(self):
        self.members=[]
        self.counter_id = {"value": 1}

    def auto_increament(self, width=4):
        def increment():
            current = self.counter_id["value"]
            self.counter_id["value"]+=1
            return f"{current:0{width}}"
        return increment
        

    def add_member(self):
        incrementer = self.auto_increament()
        while True:
            member_id = incrementer()
            name = input("Enter member name: ")
            member = {"member_id": member_id, "name": name, "total_borrow_books":0, "borrow_books":[] }
            self.members.append(member)
            print(f"Member '{name}',Member_id '{member_id}' added successfully!")
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
            if member['total_borrow_books']<= 0:
                print(f"ID: {member['member_id']}, Name: {member['name']}, Total Borrow Book: {member['total_borrow_books']}")
            else:
                print(f"ID: {member['member_id']}, Name: {member['name']}, Total Borrow Book: {member['total_borrow_books']}, Borrow Book: {member['borrow_books']}")
        print("-------------------")
    
    def check_by_memberid(self,member_id): 
        member_by_id = next((m for m in self.members if m['member_id'] == member_id), None)
        return member_by_id
    
    def borrow_book(self,member_by_id,book):
        index = next((i for i, d in enumerate(self.members) if d["member_id"] == member_by_id['member_id']), -1)
        self.members[index]['total_borrow_books'] += 1
        self.members[index]['borrow_books'].append(book)
    
    def return_book(self,member_by_id,book):
        index = next((i for i, d in enumerate(self.members) if d["member_id"] == member_by_id['member_id']), -1)
        if self.members[index]['borrow_books']['isbn'] == book['isbn']:
            self.members[index]['total_borrow_books'] -= 1 
            index2 = next((i for i, d in enumerate(self.members[index]['borrow_books']) if d["isbn"] == book['isbn']), -1)
            self.members[index]['borrow_books'].pop(index2)
            return 1
        else:
            return 0
        