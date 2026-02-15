class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' added")

    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"Book '{book_name}' removed")
        else:
            print("Book not found")

    def search_book(self, book_name):
        if book_name in self.books:
            print(f"'{book_name}' is available")
        else:
            print(f"'{book_name}' is not available")

    def display_books(self):
        print("\n--- Library Books ---")
        for book in self.books:
            print("-", book)


# Driver code
library = Library()
library.add_book("Python Basics")
library.add_book("Machine Learning")
library.search_book("Python Basics")
library.remove_book("Machine Learning")
library.display_books()
