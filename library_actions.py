import pandas as pd
import os

# Setup path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "library_data.xlsx")

def load_books():
    """Loads the Excel file into a DataFrame."""
    try:
        df = pd.read_excel(FILE_PATH)
        if df.empty:
            return pd.DataFrame(columns=["BookID", "Title", "Author", "Status"])
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=["BookID", "Title", "Author", "Status"])

def save_books(df):
    """Helper to save the DataFrame to Excel."""
    df.to_excel(FILE_PATH, index=False)

def add_book_logic():
    """Adds a book with validation against empty inputs."""
    print("\n--- Add New Book ---")
    
    # 1. Input Validation Loop
    b_id = input("Enter Book ID: ")
    if not b_id.strip():
        print("Error: Book ID cannot be empty or just spaces.")
        return

    title = input("Enter Book Title: ")
    if not title.strip():
        print("Error: Title cannot be empty.")
        return

    author = input("Enter Author Name: ")
    if not author.strip():
        print("Error: Author cannot be empty.")
        return
    
    df = load_books()
    
    if not df.empty and str(b_id) in df['BookID'].astype(str).values:
         print(f"Error: Book ID {b_id} already exists.")
         return

    new_data = {"BookID": b_id, "Title": title, "Author": author, "Status": "Available"}
    new_df = pd.DataFrame([new_data])
    
    df = pd.concat([df, new_df], ignore_index=True)
    save_books(df)
    print(f"Success: '{title}' added.")

def view_books_logic():
    """Prints books in a aligned table format."""
    df = load_books()
    
    print("\n" + "="*75)
    header_format = "{:<10} {:<30} {:<20} {:<15}"
    print(header_format.format("BookID", "Title", "Author", "Status"))
    print("-" * 75)
    
    if df.empty:
        print("No books found in the library.")
    else:
        for index, row in df.iterrows():
            if str(row['Title']).strip(): 
                print(header_format.format(
                    str(row['BookID']), 
                    str(row['Title']), 
                    str(row['Author']), 
                    str(row['Status'])
                ))
    print("="*75 + "\n")

def borrow_book_logic():
    """Updates status to 'Borrowed'."""
    print("\n--- Borrow a Book ---")
    search_id = input("Enter Book ID to borrow: ").strip()
    
    if not search_id:
        print("Error: ID cannot be empty.")
        return

    df = load_books()
    
    if df.empty:
        print("Library is empty.")
        return

    # Find the row index where BookID matches
    mask = df['BookID'].astype(str) == str(search_id)
    
    if not mask.any():
        print("Error: Book ID not found.")
        return

    # Get the index of the book
    book_index = df.index[mask].tolist()[0]
    
    if df.at[book_index, 'Status'] == 'Borrowed':
        print(f"Sorry, Book {search_id} is already borrowed.")
    else:
        df.at[book_index, 'Status'] = 'Borrowed'
        save_books(df)
        print(f"Success! Book {search_id} issued.")

def return_book_logic():
    """Updates status to 'Available'."""
    print("\n--- Return a Book ---")
    search_id = input("Enter Book ID to return: ").strip()
    
    if not search_id:
        print("Error: ID cannot be empty.")
        return

    df = load_books()
    
    if df.empty:
        print("Library is empty.")
        return

    mask = df['BookID'].astype(str) == str(search_id)
    
    if not mask.any():
        print("Error: Book ID not found.")
        return

    book_index = df.index[mask].tolist()[0]
    
    if df.at[book_index, 'Status'] == 'Available':
        print(f"Error: Book {search_id} is already in the library (Available).")
    else:
        df.at[book_index, 'Status'] = 'Available'
        save_books(df)
        print(f"Success! Book {search_id} returned.")

def delete_book_logic():
    """Removes a book from the Excel file."""
    print("\n--- Delete a Book ---")
    search_id = input("Enter Book ID to delete: ").strip()
    
    if not search_id:
        print("Error: ID cannot be empty.")
        return

    df = load_books()
    
    if df.empty:
        print("Library is empty.")
        return
    mask = df['BookID'].astype(str) == str(search_id)
    
    if not mask.any():
        print(f"Error: Book ID {search_id} not found.")
        return

    df = df[~mask]
    
    save_books(df)
    print(f"Success! Book {search_id} has been deleted permanently.")