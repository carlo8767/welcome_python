class AnyBookBorrow(Exception):

    def __init__(self, message="Any user has borrow a book!\n"):
        self.message = message
        super().__init__(self.message)



class BookAlreadyBorrow(Exception):

    def __init__(self, message="This book is already borrow\n"):
        self.message = message
        super().__init__(self.message)


class BookABorrowSameUser(Exception):

    def __init__(self, message="The book is already borrow by you!!!\n"):
        self.message = message
        super().__init__(self.message)


class LibraryEmpty(Exception):

    def __init__(self, message="Library is empty please insert a new book\n"):
        self.message = message
        super().__init__(self.message)


class NoTitleBook(Exception):

    def __init__(self, message="Title not present\n"):
        self.message = message
        super().__init__(self.message)


class WrongSelectionOptionMenu(Exception):

    def __init__(self, message="Please select a number between 1 to 5\n"):
        self.message = message
        super().__init__(self.message)


class WrongSelectionYesNo(Exception):

    def __init__(self, message="Please write Yes or No\n"):
        self.message = message
        super().__init__(self.message)


class WrongSelectionAvailability(Exception):

    def __init__(self, message="f'Please write Free or Not Available\n"):
        self.message = message
        super().__init__(self.message)



