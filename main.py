import library_actions 

def main():
    while True:
        print("\n=== LIBRARY MANAGEMENT SYSTEM ===")
        print("1. Add a New Book")
        print("2. View All Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Delete a Book")       # <--- NEW
        print("6. Exit")                # <--- UPDATED NUMBER
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == '1':
            library_actions.add_book_logic()
        elif choice == '2':
            library_actions.view_books_logic()
        elif choice == '3':
            library_actions.borrow_book_logic()
        elif choice == '4':
            library_actions.return_book_logic()
        elif choice == '5':             # <--- NEW LOGIC
            library_actions.delete_book_logic()
        elif choice == '6':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()