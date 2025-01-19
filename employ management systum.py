class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print('---')


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        isbn = input("Enter the book ISBN: ")
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books is in the library.")
        else:
            for book in self.books:
                book.display()

    def search_book(self):
        search_title = input("Enter the book title to search: ")
        found_books = [book for book in self.books if book.title.lower() == search_title.lower()]

        if not found_books:
            print("No books found with that title.")
        else:
            for book in found_books:
                book.display()

    def menu(self):
        while True:
            print("\nLibrary Menu")
            print("1. Add a Book")
            print("2. View All Books")
            print("3. Search for a Book")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.view_books()
            elif choice == '3':
                self.search_book()
            elif choice == '4':
                print("Exiting the library system. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    library = Library()
    library.menu()
