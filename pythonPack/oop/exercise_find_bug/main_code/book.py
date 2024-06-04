import uuid


class Book:
    _book_id = ""
    _book_name = ""
    _book_availability = "free"
    _menu_library = "=====LIBRARY MANAGEMENT====="
    _option_display_book = "1. Display Available Books"
    _option_borrow_book = "2. Borrow a Book"
    _option_return_book = "3. Return a Book"
    _option_view_your_book = "4. View your Books"
    _welcome_library = "<<**WELCOME TO THE LIBRARY**>>"
    _select_an_option = ">> Please select an option"
    _option_exit = "5. Exit\n"
    _username = "AdminBookUser"
    _default_admin_username = "AdminBookUser"

    def __init__(self, book_id, book_name, book_availability):
        self._book_id = book_id
        self._book_name = book_name
        self._book_availability = book_availability
        self._username = "AdminBookUser"

    def set_book_id(self, book_id):
        self._book_id = book_id

    def get_book_id(self):
        return self._book_id

    def set_book_name(self, book_name):
        self._book_name = book_name

    def get_book_name(self):
        return self._book_name

    def set_availability(self, book_availability):
        self._book_availability = book_availability

    def get_availability(self):
        return self._book_availability

    def get_menu_library(self):
        return self._menu_library

    def get_option_display_book(self):
        return self._option_display_book

    def get_option_borrow_book(self):
        return self._option_borrow_book

    def get_option_return_book(self):
        return self._option_return_book

    def get_option_view_your_book(self):
        return self._option_view_your_book

    def get_option_exit(self):
        return self._option_exit

    def get_welcome_library(self):
        return self._welcome_library

    def get_select_an_option(self):
        return self._select_an_option

    def set_username(self, username):
        self._username = username

    def get_username(self):
        return self._username

    def get_admin_username(self):
        return self._default_admin_username

    def to_string_books(self):
        print(
            f'>>Id: {int(self.get_book_id())}\nTitle book: {self.get_book_name()}\nAvailability: {self.get_availability()}')

    def to_string_menu(self):
        print(f'{self.get_menu_library()}\n{self.get_option_display_book()}\n{self.get_option_borrow_book()}\n'
              f'{self.get_option_return_book()}\n{self.get_option_view_your_book()}\n{self.get_option_exit()}')

    def list_action(self):
        list_action = {1: self.get_option_display_book(), 2: self.get_option_borrow_book(),
                       3: self.get_option_return_book(), 4: self.get_option_view_your_book(), 5: self.get_option_exit()}
        return list_action

    def print_action(self, action):
        print(f'> You have selected >> {action.replace(".", "")}')
