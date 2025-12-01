# Library Management System

#Book Class
class Book:
  def __init__(self, title, author, isbn,):
    self.title = title
    self.author = author
    self.isbn = isbn
    self.avalibility = True
  
  def borrow_book(self):
    if self.avalibility:
      self.avalibility = False
      return True
    return False
  
  def return_book(self):
      self.avalibility = True
  
  def display_info(self):
    status = "Available" if self.avalibility else "Not Available"
    print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}")

  

# Member Class
class Member:
  def __init__(self, name, member_id,):
    self.name = name
    self.member_id = member_id
    self.borrowed_books = []

  def borrow_book(self, book):
    if book.borrow_book():
      self.borrowed_books.append(book)
      print(f"{self.name} borrowed {book.title}.")
    else:
        print(f"{book.title} is not available for borrowing.")
  
  def return_book(self, book):
    if book in self.borrowed_books:
      book.return_book()
      self.borrowed_books.remove(book)
      print(f"{self.name} returned {book.title}.")
    else:
      print(f"{self.name} did not borrow {book.title}.")
  
  def display_borrowed_books(self):
    if not self.borrowed_books:
      print(f"{self.name} has not borrowed any books")
    else:
      print(f"{self.name}'s borrowed books:")
      for book in self.borrowed_books:
        print(f"- {book.title}")

# Creating Book Instances

book1 = Book("Harry Potter", "J.K. Rowling", "9780747532743")
book2 = Book("The Alchemist", "Paulo Coelho", "9780061122415")

member1 = Member("Lubhansh Sharma", "M001")

# Display Book Info
book1.display_info()
book2.display_info()

print("\n--- Borrowing Books ---")
member1.borrow_book(book1)
member1.borrow_book(book1)

print("\n--- Borrowed Books List ---")
member1.display_borrowed_books()

print("\n--- Returning Books ---")
member1.return_book(book1)

print("\n--- Borrowed Books After Returning ---")
member1.display_borrowed_books()

print("\n--- Final Book Info ---")
book1.display_info()
book2.display_info()