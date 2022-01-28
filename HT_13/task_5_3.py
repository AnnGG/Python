class LibLoginSystem(object):

    def __init__(self, lib_users):
        self.lib_users = lib_users
        self.logged_in_user = None

    def login_or_exit(self, users_log):

        users_list = list(users_log)
        flag = 0
        for logpass in self.lib_users:
            if users_list[0]== logpass['login'] and users_list[1] == logpass['password'] and logpass['status'] == 'user':
                self.logged_in_user = users_list[0]
                print("Success!")
                student_menu()
            elif users_list[0] == logpass['login'] and users_list[1] == logpass['password'] and logpass['status'] == 'admin':
                self.logged_in_user = users_list[0]
                print("Success!")
                librarian_menu()
            else:
                flag = 1
        if flag == 1:
            print("Unsuccesful!")


class Library(object):

    def __init__(self, listofbooks):

        self.availablebooks = listofbooks

    def displayAvailablebooks(self):

        print("The books we have in our library are as follows:")
        print("================================")
        for book in self.availablebooks:
            print(book)

    def librarianAddBookToLib(self, book):

        list_book = list(book)
        book_d = {}
        if not self.availablebooks:
            self.availablebooks.append(list_book)
            print("The book was successfully added to the library!")
        elif len(self.availablebooks) > 0:
            flag = 0
            for books in self.availablebooks:
                if flag == 0:
                    if list_book[0] != books['title'] and list_book[1] != books['author'] and list_book[3] != books['year']:
                        flag = 0
                    else:
                        flag = 1
                if flag == 1:
                    if list_book[4] < 0:
                        print("You input negativ number!")
                    else:
                        books['number'] += book[4]
                        print('Success')
                else:
                    book_d['title'] = book[0]
                    book_d['author'] = book[1]
                    book_d['genre'] = book[2]
                    book_d['year_publ'] = book[3]
                    if book[4] < 0:
                        print("You input negativ number!")
                    else:
                        book_d['number'] = book[4]

        if len(book_d) > 0:
            self.availablebooks.append(book_d)
            print("The book was successfully added to the library!")

    def librarianDeleteBookFromLib(self, del_book):

        if not self.availablebooks:
            print("There are no books in the library!")
        else:
            flag = 0
            for books in self.availablebooks:
                if flag == 0:
                    if del_book[0] != books['title'] and del_book[1] != books['author'] and del_book[2] != \
                            books['year']:
                        flag = 0
                    else:
                        flag = 1
                if flag == 0:
                    print('Sorry the book you have delete is not in the library!')
                else:
                    if del_book[3] < 0:
                        print("You input negativ number!")
                    else:
                        books['number'] -= del_book[3]
                        print('Success')
                        if books['number'] == 0:
                            self.availablebooks.remove(books)
                            print('Success')


    def lendBook(self, student, requestedBook):

        flag = 0
        for books in self.availablebooks:
            if flag == 0:
                if requestedBook[0] != books['title'] and requestedBook[1] != books['author'] and requestedBook[2] != \
                        books['year']:
                    flag = 0
                else:
                    flag = 1
            if flag == 0:
                print('Sorry the book you have requested is currently not in the library!')
            else:
                number = None
                try:
                    number = int(input('Input number of the books: '))
                except ValueError:
                    print("You entered incomprehensible values!")
                    exit()
                if number < 0:
                    print("You input negativ number!")
                else:
                    books['number'] -= number
                    student.addBookOnBag([requestedBook[0], requestedBook[1], requestedBook[2], number])
                    if books['number'] == 0:
                        self.availablebooks.remove(books)


    def addBook(self, student, book):

        book_d = {}
        flag = 0
        for books in self.availablebooks:
            if flag == 0:
                if book[0] != books['title'] and book[1] != books['author'] and book[2] != books['year']:
                    flag = 0
                else:
                    flag = 1
            if flag == 1:
                if book[3] < 0:
                    print("You input negativ number!")
                else:
                    books['number'] += book[3]
                    print('Success')
            else:
                book_d['title'] = book[0]
                book_d['author'] = book[1]
                book_d['genre'] = input("Genre of book: ")
                book_d['year_publ'] = book[2]
                if book[3] < 0:
                    print("You input negativ number!")
                else:
                    book_d['number'] = book[3]

            student.delBookFromBag((book[0], book[1], book[2], book[3]))

        if len(book_d) > 0:
            self.availablebooks.append(book_d)
            print('Success')


class User(object):

    def __init__(self, name, adress, phone_number):

        self.name = name
        self.adress = adress
        self.phone = phone_number

    def authorization(self):

        login = input("Input your login: ")
        password = input("Input your password: ")
        return login, password


class Student(User):

    def __init__(self, name, adress, phone_number, grade):
        super().__init__(name, adress, phone_number)
        self.grade = grade
        self.student_bag = []

    def requestBook(self):

        print("Enter the name of the book you'd like to borrow")
        book = input()
        print("Enter the author of the book")
        name = input()
        print("Enter the year of publishing of the book")
        year_pub = input()
        if year_pub.isdigit():
            if 0 < int(year_pub) < 2023:
                return book, name, year_pub
            else:
                print("You entered an incorrect date!")
                exit()


    def addBookOnBag(self, book):

        list_book = list(book)
        if not self.student_bag:
            self.student_bag.append(list_book)
            print("The book you requested has now been borrowed")
        elif len(self.student_bag) > 0:
            for books in range(len(self.student_bag)):
                if list_book[:3] != self.student_bag[books][:3]:
                    self.student_bag.append(list(book))
                    print("The book you requested has now been borrowed")
                else:
                    print("You already have such a book!")

    def delBookFromBag(self, book):

        list_book = list(book)
        for books in range(len(self.student_bag)):
            if list_book[:3] == self.student_bag[books][:3]:
                if self.student_bag[books][3] - list_book[3] == 0:
                    self.student_bag.remove(list_book)
                else:
                    self.student_bag[books][3] = self.student_bag[books][3] - list_book[3]
            else:
                print("There is no such book in your bag!")
        if not self.student_bag:
            print("Now your bag is empty!")
        else:
            print('Now in your bag thees books')
            print(self.student_bag)

    def returnBook(self):
        number = None
        book = input("Enter the name of the book you'd like to return: ")
        name = input("Enter the author of the book: ")
        year_pub = input("Enter the year of publishing of the book: ")
        try:
            number = int(input('Input number of the books: '))
        except ValueError:
            print("You entered incomprehensible values!")
            exit()
        if year_pub.isdigit():
            if 0 < int(year_pub) < 2023:
                return book, name, year_pub, number
            else:
                print("You entered an incorrect date!")
                exit()


class Librarian(User):

    def __init__(self, name, adress, phone_number, position):
        super().__init__(name, adress, phone_number)
        self.position = position

    def addBookToLib(self):
        number = None
        title = input('Input title: ')
        author = input('Input author: ')
        ganre = input('Input ganre: ')
        year_book = input('Input year: ')
        try:
            number = int(input('Input number of the books: '))
        except ValueError:
            print("You entered incomprehensible values!")
            exit()
        if year_book.isdigit():
            if 0 < int(year_book) < 2023:
                return title, author, ganre, year_book, number
        else:
            print("You entered an incorrect date!")
            exit()

    def dellBookFromLib(self):
        number = None
        title = input('Input title: ')
        author = input('Input author: ')
        year_book = input('Input year: ')
        try:
            number = int(input('Input number of the books: '))
        except ValueError:
            print("You entered incomprehensible values!")
            exit()
        if year_book.isdigit():
            if 0 < int(year_book) < 2023:
                return title, author, year_book, number
        else:
            print("You entered an incorrect date!")
            exit()



lib_users = [{'login':'user1', 'password':'user1', 'status':'user'}, {'login':'user2', 'password':'user2', 'status':'admin'}]

liblog = LibLoginSystem(lib_users)
library = Library([{'title': '2666', 'author': 'Roberto Bolano', 'ganre': 'novel', 'year': '2003', 'number': 3}])
student = Student('student1', 'Kiev', '+380632541232', '7')
librarian = Librarian('librarian1', 'Kiev', '+380502541232', 'manager')



def librarian_menu():

    done = False
    while not done:
        print("======LIBRARY MENU=======")
        print(
            '1. Display all available books in Library\n'
            '2. Add a book in Library\n'
            '3. Delete a book in Library\n'
            '4. Exit\n '
        )
        choice = None
        try:
            choice = int(input("Enter Choice:"))
        except ValueError:
            print("You entered incomprehensible values!")
            exit()
        if choice == 1:
            library.displayAvailablebooks()
        elif choice == 2:
            library.librarianAddBookToLib(librarian.addBookToLib())
            library.displayAvailablebooks()
        elif choice == 3:
             library.librarianDeleteBookFromLib(librarian.dellBookFromLib())
             library.displayAvailablebooks()
        elif choice == 4:
            exit()


def student_menu():

    done = False
    while not done:
        print("======LIBRARY MENU=======")
        print(
            '1. Display all available books in Library\n'
            '2. Request a book in Library\n'
            '3. Return a book in Library\n'
            '4. Exit\n '
        )
        choice = None
        try:
            choice = int(input("Enter Choice:"))
        except ValueError:
            print("You entered incomprehensible values!")
            exit()
        if choice == 1:
            library.displayAvailablebooks()
        elif choice == 2:
            library.lendBook(student, student.requestBook())
            print('Now in your bag thees books')
            print(student.student_bag)
        elif choice == 3:
            library.addBook(student, student.returnBook())
        elif choice == 4:
            exit()


def main():

    done = False
    while not done:
        print("======Login MENU=======")
        print(
            '1. Login\n'
            '2. Exit\n'
        )
        unswer = input("Are you studen ? yes/no: ")
        choice = None
        if unswer.isdigit():
            print("You input number!")
            exit()
        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("You entered incomprehensible values!")
            exit()
        if choice == 1 and unswer == 'yes':
            liblog.login_or_exit(student.authorization())
        elif choice == 1 and unswer == 'no':
            liblog.login_or_exit(librarian.authorization())

        elif choice == 2:
            exit()
main()
