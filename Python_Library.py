# Available books list
a_books = ['The Adventures of Mario', 'Bowsers Hunt', 'Peach On The Fly']
# Borrowed books list
b_books = []


# Function that is used for the display menu
def display_menu():
    print("Welcome to Mario's Library! Choose an option below")
    print("a.) Display both available and borrowed books")
    print("b.) Borrow a book")
    print("c.) Return a book")
    print("d.) Exit the program")

# Function will be used to display the books
def display_books():
    print("Books Available:")
    for aval in a_books:
        print(f"{aval}")
    print("Books Borrowed:")
    if not b_books:
        print("There are no books borrowed!")
    else:
        # For Loop will go through and list the book in the borrowed books list if any are in there
        for borr in b_books:
            print(f"{borr}")


#Function will be used if user wants to borrow a book
def borrow_book():
    display_books()
    book = input("\n Enter name of the book you want to borrow: ").strip()
        # Will remove book from a_book list and append it to b_book list
    if book in a_books:
        a_books.remove(book)
        b_books.append(book)
        print(f"\n You borrowed {book}.")
    else:
        print(f"\n Sorry that {book} is not in our library")

# Function will be used if user wants to return a book
def return_book():
    if not b_books:
        print("\n You have no books to return!")
        return
    display_books()
    book = input("\n Enter the name of the book you want to return: ").strip()
    # Will remove book from b_book and append to a_book
    if book in b_books:
        b_books.remove(book)
        a_books.append(book)
        print(f"\n You have returner {book}")
    else:
        print(f"\nYou don't have a borrowed book")

# Function that is used for the movie program
def bookstore():

    # While loop for re-prompt
    while True:
        display_menu()
        # User choice
        choice = input("\n Choose an option (a,b,c,d): ").lower()
        if choice == "a":
            display_books()
        elif choice == "b":
            borrow_book()
        elif choice == "c":
            return_book()
        elif choice == "d":
            print("\n Goodbye! Have a great day!")
            break
        else:
            print("\n Invalid choice. Please try again")



 # Function will be called here
if __name__ == "__main__":
    bookstore()