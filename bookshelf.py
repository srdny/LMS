class BookShelf:

    def __init__(self):
        self.books = []

    def show_catalog(self):
        if not self.books:
            print("No books registered.")
            return
        for book in self.books: 
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Available Stocks: {book['stock']}")
            print("------------------------------------------------")

    def add_book(self):
        while True:
            title = input("Enter book title: ")
            author = input("Enter author: ") 
            isbn = input("Enter isbn: ") 
            while True:
                try:
                    stock = int(input("Enter number of stock: "))
                    if stock > 0:
                        break
                    else:
                        print("Number of stock must be positive.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            
            book = {"title": title, "author": author, "isbn": isbn, "stock": stock}
            self.books.append(book)
            
            while True:
                choice = input("Add Again ? [Y/N]: ").upper()
                if choice in ("Y", "N"):
                    break
                else :
                    print("Invalid input. Please enter 'Y' or 'N'.")
            if choice == "N":
                break
        
    def find_book_by_title(self):
        title = input("Enter the title to search: ").lower()
        found_books = [book for book in self.books if title in book['title'].lower()]
        if found_books:
            print("\n--- Found Books ---")
            for book in found_books:
                print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Available Stocks: {book['stock']}")
            print("-------------------")
        else:
            print(f"No books found with the title '{title}'.")

    def find_book_by_author(self):
        author = input("Enter the author to search: ").lower()
        found_books = [book for book in self.books if author in book['author'].lower()]
        if found_books:
            print("\n--- Found Books ---")
            for book in found_books:
                print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Available Stocks: {book['stock']}")
            print("-------------------")
        else:
            print(f"No books found by the author '{author}'.")

    def check_by_isbn(self,isbn):
        book = next((b for b in self.books if b['isbn'] == isbn), None)
        return book
    
    def book_borrow(self,isbn):
        #found_books = [book for book in self.books if isbn in book['isbn']]
        index = next((i for i, d in enumerate(self.books) if d["isbn"] == isbn), -1)
        self.books[index]['stock'] -= 1
 
        # found_books['stock'] -= 1
        # print(f"Title: {found_books['title']}, Author: {found_books['author']}, ISBN: {found_books['isbn']}, Available Stocks: {found_books['stock']}")
        
        



