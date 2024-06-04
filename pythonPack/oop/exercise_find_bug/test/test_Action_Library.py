import string
import uuid
from unittest import TestCase
from main_code.book import Book
from main_code.actionLibrary import Return_Book, Borrow_Book, View_Book, DisplayBook
from main_code.error import LibraryEmpty, NoTitleBook, BookAlreadyBorrow, BookABorrowSameUser, AnyBookBorrow


class TestReturn_Book(TestCase):
    verify = Return_Book("", "", "")

    def test_return_book(self):
        # FAKE DICTIONARY VERIFY THAT A USER CAN RETURN A BOOK

        books_mock = Book("", "", "")
        books_mock.set_book_name("FakeTitle")
        books_mock.set_availability("not available")
        books_mock.set_book_id("1")
        books_mock.set_username("Carlo")

        other_dictionary = {str(uuid.uuid4()): books_mock}

        second_books_mock = Book("", "", "")
        second_books_mock.set_book_name("FakeTitleSecond")
        second_books_mock.set_availability("not available")
        second_books_mock.set_book_id("1")
        second_books_mock.set_username("Pippo")

        other_dictionary[str(uuid.uuid4())] = second_books_mock

        dictionary_fake = {"F": other_dictionary}
        self.verify.set_dictionary_books(dictionary_fake)
        self.verify.set_verification_book_present(True)
        self.verify.type_action()
        self.assertEqual(books_mock.get_availability(), "free")
        self.assertEqual(books_mock.get_username(), "AdminBookUser")

    def test_no_title_present(self):
        # FAKE DICTIONARY VERIFY THAT A USER CAN RETURN A BOOK
        books_mock = Book("", "", "")
        books_mock.set_book_name("FakeTitle")
        books_mock.set_availability("not available")
        books_mock.set_book_id("1")
        books_mock.set_username("Carlo")

        other_dictionary = {str(uuid.uuid4()): books_mock}

        second_books_mock = Book("", "", "")
        second_books_mock.set_book_name("FakeTitleSecond")
        second_books_mock.set_availability("not available")
        second_books_mock.set_book_id("1")
        second_books_mock.set_username("Pippo")

        other_dictionary[str(uuid.uuid4())] = second_books_mock

        dictionary_fake = {"F": other_dictionary}
        dictionary_fake["N"] = ""
        self.verify.set_dictionary_books(dictionary_fake)
        self.verify.set_verification_book_present(True)
        self.verify.type_action()
        self.assertEqual(self.verify._title_not_present, True)
        self.assertRaises(NoTitleBook)

    def test_library_empty(self):
        # FAKE DICTIONARY VERIFY THAT A USER CAN RETURN A BOOK
        books_mock = Book("", "", "")
        books_mock.set_book_name("FakeTitle")
        books_mock.set_availability("not available")
        books_mock.set_book_id("1")
        books_mock.set_username("Carlo")

        other_dictionary = {str(uuid.uuid4()): books_mock}

        second_books_mock = Book("", "", "")
        second_books_mock.set_book_name("FakeTitleSecond")
        second_books_mock.set_availability("not available")
        second_books_mock.set_book_id("1")
        second_books_mock.set_username("Pippo")

        other_dictionary[str(uuid.uuid4())] = second_books_mock

        dictionary_fake = {"F": other_dictionary}
        dictionary_fake["N"] = ""
        self.verify.set_dictionary_books(dictionary_fake)
        self.verify.set_verification_book_present(False)
        self.verify.type_action()
        self.assertRaises(LibraryEmpty)


class TestBorrowBook(TestCase):
    verify = Borrow_Book("", "", "")

    def test_borrow_book_Library_Empty(self):
        # FAKE DICTIONARY VERIFY THAT A USER CAN RETURN A BOOK
        books_mock = Book("", "", "")
        books_mock.set_book_name("FakeTitle")
        books_mock.set_availability("not available")
        books_mock.set_book_id("1")

        other_dictionary = {str(uuid.uuid4()): books_mock}

        second_books_mock = Book("", "", "")
        second_books_mock.set_book_name("FakeTitleSecond")
        second_books_mock.set_availability("not available")
        second_books_mock.set_book_id("2")

        other_dictionary[str(uuid.uuid4())] = second_books_mock

        dictionary_fake = {"F": other_dictionary}
        self.verify.set_dictionary_books(dictionary_fake)
        self.verify.set_verification_book_present(False)
        self.verify.type_action()
        self.assertRaises(LibraryEmpty)

    def test_borrow_book_Title_No_Present(self):

        dictionary_fake = {}

        if len(dictionary_fake) < 1:
            for item in string.ascii_uppercase:
                dictionary_fake[item] = ""

        # FAKE DICTIONARY VERIFY THAT A USER CAN RETURN A BOOK
        books_mock = Book("", "", "")
        books_mock.set_book_name("FakeTitle")
        books_mock.set_availability("not available")
        books_mock.set_book_id("1")
        first_name = books_mock.get_book_name()

        other_dictionary = {str(uuid.uuid4()): books_mock}

        dictionary_fake[first_name[0]] = other_dictionary

        second_books_mock = Book("", "", "")
        second_books_mock.set_book_name("FakeTitleSecond")
        second_books_mock.set_availability("not available")
        second_books_mock.set_book_id("2")

        other_dictionary[str(uuid.uuid4())] = second_books_mock
        name = second_books_mock.get_book_name()

        dictionary_fake = {name[0]: other_dictionary}
        self.verify.set_dictionary_books(dictionary_fake)
        self.verify.set_verification_book_present(True)
        self.verify.type_action()
        self.assertRaises(NoTitleBook)

    def test_borrow_book_already_borrow_(self):

        dictionary_fake = {}

        if len(dictionary_fake) < 1:
            for item in string.ascii_uppercase:
                dictionary_fake[item] = ""

        # FAKE DICTIONARY VERIFY THAT A USER CAN RETURN A BOOK
        books_mock = Book("", "", "")
        books_mock.set_book_name("FakeTitle")
        books_mock.set_availability("not available")
        books_mock.set_book_id("1")
        books_mock.set_username("pippo")
        first_name = books_mock.get_book_name()

        other_dictionary = {str(uuid.uuid4()): books_mock}

        dictionary_fake[first_name[0]] = other_dictionary

        second_books_mock = Book("", "", "")
        second_books_mock.set_book_name("FakeTitleSecond")
        second_books_mock.set_availability("not available")
        second_books_mock.set_book_id("2")
        second_books_mock.set_username("pippo")
        other_dictionary[str(uuid.uuid4())] = second_books_mock
        name = second_books_mock.get_book_name()
        dictionary_fake = {name[0]: other_dictionary}
        self.verify.set_dictionary_books(dictionary_fake)
        self.verify.set_verification_book_present(True)
        self.verify.type_action()
        self.assertRaises(BookAlreadyBorrow)

    def test_borrow_book_same_user(self):

        dictionary_fake = {}

        if len(dictionary_fake) < 1:
            for item in string.ascii_uppercase:
                dictionary_fake[item] = ""

        # FAKE DICTIONARY VERIFY THAT A USER CAN RETURN A BOOK
        books_mock = Book("", "", "")
        books_mock.set_book_name("FakeTitle")
        books_mock.set_availability("not available")
        books_mock.set_book_id("1")
        books_mock.set_username("pippo")
        first_name = books_mock.get_book_name()

        other_dictionary = {str(uuid.uuid4()): books_mock}

        dictionary_fake[first_name[0]] = other_dictionary

        second_books_mock = Book("", "", "")
        second_books_mock.set_book_name("FakeTitleSecond")
        second_books_mock.set_availability("not available")
        second_books_mock.set_book_id("2")
        second_books_mock.set_username("pippo")
        other_dictionary[str(uuid.uuid4())] = second_books_mock
        name = second_books_mock.get_book_name()
        dictionary_fake = {name[0]: other_dictionary}
        self.verify.set_dictionary_books(dictionary_fake)
        self.verify.set_verification_book_present(True)
        self.verify.type_action()
        self.assertRaises(BookABorrowSameUser)

    def test_borrow_book_verify_borrow_a_book(self):

        dictionary_fake = {}
        if len(dictionary_fake) < 1:
            for item in string.ascii_uppercase:
                dictionary_fake[item] = ""

        # FAKE DICTIONARY VERIFY THAT A USER CAN RETURN A BOOK
        books_mock = Book("", "", "")
        books_mock.set_book_name("FakeTitle")
        books_mock.set_availability("free")
        books_mock.set_book_id("1")
        first_name = books_mock.get_book_name()

        other_dictionary = {str(uuid.uuid4()): books_mock}

        dictionary_fake[first_name[0]] = other_dictionary

        second_books_mock = Book("", "", "")
        second_books_mock.set_book_name("FakeTitleSecond")
        second_books_mock.set_availability("not available")
        second_books_mock.set_book_id("2")

        other_dictionary[str(uuid.uuid4())] = second_books_mock
        name = second_books_mock.get_book_name()

        dictionary_fake = {name[0]: other_dictionary}

        self.verify.set_dictionary_books(dictionary_fake)
        self.verify.set_verification_book_present(True)
        # CARLO
        self.verify.type_action()
        self.assertEqual(books_mock.get_availability(), "not available")
        self.assertEqual(books_mock.get_username(), "pippo")
        self.assertEqual(self.verify.get_current_user(), "pippo")


class TestView_Book(TestCase):
    verify = View_Book("", "", "")

    def test_view_book_Library_Empty(self):
        # FAKE DICTIONARY VERIFY THAT A USER CAN RETURN A BOOK
        books_mock = Book("", "", "")
        books_mock.set_book_name("FakeTitle")
        books_mock.set_availability("not available")
        books_mock.set_book_id("1")

        other_dictionary = {str(uuid.uuid4()): books_mock}

        second_books_mock = Book("", "", "")
        second_books_mock.set_book_name("FakeTitleSecond")
        second_books_mock.set_availability("not available")
        second_books_mock.set_book_id("2")

        other_dictionary[str(uuid.uuid4())] = second_books_mock

        dictionary_fake = {"F": other_dictionary}
        self.verify.set_dictionary_books(dictionary_fake)
        self.verify.set_verification_book_present(False)
        self.verify.type_action()
        self.assertRaises(LibraryEmpty)

    def test_view_book_anyBookBorrow(self):

        dictionary_fake = {}

        if len(dictionary_fake) < 1:
            for item in string.ascii_uppercase:
                dictionary_fake[item] = ""

        # FAKE DICTIONARY VERIFY THAT A USER CAN RETURN A BOOK
        books_mock = Book("", "", "")
        books_mock.set_book_name("FakeTitle")
        books_mock.set_availability("free")
        books_mock.set_book_id("1")
        name_other = books_mock.get_book_name()
        other_dictionary = {str(uuid.uuid4()): books_mock}

        dictionary_fake[name_other[0]] = other_dictionary

        second_books_mock = Book("", "", "")
        second_books_mock.set_book_name("FakeTitleSecond")
        second_books_mock.set_availability("free")
        second_books_mock.set_book_id("2")
        name = second_books_mock.get_book_name()

        other_dictionary[str(uuid.uuid4())] = second_books_mock

        dictionary_fake[name[0]] = other_dictionary
        self.verify.set_dictionary_books(dictionary_fake)
        self.verify.set_verification_book_present(True)
        self.verify.type_action()
        self.assertRaises(AnyBookBorrow)

    def test_view_book_w(self):

        dictionary_fake = {}

        if len(dictionary_fake) < 1:
            for item in string.ascii_uppercase:
                dictionary_fake[item] = ""

        # FAKE DICTIONARY VERIFY THAT A USER CAN RETURN A BOOK
        books_mock = Book("", "", "")
        books_mock.set_book_name("FakeTitle")
        books_mock.set_availability("free")
        books_mock.set_book_id("1")
        books_mock.set_username("pippo")
        name_other = books_mock.get_book_name()
        other_dictionary = {str(uuid.uuid4()): books_mock}

        dictionary_fake[name_other[0]] = other_dictionary

        second_books_mock = Book("", "", "")
        second_books_mock.set_book_name("FakeTitleSecond")
        second_books_mock.set_availability("free")
        second_books_mock.set_book_id("2")
        second_books_mock.set_username("pippo")
        name = second_books_mock.get_book_name()

        other_dictionary[str(uuid.uuid4())] = second_books_mock

        dictionary_fake[name[0]] = other_dictionary
        self.verify.set_dictionary_books(dictionary_fake)
        self.verify.set_current_user("pippo")
        self.verify.set_verification_book_present(True)
        self.verify.type_action()


class TestDisplayBook(TestCase):
    display_book = DisplayBook("", "", "")

    def test_multiple_book(self):

        main_dictionary = {}

        for item in string.ascii_uppercase:
            main_dictionary[item] = ""

        books_mock = Book("", "", "")
        books_mock.set_book_name("FakeTitle")
        books_mock.set_availability("available")
        books_mock.set_book_id("1")

        other_dictionary = {str(uuid.uuid4()): books_mock}
        books_name = books_mock.get_book_name()
        main_dictionary[books_name[0].upper()] = other_dictionary.copy()

        second_books_mock = Book("", "", "")
        second_books_mock.set_book_name("FakeTitleSecond")
        second_books_mock.set_availability("available")
        second_books_mock.set_book_id("2")

        books_name = second_books_mock.get_book_name()
        other_dictionary[str(uuid.uuid4())] = second_books_mock
        main_dictionary[books_name[0].upper()] = other_dictionary.copy()

        third_books_mock = Book("", "", "")
        third_books_mock.set_book_name("FakeTitleSecond")
        third_books_mock.set_availability("available")
        third_books_mock.set_book_id("3")

        books_name = third_books_mock.get_book_name()
        other_dictionary[str(uuid.uuid4())] = third_books_mock
        main_dictionary[books_name[0].upper()] = other_dictionary.copy()

        self.display_book.set_dictionary_books(main_dictionary)
        self.display_book.set_verification_book_present(True)
        self.display_book.type_action()


