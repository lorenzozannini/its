class Libro:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.status=False

class Biblioteca:
    def __init__(self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)
        print(f"{book} aggiunto alla Biblioteca")
    
    def borrow_book(self,title):
        for book in self.books:
            if book.title==title and book.status==False:
                book.status=True
                print(f"{book.title} preso in prestito")
                break
        print(f"{book.title} non disponibile")
    
    def return_book(self,title):
        for book in self.books:
            if book.title==title and book.status==True:
                book.status=False
                print(f"{book.title} restituito")
                break
        print(f"{book.title} non possibile restituire")

    def show_available_books(self):
        available=[]
        for book in self.books:
            if book.status==False:
                available.append(book.title)
        if available!=[]:
            return available
        else:
            return f"Nessun libro disponibile nella biblioteca"