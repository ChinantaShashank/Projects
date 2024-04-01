import datetime
import os

class LMS:
    
    def __init__(self, list_of_books, library_name):
        self.list_of_books = "List_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        Id = 101
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({str(Id):{"books_title":line.replace("\n", ""),
                                              "lender_name": "", "Issue_date": '',
                                              'Status': "Available"}})
            Id += 1

        self.users = {}  # Dictionary to store user information
        self.transactions = {}  # Dictionary to store transaction information

    def display_books(self):
        print("_____________________________________________________")
        print("Books ID", "\t", "Title", "\t", "User ID", "\t", "Issue Date", "\t", "Status")
        print("_____________________________________________________")
        for key, value in self.books_dict.items():
            book_id = key
            book_title = value.get("books_title")
            user_id = ""
            issue_date = ""
            status = value.get('Status')

            for bk_id, users in self.transactions.items():
                if book_id == bk_id and users:
                    user_id = users[0]
                    issue_date = self.books_dict[book_id]['Issue_date']
                    break

            print(book_id, "\t", book_title, "\t", user_id, "\t", issue_date, "\t", status)


    def issue_books(self):
        books_id = input("Enter book ID: ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")  # Fixed: Corrected strftime format
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]['Status'] == "Available":
                if len(self.transactions.get(books_id, [])) < 3:  # Check if user has already issued 3 books
                    user_id = input("Enter user ID: ")
                    if user_id not in self.users:
                        print("User not found. Please register first.")
                        return
                    self.books_dict[books_id]['lender_name'] = self.users[user_id]['name']
                    self.books_dict[books_id]['Issue_date'] = current_date
                    self.books_dict[books_id]['Status'] = "Issued"
                    self.transactions.setdefault(books_id, []).append(user_id)
                    print("Book issued successfully!")
                else:
                    print("You have already issued 3 books.")
            else:
                print("This book is already issued.")
        else:
            print("Book ID not found.")

    def add_books(self):
        new_books = input("Enter book title: ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 25:
            print("Book title is too long!!! Title length should be 25 chars")
            return self.add_books()
        else:
            with open(self.list_of_books, "a") as bk:
                bk.writelines(f"{new_books}\n")
            Id = str(int(max(self.books_dict)) + 1)  # Updated to get the maximum key from self.books_dict
            self.books_dict[Id] = {'books_title': new_books, 'lender_name': "", 'Issue_date': "",
                                   'Status': "Available"}  # Updated the dictionary update
            print(f"This book '{new_books}' has been added successfully !!!")

    def return_books(self):
        books_id = input("Enter book ID: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Issued":
                user_id = self.transactions.get(books_id, [])[0]
                self.books_dict[books_id]['lender_name'] = ""
                self.books_dict[books_id]['Issue_date'] = ""
                self.books_dict[books_id]['Status'] = "Available"
                self.transactions[books_id].pop(0)
                print("Book returned successfully!")
            else:
                print("This book is not issued.")
        else:
            print("Book ID is not found.")

    def register_user(self):
        user_name = input("Enter user name: ")
        user_id = input("Enter user ID: ")
        if user_id not in self.users:
            self.users[user_id] = {'name': user_name}
            print("User registered successfully!")
        else:
            print("User ID already exists. Please choose a different one.")

    def overdue_books(self, user_id):
        total_fine = 0
        print("Overdue Books:")
        for books_id, users in self.transactions.items():
            if user_id in users:
                due_date = datetime.datetime.strptime(self.books_dict[books_id]['Issue_date'], "%Y-%m-%d") + datetime.timedelta(days=14)
                if datetime.datetime.now() > due_date:
                    days_overdue = (datetime.datetime.now() - due_date).days
                    fine = days_overdue * 1
                    total_fine += fine
                    print(f"Book ID: {books_id}, Due Date: {due_date.strftime('%Y-%m-%d')}, "
                          f"Days Overdue: {days_overdue}, Fine: ${fine}")
        print(f"Total Fine: ${total_fine}")

try:
    myLMS = LMS("List_of_books.txt", "Python's")
    press_key_list = {"D": "Display Books", "I": "Issue Books", "A": "Add Books",
                      "R": "Return Books", "U": "User Registration", "O": "Overdue Books", "Q": "Quit"}
    key_press = False
    while key_press != "q":
        print(f"\n----------------------Welcome TO {myLMS.library_name} Library management System----------------\n")
        for key, value in press_key_list.items():
            print(f"Press {key} To {value}")
        key_press = input("Press key: ").lower()
        if key_press == "i":
            print("\nCurrent Selection : Issue Books\n")
            myLMS.issue_books()
        elif key_press == "a":
            print("\nCurrent Selection : ADD Books\n")
            myLMS.add_books()
        elif key_press == "d":
            print("\nCurrent Selection : Display Books\n")
            myLMS.display_books()
        elif key_press == "r":
            print("\nCurrent Selection : Return Books\n")
            myLMS.return_books()
        elif key_press == "u":
            print("\nCurrent Selection : User Registration\n")
            myLMS.register_user()
        elif key_press == "o":
            print("\nCurrent Selection : Overdue Books\n")
            user_id = input("Enter user ID: ")
            myLMS.overdue_books(user_id)
        elif key_press == "q":
            break
        else:
            continue
except Exception as e:
    print("Something went wrong. Please check your input!!!")