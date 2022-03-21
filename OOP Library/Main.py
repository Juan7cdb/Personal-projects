from cProfile import run
from pydoc import synopsis
from Book import Book
from Library import Library


if __name__ == "__main__":
    run = True
    
    
    while(run):
        print("- - - WELCOME TO THE LIBRARY - - -")
        option = int(input("""
                           Options to perform:
                           
                           1 - Create library.
                           
                           2 - Add book.
                           
                           3 - See catalog.
                           
                           4 - Delete book.
                           
                           5 - Exit.
                           """))
        
        
        if option == 1:
            name = input("Name of the library: ")
            name = name.capitalize()
            library = Library(name)
            
            print("Se creo la biblioteca: {}".format(Library.Search_name_library))
            
        elif option == 2:
            book_title = (str(input("Book`s title: ")).capitalize())
            book_author = (str(input("Book`s author: ")).capitalize())
            book_genre = (str(input("Book`s genre: ")).capitalize())
            publisher = (str(input("Book`s publisher: ")).capitalize())
            pages_number = (str(input("Book`s nuber pages: ")).capitalize())
            sinopsis= (str(input("Book`s synopsis: ")).capitalize())
            
            book = Book(book_title, book_author, book_genre, publisher, pages_number, sinopsis)
            Library.Add_book(book)
            
        elif option == 3:
            print("Book´s catalog: ")
            for i in Library.Search_book():
                print(i)
                
        elif option == 4:
            index = input("Book´s ID to delete: ")
            Library.Delete_book(index)
            
        elif option == 5:
            run = False
            
        else:
            print("Incorrect choice.")