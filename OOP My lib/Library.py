class Library:
    
    
    def __init__(self, name):
        self.name = name
        self._books = []
        
        
    def Search_name_library(self):
        return self.name
    
    
    def Add_book(self, book):
        self._books.append({
            book.book_title,
            book.book_author,
            book.book_genre,
            book.pages_number,
            book.publisher,
            book.synopsis
        })
        
    
    def Search_book(self):
        return self._books
    
    
    def Search_book_id(self, id):
        return self._books[id]
    
    
    def Delete_book(self, id):
        self._books.pop(id)