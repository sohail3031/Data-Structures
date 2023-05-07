"""
Linear Search:
    Liner search is the simplest searching technique which is used to search whether a number is present in the lost or
    not. For linear search, it is not important to sort the list.

Working:
    The list is traversed in the linear (i.e: sequential) fashion until the key is found or the list come to an end.
"""

import sys


class LinearSearch:
    """ Linear Search """
    __data: list[int] = []

    @staticmethod
    def _display_options() -> None:
        """ Display the display options """
        print("""
            *********************
                Linear Search
                
                0. Exit
                1. Add
                2. Search
                3. Display
            *********************
        """)

    def __add_element(self) -> None:
        """ Adds the element into the list """
        value: int = int(input("Enter a number: "))
        self.__data.append(value)

        print(f"Value: {value} is added!")

    def __search_element(self) -> None:
        """ Search the element in the list """
        value: int = int(input("Enter a number: "))
        element_index: int = -1

        for i in range(len(self.__data)):
            if self.__data[i] == value:
                element_index = i
                break

        if element_index > -1:
            print(f"The position of {value} is {element_index}!")
        else:
            print(f"No element with value: {value} found!")

    def start(self) -> None:
        """ Main function """
        while True:
            self._display_options()

            try:
                match int(input("Enter your option: ")):
                    case 0:
                        break
                    case 1:
                        self.__add_element()
                    case 2:
                        self.__search_element()
                    case 3:
                        print(*self.__data, sep=", ")
                    case _:
                        print("Invalid Option!")
            except ValueError:
                print("Invalid input!")


if __name__ == '__main__':
    LinearSearch().start()
    sys.exit(0)
