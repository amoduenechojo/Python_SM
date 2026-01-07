print("Welcome to the Book Suggestion System!");       
    String Suggestion = input.nextLine();

    String bookSystem = """
        Tap 1: To Get Suggestions
        Tap 2: To Add book
        Tap 3: To Remove book
        Tap 4: To Update book
        Tap 5: To Show all books
        """;

    print(bookSystem);
    print("Enter your choice: ");
    int bookSystemOption = input.nextInt();

   match (bookSystemOption)
        case 1 -> 
                print("To Get Suggestions");
                String options = """
                        Book of the Day:
                            Book Title: Hafastu Bebi
                            Page: 47
                            """;
                print(options);

   print("Enter a number to see details (1-3): ");
                int suggestionsChoice = input.nextInt();

               match (suggestionsChoice)
                    case 1 -> print("Book of the Day: ");
                    case 2 -> print("Book Title: Hafastu Bebi");
                    case 3 -> print("Page: 47 ");
            
                System.out.println("Would you like another book suggestion? (yes/no): ");
                String response = input.next(); 
                print("Book Title: Broken");
                print("Page 12");

    print("Enter book title to add:");
    int addBookOption = input.nextInt(); 
    match (addBookOption)                
        case 2 -> 
                  print("To Add book");
                    String addOption = """
                           Enter the book title: The Chosen;
                           Book added successfully!
                        """;
                   print(addOption);
                 

           case 1-> print("Enter the book title: The Chosen");
           case 3-> print("Book added successfully!");
    

    System.out.println("Enter your choice:");
    int removeBookOption = input.nextInt(); 
    switch (removeBookOption)
        case 3 ->
                   print("To Remove book");
                    String removeOption = """
                           Enter the book title to remove:The Chosen;
                           Book removed successfully! 
                        """;
                   print(removeOption);  


    print("Enter your choice:");
    int updateBookOption = input.nextInt(); 
    switch (updateBookOption)
        case 4 -> 
                   print("To Update book");
                    String updateOption = """
                            Enter the old title: Chi kind
                            Enter the latest title: Chicken kingdom
                            Book updated successfully!
                        """;
                   print(updateOption);  
  

   print("Enter your choice:");
    int showAllBooksOptions = input.nextInt();    
    switch (showAllBooksOptions)
        case 5 -> 
                 print("To Show all books");
                   String allOptions = """        
                           All Books
                            1. Hafastu Bebi
                            2. Broken
                            3. The Chosen
                            4. Unchained
                    """;
                   print(allOptions);
        
   
