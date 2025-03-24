import json,os,textwrap


class Book :
    def __init__(self, title, author, publication_year,genre,read_status):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.read_status = read_status


Books:list = []
# Books = ({})

BOOKS_FILE = 'books.json'  


def save_books():  
    with open(BOOKS_FILE, 'w') as file:  
        json.dump([book.__dict__ for book in Books], file)  

def load_books():  
    if os.path.exists(BOOKS_FILE):  
        with open(BOOKS_FILE, 'r') as file:  
            books_data = json.load(file)  
            return [Book(**book) for book in books_data]  
    return []  

# Load existing books when the program starts  
Books = load_books()  

def center_text(text):
    print("\n"+text.center(80)+"\n")
    # print("\n"+" "*10+text.center(80)+" "*10+"\n")

def add_new_book():
    center_text("\n📚 ================================== Adding New Book ================================== 📚")
   
    book_title: str = input("📖 Please enter a book title: ")
    book_author: str = input("✍️  Please enter a book author: ")
    book_publication_year: str = input("📅 Please enter a book publication year: ")
    book_genre: str = input("📂 Please enter a book genre: ")
    # read_status:str = input('Have you read the Book? Type Yes or No:')
    i=2
    while i>1:
     if i<5:
      i+=1
      read_status:str = input('📘 Have you read the Book? Type Yes or No: ')
    #   if read_status == 'yes' or read_status == 'Yes':
      if read_status.lower() == 'yes':
        read_status = True
        break
    #   elif read_status == 'no' or read_status == 'No':
      elif read_status.lower() == 'no':
        read_status = False
      else:
        print("⚠️  Invalid input. You have Two more chances to tell the read_status.")
     else:
        print("❌ You have exceeded the number of attempts. Setting read_status to False by default.")
        read_status = False
        break    
    new_Book = Book(book_title, book_author,book_publication_year, book_genre, read_status)
    
    # list(Books)
    Books.append(new_Book)
    center_text(f"✅ Book '{book_title}' added successfully!")
    # Books.append(Book(book_title, book_author,book_publication_year, book_genre))
    # print(new_Book.title)
    # tuple(Books)
    save_books()  # Save the updated book list after adding  

{
# def print_books(book,index):
# # def print_books(books,index):
#   if index >= 0:
#     index+=1
    
#     print(f"Book: ",index)
#     # print(f"Book: ",index+1)
#     # print(f"Title: ",book['title'])
#     # print(f"Author: ",book['author'])
#     # print(f"Publication Year: ",book['publication_year'])
#     # print(f"Genre: ",book['genre'])
#     print(f"Title: ",book.title)
#     print(f"Author: ",book.author)
#     print(f"Publication Year: ",book.publication_year)
#     print(f"Genre: ",book.genre)
#     # # print(f"Title: {book.title}")
#     # print(f"Author: {book.author}")
#     # print(f"Publication Year: {book.publication_year}")
#     # print(f"Genre: {book.genre}")
}

def remove_books(bookTitle):
    for index,book in enumerate(Books):
        if bookTitle == book.title:
            Books.remove(book)
            center_text(f"\n ✅ Book '{bookTitle}' removed successfully! \n")
            save_books()  # Save the updated book list after removing
            return  

        elif index == len(Books) - 1:
            center_text(f'❌ Book "{bookTitle}" not found!')
            

def list_available_books():
#    print(type(Books[1]))
#    print(Books[0].title)
#    if Books!=[{}]:

  
   if Books!=[]:
    #    print(Books)
    #    for book in Books:
       center_text("📚 ================================== Available Books ================================== 📚")
    #    SECOND WAY
       {     
    #    header_format = f"{'Index':<6} | {'Title':<30} | {'Author':<20} | {'Year':<10} | {'Genre':<15} | {'Read Status':<15}"  
    #    print(header_format)       
    #    print("_" * 100)  
       }

       for index,book in enumerate(Books):
    #    for index,book in enumerate(Books):
        #    print_books(book,index)
        if index >= 0:
          index+=1
        #  SECOND WAY
          {
        #   wrapped_title = textwrap.fill(book.title, width=30)  
        #   wrapped_author = textwrap.fill(book.author, width=20)  
        #   # Format to align with vertical separators  
        #   print(f"{index:<6} | {wrapped_title:<30} | {wrapped_author:<20} | {book.publication_year:<10} | {book.genre:<15} | {book.read_status}")       
        #   print("_" * 100)
        #   print('\n')
          }

        #   FIRST WAY

          print(f"   📖  Book           : {index}")
          print(f"   📕 Title           : {book.title}")
          print(f"   ✍️  Author         : {book.author}")
          print(f"   📅 Publication Year: {book.publication_year}")
          print(f"   📂 Genre           : {book.genre}")
          print(f"   🧐 read_status     : {book.read_status}")
          print('\n')
        {          
    # print(f"Book: ",index+1)
    # print(f"Title: ",book['title'])
    # print(f"Author: ",book['author'])
    # print(f"Publication Year: ",book['publication_year'])
    # print(f"Genre: ",book['genre'])
        }          
        
    #    list(map(lambda x:print_books(x[1], x[0]),enumerate(Books)))


def search_for_book(book_to_find):
    center_text(f" 🔍 ================================== Searching for the Book: {book_to_find} ================================== 🔍 ")
    for index, book in enumerate(Books):
        if book_to_find == book.title:
            if index >= 0:
                index+=1
                center_text(f"\n🔍 Book Found!")
                print(f"   📖  Book           : {index}")
                print(f"   📕 Title           : {book.title}")
                print(f"   ✍️  Author         : {book.author}")
                print(f"   📅 Publication Year: {book.publication_year}")
                print(f"   📂 Genre           : {book.genre}")
                print(f"   🧐 read_status     : {book.read_status}")
        elif index == len(Books) - 1:
            center_text(f'❌ Book "{book_to_find}" not found!')

def show_statistics():
    total_books_read = 0

    # if Books == []:
    #     center_text("❌ No Books Added Yet")
    #     return
    for index,book in enumerate(Books):
        if book.read_status:
            print(f"✅ Book {index + 1} '{book.title}': You have read this book. 👌🤗🥰")

            total_books_read += 1
        else:
            print(f"❌ Book {index + 1} '{book.title}': You have not read this book yet. ☹😑😕")

    
    percentage_read = (total_books_read / len(Books)) * 100

    center_text(f"\n📊 Total Books: {len(Books)}")
    center_text(f"📘 Books Read: {total_books_read}")
    center_text(f"📈 You have read {percentage_read:.2f}% of your books.")

def show_menu():  
    center_text("📚 ================================== MAIN MENU ================================== 📚")
    print("1️⃣  Add a new book")
    print("2️⃣  Remove a Book")
    print("3️⃣  List available books")
    print("4️⃣  Search a book by title")
    print("5️⃣  Show statistics")
    print("6️⃣  Exit")
    choice: int = input("👉 Please enter the number of the operation you want to perform (1-6): ")
    return choice
    {
    # choice: int = int(input("Please enter number of the operation you want to perform like 1,2,3...: "))
    # if type(choice) == int:
    #  return choice  
    # else:
    #    print("Invalid choice! Please enter a number.")
    #    return None
    }


        
# # FIRST ATTEMPT - This approach was good but the exit functionality on choice 3 was not working the error was with the break statement!
{
# operation_perfomed = False
# i=2
# while i>1:
    
#     # MENU
#     def show_menu():

#      if i == 2:
#         print("Welcome to your personal Library Manager")
#      else:
#         print("Your Personal Library Manager")

#      print("1. Add a new book")
#      print("2. List available books")
#      print("3. Exit")
#      choice:int = int(input("Please enter your choice: "))

#      if choice == 1:
#             add_new_book()
#             print("Book added successfully!")
#             # print("1. Add a new book")
#             # print("2. List available books")
#             # choice:int = int(input("Please enter your choice: "))
#             choice = None
#             # operation_perfomed = True
    

#      elif choice == 2:
#             # operation_perfomed = True
#             if Books != []:
#             # if Books != [{}]:
#                 # print("Available books:" , Books)
#                 list_available_books()
#                 # print("1. Add a new book")
#                 # print("2. List available books")
#                 # choice:int = int(input("Please enter your choice: "))
#                 choice = None

            

#             else:
#                 print("No Books Added yet")
#                 # print("1. Add a new book")
#                 # print("2. List available books")
#                 # choice:int = int(input("Please enter your choice: "))
#                 choice = None

#      elif choice == 3:
#         print("Thank you for using Library Manager")
#         break       

#      else:
#             print("Invalid choice!")

#     if operation_perfomed==False:
#         # print(operation_perfomed)
#         show_menu()

}

# SECOND ATTEMPT

open_menu = ''
def home_page():
    # center_text("\n \n 📚 ================================== Welcome to Your Personal Library Manager ================================== 📚 \n \n")
    open_menu = input("👉 Type 'Yes' to open the menu: ")
    if open_menu.lower() == 'yes':
        return open_menu
    else:
        print("⚠️ " + " "+"Please type 'Yes' to open the menu.")
        return home_page()
j = 1
# while True: 
     
while j>0:  
    if j<2:
       center_text("\n 📚 ================================== Welcome to Your Personal Library Manager ================================== 📚 \n ")
       home_page()
       j +=1
       choice = show_menu()  # Get user input from the menu 
    elif j>=2:
       choice = show_menu() 

    # print("================================== Welcome to your personal Library Manager ==================================")

    # choice = show_menu()  # Get user input from the menu    
    if choice == "1":  
        add_new_book()  
    
    elif choice == "2":
    # elif choice == 2 and Books!=[]:
       if Books != []:

        bookTitle = input("📖 Enter the title of the book you want to remove: ")
        remove_books(bookTitle)
       else:
             center_text("❌ No books available in the library.")       
 

    elif choice == "3": 
         if Books != []:
            # if Books != [{}]:
                # print("Available books:" , Books)
                list_available_books() 
         else:
             center_text("❌ No books available in the library.")

    elif choice == "4":
       if Books != []:
        book_to_search=input("🔍 Enter the title of the book to search: ")
        search_for_book(book_to_search)
       else:
             center_text("❌ No books available in the library.")
    
    elif choice == "5":
       if Books != []:    
        show_statistics()
       else:
          center_text("❌ No Books Added Yet")

    elif choice == "6":  
        center_text("🙏 Thank you for using Library Manager! 📚")  
        break  # Break the loop to exit the program  

    else:  
        center_text("❌ Invalid choice!, Please type a number between 1 to 6")  

