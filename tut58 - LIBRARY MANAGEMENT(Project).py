'''
Create a library class
display book
lend book - (who owns the book if not present)
add book
return book

HarryLibrary = Library(listofbooks, libraryName)


dictionary (books-nameofperson)

create a main function and run an infinite while loop asking
users for their input '''

class Library():
    def __init__(self,booksList,Library_name):
        # creating a dictionary of all books keys
        self.lendData = {}
        self.booksList = booksList
        self.libraryName = Library_name

        # adding books to dictionary
        for books in self.booksList:
            # none means No author have lend this book
            self.lendData[books] = None

    def display_books(self):
        for index,books in enumerate(self.booksList):
            print(f"{index}){books}")

    def lend_book(self,book,author):
        if book in self.booksList:
            if self.lendData[book] is None:
                self.lendData[book] = author
            else:
                print(f"Sorry This book is lend by {self.lendData[book]}")
        else:
            print("You have written wrong book name")

    def return_book(self,book,author):
        if book in self.booksList:
            if self.lendData[book] is not None:
                self.lendData.pop(book)
            else:
                print("Sorry but This book is not Lend")
        else:
            print("You have written wrong book name")

    def add_book(self,book_name):
        self.booksList.append(book_name)
        self.lendData[book_name] = None

    def delete_book(self,book_name):
        self.booksList.remove(book_name)
        self.lendData.pop(book_name)

def main():
    # By deafault variables
    listBooks = ['Cookbook','Motu Patlu','Chacha_chaudhary','Rich Dad and Poor Dad']
    Library_name = 'Harry'
    secret_key = 123456

    Harry = Library(listBooks,Library_name)

    print(f"Welecome To {Harry.libraryName} library\n\nq for exit \nDisplay Book Using 'd' and add lend book using 'l' and Return a Book using 'r' \nAdd Book Using 'a' and Delete Book using 'del' \n ")

    Exit = False
    while (Exit is not True):
        _input = input("option:")
        print("\n")
        
        if _input == "q":
            Exit = True

        elif _input == "d":
            Harry.display_books()

        elif _input == "l":
            _input2 = input("What is your name:")
            _input3 = input("Which Book Do you want to lend:")
            print("\n Book Lend \n")
            Harry.lend_book(_input3,_input2)

        elif _input == "a":
            _input2 = input("Book name:")
            Harry.add_book(_input2)

        elif _input == "del":
            _input_secret = int(input("Write the secret key to delete:"))
            if (_input_secret == secret_key):
                _input2 = input("Book Which you want to delete:")
                Harry.delete_book(_input2)
            else:
                print("Sorry We can't Delete the Book")

        elif _input == "r":
            _input2 = input("What is your name:")
            _input3 = input("Which Book Do you want to return:")
            Harry.return_book(_input3,_input2)

if __name__ == "__main__":
    main()