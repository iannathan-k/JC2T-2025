class Library:
    book_count = 0
    def __init__(self, name, city):
        self.__name = name
        self.__city = city
        self.__books = []

    def addBook(self, book):
        self.__books.append(book)
        Library.book_count += 1

    def printBooks(self):
        for book in self.__books:
            print(f"{book.getTitle()}, by {book.getAuthor()} with {book.getPages()} pages")

class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages

    def getTitle(self):
        return self.__title
    
    def getAuthor(self):
        return self.__author
    
    def getPages(self):
        return self.__pages

lib = Library("BBS Library", "Jakarta")
book1 = Book("Harry Potter", "JK Rowling", "312")
book2 = Book("A-Level and AS-Level Computer Science", "David Watson", "457")
lib.addBook(book1)
lib.addBook(book2)
lib.printBooks()