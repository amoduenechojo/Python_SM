import random

print("Welcome to the Book Suggestion System!") 

Suggestion = input.nextLine()

def book_system = """
    Tap 1: To Get Suggestions
    Tap 2: To Add book
    Tap 3: To Remove book6
    Tap 4: To Update book
    Tap 5: To Show all books
    """

print(book_system)
print("Enter your choice: ")
     


book_system_option = input.nextInt()

match (book_system_option):
    case 1:
            print("To Get Suggestions")
            options = """
                    Book of the Day:
                        Book Title: Hafastu Bebi
                        Page: 47
                        """
            print(options)

print("Enter a number within (1-3): ")
           suggestions_choice = input.nextInt()

           match (suggestionsChoice)
                case 1 -> print("Book of the Day: ")
                case 2 -> print("Book Title: Hafastu Bebi")
                case 3 -> print("Page: 47")
        
            print("Would you like another book suggestion? (yes/no): ")
                 response = input.nextLine()
            print("Book Title: Broken")
            print("Page 12")

print("Enter book title to add: ")
     add_book_option = input.nextInt() 
match (add_book_option)                
    case 2 -> 
              print("To Add book")
                String add_option = """
                       Enter the book title: The Chosen
                       Book added successfully!
                    """
               print(add_option)
             

       case 1-> print("Enter the book title: The Chosen")
       case 3-> print("Book added successfully!")


print("Enter your choice: ")
int remove_book_option = input.nextInt() 
switch (remove_book_option)
    case 3 ->
               print("To Remove book")
                String remove_option = """
                       Enter the book title to remove:The Chosen
                       Book removed successfully! 
                    """
               print(remove_option) 


print("Enter your choice:")
int update_book_option = input.nextInt()
switch (update_book_option)
    case 4 -> 
               print("To Update book")
                String update_option = """
                        Enter the old title: Three together
                        Enter the latest title: Me, Micheal and God
                        Book updated successfully!
                    """;
               print(update_option)  


print("Enter your choice: ")
int show_all_books_options = input.nextInt()    
switch (show_all_books_options)
    case 5 -> 
             print("To Show all books")
               String all_options = """        
                       All Books
                        1. Hafastu Bebi
                        2. Broken
                        3. The Chosen
                        4. Unchained
                """
               print(all_options)
    


















































