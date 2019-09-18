class Book:
    def __init__(self, title="Software Engineering", isbn=""):
        self.title = title
        self.isbn = isbn

    def printBook(self):
        print(self.title + ", " + self.isbn)
        print(Book.printBook('Software'+'5'))

def main():
    book1 = Book("Harry potter", 657923489263)
    book1  .printBook()

if __name__ == '__main__':
    main()