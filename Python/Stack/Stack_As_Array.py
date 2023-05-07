"""
Stack:
    Stack is a data structure, in which the element which we inserted first will be the last one to be deleted. It
    follows LIFO (Last In First Out) terminology.

Implementation:
    This program uses array to store the elements of stack.

Operations:
    0. Exit: Exit the program.
    1. Push: Push element into the stack.
    2. Pop: Remove the top element from the stack.
    3. Display: Display all the elements present in the stack.

Structure:

    Deletion ->     |    Top    |   <- Insertion
                    |-----------|
                    |   Data    |
                    |-----------|
                    |   Data    |
                    |-----------|
                    |   Data    |
                    |-----------|
"""

import sys


class Stack:
    """ Stack """
    __stack: list[object] = []

    @staticmethod
    def __display_options() -> None:
        """ Display the display options """
        print("""
            *****************
                Stack
                
                0. Exit
                1. Push
                2. Pop
                3. Display
            *****************
        """)

    def _display_stack(self) -> None:
        """ Display elements in the form of stack """
        for i in range(len(self.__stack) - 1, -1, -1):
            print(f"|    {self.__stack[i]}    ", " " * (len(str(max(self.__stack))) - len(str(self.__stack[i]))), "|")
            print("-" * (12 + len(str(max(self.__stack)))))

    def start(self) -> None:
        """ Main method """
        while True:
            self.__display_options()

            match int(input("Select your option: ")):
                case 0:
                    break
                case 1:
                    value: object = input("Enter a value: ")
                    self.__stack.append(value)
                case 2:
                    if self.__stack:
                        self.__stack.pop(len(self.__stack) - 1)
                    else:
                        print("The stack is empty")
                case 3:
                    if self.__stack:
                        self._display_stack()
                        # print(*self.__stack, sep=" ")
                    else:
                        print("The stack is empty")
                case _:
                    print("Invalid option")


if __name__ == '__main__':
    Stack().start()
    sys.exit(0)
