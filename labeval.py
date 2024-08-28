book_isbn =dict()
book_title = dict()
book_author = dict()
book_genre = dict()


def add_book(isbn):
    book_title[isbn]=input("enter the name of the book:  ")
    book_author[isbn]=input("enter the name of the author:  ")
    book_genre[isbn]=input("enter the genre of book:  ")
    books = []
    for c in range(1):
        isbn = int(input("enyter the isbn"))
        books.append(isbn)
    book_title[isbn] = books
    
def update_book_details(isbn):
    print("enter new details")
    books=[]
    for i in range(10):
        book= input("enyer the new book details")
        books.append(book)
        book_isbn[isbn]=books
    print(books)


def search_byisbn(isbn):
    searchisbn = int(input("enter the isbn nmber"))
    for i in range(10):
        if searchisbn == isbn:
            print(books)

        else:
            print("not found")







    
        
            
