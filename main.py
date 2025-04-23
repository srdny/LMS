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
            input("Press anykey to continue...")
        elif choice == '6': 
            book.find_book_by_author()
            input("Press anykey to continue...")
        elif choice == '7':
            while True:
                try:
                    member_id = input('member id: ')
                    member_by_id = member.check_by_memberid(member_id) 
                    if member_by_id == None:
                        print("Member ID doesn't exist.") 
                        break 
                    else:
                        isbn = input('isbn: ')
                        book_by_isbn = book.check_by_isbn(isbn)
                        if book_by_isbn == None: 
                            print(f"Book with ISBN '{isbn}' not found.")
                        else:
                            if book_by_isbn["stock"] <= 0:
                                print("There is no copies available") 
                            else: 
                                member_book = {"book_title": book_by_isbn['title'],"isbn": book_by_isbn['isbn']}
                                book.borrow_book(isbn)
                                member.borrow_book(member_by_id,member_book)
                                print("Borrow Success !")
                        break

                except ValueError:
                    print("Invalid input. Please enter a number.")
            input("Press anykey to continue...") 
        elif choice == '8':
            while True:
                try:
                    member_id = input('member id: ')
                    member_by_id = member.check_by_memberid(member_id)
                    if member_by_id == None:
                        print("Member ID doesn't exist.") 
                        break
                    else:
                        if member_by_id['total_borrow_books'] <= 0:
                            print("Haven't borrowed anything yet")
                        else:
                            isbn = input('isbn: ')
                            book_by_isbn = book.check_by_isbn(isbn)
                            if book_by_isbn == None: 
                                print(f"Book with ISBN '{isbn}' not found.") 
                            else:
                                if member.return_book(member_by_id,book_by_isbn)  == 1:
                                    book.return_book(isbn)
                                    print("successfully returned the book")
                                else:
                                    print("Failed returned book")
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            input("Press anykey to continue...") 
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

    

    