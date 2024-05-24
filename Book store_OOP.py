"""Book store"""


class Book:
    def __init__(self, title: str, author: str, price: float, rating: float):
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating
    
    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, price={self.price}, rating={self.rating})"


class Store:
    def __init__(self, name: str, rating: float):
        self.name = name
        self.rating = rating
        self.books = []

    def can_add_book(self, book: Book) -> bool:
        if book.rating < self.rating:
            return False
        for b in self.books:
            if b.title == book.title and b.author == book.author:
                return False
        return True

    def add_book(self, book: Book):
        if self.can_add_book(book):
            self.books.append(book)

    def can_remove_book(self, book: Book) -> bool:
        for b in self.books:
            if b.title == book.title and b.author == book.author:
                return True
        return False

    def remove_book(self, book: Book):
        if self.can_remove_book(book):
            self.books = [b for b in self.books if not (b.title == book.title and b.author == book.author)]

    def get_all_books(self) -> list:
        return self.books

    def get_books_by_price(self) -> list:
        return sorted(self.books, key=lambda book: book.price)

    def get_most_popular_book(self) -> list:
        if not self.books:
            return []
        highest_rating = max(book.rating for book in self.books)
        return [book for book in self.books if book.rating == highest_rating]



if __name__ == "__main__":
    
    book1 = Book("Title1", "Author1", 25.5, 4.5)
    book2 = Book("Title2", "Author2", 15.0, 4.7)
    book3 = Book("Title3", "Author1", 30.0, 4.8)
    book4 = Book("Title4", "Author3", 20.0, 4.2)
    book5 = Book("Title1", "Author1", 22.0, 4.5)
    
  
    store = Store("BookStore", 4.0)
    

    store.add_book(book1)
    store.add_book(book2)
    store.add_book(book3)
    store.add_book(book4)
    store.add_book(book5)  

    
    store.remove_book(book4)
    
    
    print("All books in the store:", store.get_all_books())
    
    
    print("Books sorted by price:", store.get_books_by_price())
    
    
    print("Most popular book(s):", store.get_most_popular_book())
