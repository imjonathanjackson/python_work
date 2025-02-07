class Book():
    
    favorites = []
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        if self.pages > 100:
            return True
        return False

    def __str__(self):
        return f"{self.title} is {self.pages} pages long."
    
    def __eq__(self, other):
        if self.title == other.title and self.author == other.author and self.pages == other.pages:
            return True
        return False
    
    def __hash__ (self):
        return hash(self.title) ^ hash(self.author) ^ hash(self.pages)

book = Book("Margin of Safety", "Seth Klarman", 288)
book2 = Book("Crash Proof", "Peter Schiff", 98)
book3 = Book("Margin of Safety", "Seth Klarman", 288)

Book.favorites.append(book)
Book.favorites.append(book2)

for b in Book.favorites:
    print(b)

books = (book, book2, book3)

print(book == book3)
print(hash(book) == hash(book3))
print(id(book), id(book3))
print(book is book2)