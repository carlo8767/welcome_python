import re

from error import *
from main_code.actionLibrary import Action_Library, DisplayBook, Borrow_Book, Return_Book, View_Book, Exit_Book


class ServiceActionLibrary(Action_Library):

    def selection_menu(self):

        boolean_selection = True
        while boolean_selection:
            try:
                print(self.get_welcome_library())
                self.to_string_menu()
                print(self.get_select_an_option())
                selection = input()
                # VERIFY ERROR , OR .5
                pattern_string = re.compile('[a-z,A-Z]')
                check_string = pattern_string.findall(selection)
                if check_string:
                    raise WrongSelectionOptionMenu
                elif int(selection) > 5 or int(selection) < 1:
                    raise WrongSelectionOptionMenu
                else:
                    # EXTRACT TYPE OF ACTION
                    value_action = self.list_action().get(int(selection))
                    boolean_selection = False
            except WrongSelectionOptionMenu as e:
                print(e.message)
        return value_action

    def start(self):
        # CREATION MENU
        boolean_menu = True

        while boolean_menu:
            # CALL SELECTION MENU
            evaluation = self.selection_menu()
            self.print_action(evaluation)
            # SET ACTION STRATEGY AND COMPARE WITH USER SELECTOIN
            if evaluation == self.get_option_display_book():
                self.set_action_strategy(DisplayBook)
            elif evaluation == self.get_option_borrow_book():
                self.set_action_strategy(Borrow_Book)
            elif evaluation == self.get_option_return_book():
                self.set_action_strategy(Return_Book)
            elif evaluation == self.get_option_view_your_book():
                self.set_action_strategy(View_Book)
            elif evaluation == self.get_option_exit():
                self.set_action_strategy(Exit_Book)
                boolean_menu = False
            self.execute_action_strategy()

    def set_action_strategy(self, actions_library: Action_Library) -> Action_Library:
        self.actions_library = actions_library(self.get_book_id(), self.get_book_name(), self.get_availability())

    def execute_action_strategy(self):
        return self.actions_library.type_action()


if __name__ == "__main__":
    test = ServiceActionLibrary("", "", "")
    test.start()
