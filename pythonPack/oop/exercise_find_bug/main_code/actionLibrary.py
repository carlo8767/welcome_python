import string
import uuid
from error import *
from book import Book


class Action_Library(Book):
    # GLOBAL VARIABLE IN ALL  IN CHILD CLASS
    _dictionary_book = {}
    _dictionary_book_availability = {}
    _input_available_book = "free"
    _input_not_available_book = "not available"
    _book_available = "***THESE ARE THE BOOKS AVAILABLE***:"
    _verification_book_present = False
    _current_user = ""

    # USE IN DISPLAY BOOK
    _input_ask_insert_value = ">>>Do you want insert any new book ? Please answer Yes or No"
    _input_book_id = ">>> insert book id"
    _input_book_name = ">>> insert the book name"
    _input_insert_book_availability = ">>> please, insert if the book is Free or Not Available"
    _input_yes = "yes"
    _input_no = "no"

    # USE IN BORROW CLASS
    _insert_username = ">>> please, insert your username"
    _input_name_book = ">>> please, insert the title of book you would like borrow"
    _no_find_book = True

    # USE IN RETURN CLASS
    _input_return_book = ">>> Insert the title of the book you want give back"
    _title_not_present = ">>> Book not present"

    # USE IN EXIT CLASS
    _final_message = "Thank for use our tool. See you next time !!!!"

    def __init__(self, book_id, book_name, book_availability):
        super().__init__(book_id, book_name, book_availability)
        self.current_user = None

    def type_action(self):
        pass

    def set_dictionary_books(self, dictionary_books: dict) -> dict:
        self._dictionary_book = dictionary_books

    def get_dictionary_books(self):
        return self._dictionary_book

    def set_dictionary_book_availability(self, dictionary_book_availability: dict) -> dict:
        self._dictionary_book_availability = dictionary_book_availability

    def get_dictionary_book_availability(self):
        return self._dictionary_book_availability

    def set_verification_book_present(self, verification_book_present: bool) -> bool:
        self._verification_book_present = verification_book_present

    def get_verification_book_present(self) -> bool:
        return self._verification_book_present

    def set_current_user(self, current_user):
        self._current_user = current_user

    def get_current_user(self):
        return self._current_user

    def clean_dictionary(self, dictionary_library: dict) -> dict:
        list_index_remove = []
        # SAVE  THE WRONG POSITION
        for external in dictionary_library:
            save_check_letter = external
            internal_dictionary = dictionary_library[external]
            for internal_books in internal_dictionary:
                key_internal = internal_books
                books_object = internal_dictionary[internal_books]
                verify_letter = books_object.get_book_name().upper()
                if verify_letter[0] != save_check_letter:
                    list_index_remove.append(f'{external},{key_internal}')
        # REMOVE WRONG POSITION
        if len(list_index_remove) > 0:
            for list_remove in list_index_remove:
                split_list_remove = list(list_remove.split(","))
                for index, item in enumerate(split_list_remove):
                    first_index = split_list_remove[index]
                    second_index = split_list_remove[index + 1]
                    del (dictionary_library[first_index][second_index])
                    break


class DisplayBook(Action_Library):

    def type_action(self):
        boolean_control = True
        # Create a Dictionary contains alphabetical Letter
        if len(self._dictionary_book) < 1:
            for item in string.ascii_uppercase:
                self._dictionary_book[item] = ""
        while boolean_control:
            try:
                input_ask_insert_value = input(f'{self._input_ask_insert_value}\n')
                # VERIFY THAT THE INPUT IS CONTAINS ONLY YES OR NO
                if input_ask_insert_value.lower() == self._input_yes:
                    # ADD BOOK A THE LIBRARY
                    book_object = Book("", "", "")
                    input_book_id = input(f'{self._input_book_id}\n')
                    book_object.set_book_id(str(input_book_id))
                    input_book_name = input(f'{self._input_book_name}\n')
                    book_object.set_book_name(input_book_name)
                    # ASK AVAILABILITY BOOK AND VERIFY ANSWER
                    status_availability = True
                    while status_availability:
                        input_book_availability = input(f'{self._input_insert_book_availability}\n')
                        try:

                            if input_book_availability.lower() == self._input_available_book \
                                    or input_book_availability.lower() == self._input_not_available_book:
                                book_object.set_availability(input_book_availability.lower())
                                # SAVE THE BOOK OBJECT IN ANOTHER DICTIONARY TO SORT BY  ALPHABETICAL ORDER
                                self._dictionary_book_availability[str(uuid.uuid4())] = book_object
                                self._dictionary_book[
                                    input_book_name[0].upper()] = self._dictionary_book_availability.copy()
                                self.set_dictionary_books(self._dictionary_book)
                                self.set_verification_book_present(True)
                                status_availability = False
                            else:
                                #  WRONG INPUT AVAILABILITY
                                raise WrongSelectionAvailability
                        except WrongSelectionAvailability as e:
                            print(e)

                elif input_ask_insert_value.lower() == self._input_no:
                    try:
                        # verify if dictionary have item
                        if self.get_verification_book_present():
                            # REMOVE /
                            self.clean_dictionary(self._dictionary_book)
                            # LIST BOOK BY ONLY THE LETTER ADD ERROR MESSAGE IF DICTIONARY IS EMPTY
                            # SHOW LIST OF BOOK
                            print(f'{self._book_available}')
                            for key in self._dictionary_book:
                                object_book = self._dictionary_book[key]
                                if len(object_book) > 0:
                                    for books_key in object_book:
                                        books_objects = self._dictionary_book[key][books_key]
                                        books_objects.to_string_books()
                                    boolean_control = False
                        else:
                            boolean_control = False
                            raise LibraryEmpty
                    except LibraryEmpty as p:
                        print(p)

                else:
                    #  WRONG INPUT YES NOT
                    raise WrongSelectionYesNo

            except WrongSelectionYesNo as e:
                print(e)


class Borrow_Book(Action_Library):

    def type_action(self):
        try:
            if self.get_verification_book_present():
                # ASK CURRENT USER
                current_user_active = input(f'{self._insert_username}\n')
                title_book_to_search = input(f'{self._input_name_book}\n')
                search_key_book = title_book_to_search[0].upper()
                # VERIFY EXIST ANY INPUT
                for list_books in self._dictionary_book[search_key_book]:
                    title_book_object = self._dictionary_book[search_key_book][list_books]
                    if title_book_object.get_book_name() == title_book_to_search:
                        self._no_find_book = False
                        if title_book_object.get_availability() == self._input_available_book:
                            # CHANGE AVAILABILITY IN THE DICTIONARY NOT AVAILABLE AND SET FROM THE USER
                            self._dictionary_book[search_key_book][list_books].set_availability(
                                self._input_not_available_book)
                            self.set_current_user(current_user_active)
                            self._dictionary_book[search_key_book][list_books].set_username(current_user_active)
                        elif title_book_object.get_availability() == self._input_not_available_book:
                            # CHECK IF IS BORROW BY THE USER
                            verify_username = title_book_object.get_username()
                            if verify_username == self.get_current_user():
                                raise BookABorrowSameUser
                            else:
                                raise BookAlreadyBorrow
                if self._no_find_book:
                    raise NoTitleBook

            else:
                # library is empty
                raise LibraryEmpty
        except BookAlreadyBorrow as e:
            print(e)
        except BookABorrowSameUser as e:
            print(e)
        except LibraryEmpty as e:
            print(e)
        except NoTitleBook as e:
            print(e)


class Return_Book(Action_Library):

    def type_action(self):
        current_dictionary = self.get_dictionary_books()
        self._title_not_present = True
        try:
            if self.get_verification_book_present():
                return_book_title = input(f'{self._input_return_book}\n')
                search_index = return_book_title[0].upper()
                # RETURN A BOOK
                for internal in current_dictionary[search_index]:
                    book_object = current_dictionary[search_index][internal]
                    if book_object.get_book_name() == return_book_title:
                        self._dictionary_book[search_index][internal].set_availability(self._input_available_book)
                        # CHANGE ADMIN USER
                        self._dictionary_book[search_index][internal].set_username(self.get_admin_username())
                        self._title_not_present = False
                        break
                # VERIFICATION IF IT IS FIND ANY BOOK
                if self._title_not_present:
                    raise NoTitleBook
            else:
                raise LibraryEmpty
        except LibraryEmpty as e:
            print(e)
        except NoTitleBook as e:
            print(e)


class View_Book(Action_Library):

    # VIEW CURRENT USER BOOK
    def type_action(self):
        view_book_user = self.get_dictionary_books()
        try:
            if self.get_verification_book_present():
                for books in view_book_user:
                    book_object = view_book_user[books]
                    for books_user in book_object:
                        user = self._dictionary_book[books][books_user].get_username()
                        current_user = self.get_current_user()
                        if user == current_user:
                            self._dictionary_book[books][books_user].to_string_books()
                        else:
                            raise AnyBookBorrow
            else:
                raise LibraryEmpty
        except AnyBookBorrow as e:
            print(e)
        except LibraryEmpty as e:
            print(e)


class Exit_Book(Action_Library):

    def type_action(self):
        print(self._final_message)
