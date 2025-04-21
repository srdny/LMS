from bookshelf import BookShelf
from member import Member

def main_menu():
    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add Book")
        print("2. Add Member")
        print("3. View All Books")
        print("4. View All Members")
        print("5. Find Book by Title")
        print("6. Find Book by Author")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. View Borrowed Books by Member")
        print("0. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            book.add_book()
        elif choice == '2':
            member.add_member() 
        elif choice == '3': 
            book.show_catalog()
            input("Press anykey to continue...")
        elif choice == '4': 
            member.view_members()
            input("Press anykey to continue...")
        elif choice == '5': 
            book.find_book_by_title()
            input("Press Enter to continue...")
        elif choice == '6': 
            book.find_book_by_author()
            input("Press Enter to continue...")
        elif choice == '7':
            print('2')
            #borrow_book()
        elif choice == '8':
            print('2')
            #return_book()
        elif choice == '9':
            print('2')
            #view_borrowed_books_by_member()
        elif choice == '0':
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9. 0 for Exit")    

if __name__ == "__main__":
    book = BookShelf()
    member = Member()
    main_menu()

    

    