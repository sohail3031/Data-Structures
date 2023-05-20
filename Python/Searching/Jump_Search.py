"""
"Jump" Search:
    Unlike other searching algorithms, jump search uses the square root of the length of the array to search for the
    element.

Working:
    In the initial iteration, it checks for the index position of square root of the length of the array. It the element
    is found, the search will stop and the index position is returned. Else, it will add the square root of the length
    of the array again to the previous square root and the search will continue. The search will continue until the
    element if found, or it reaches to an end. There might be a situation where the element is present in between two
    jumps. In this case, the linear search is preformed between the two intervals.

Note:
    The index position starts from 0.
"""

import math
import sys


class JumpSearch:
    __data: list[int] = []

    @staticmethod
    def _display_options() -> None:
        """ Display available options """
        print("""
                ***********************
                    Jump Search

                        0. Exit
                        1. Add
                        2. Search
                        3. Display
                ***********************
            """)

    def __add_element(self) -> None:
        """ Add element in the list """
        value: int = int(input("Enter a number: "))
        self.__data.append(value)
        print(f"Value {value} is added!")

    def __sort_data(self) -> None:
        """ Sort the list """
        for i in range(len(self.__data)):
            for j in range(i + 1, len(self.__data)):
                if self.__data[i] > self.__data[j]:
                    self.__data[i], self.__data[j] = self.__data[j], self.__data[i]

    def __search_element(self) -> None:
        """ Search the element in the list """
        self.__sort_data()

        value: int = int(input("Enter a number: "))
        result: int = self.__jump_search(value=value)

        if result != -1:
            print(f"The position of {value} is {result}!")
        else:
            print(f"No element with value: {value} found!")

    def __jump_search(self, value: int) -> int:
        """ "Jump" Search """
        low: int = 0
        high: int = len(self.__data) - 1
        step: int = int(math.sqrt(high))

        while self.__data[step] <= value and step <= high:
            low = step
            step += int(math.sqrt(high))

            if step > high:
                return -1

        for i in range(low, step):
            if self.__data[i] == value:
                return i

        return -1

    def start(self) -> None:
        """ Main method """
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
                        print("Invalid Option")
            except ValueError:
                print("Invalid input!")


if __name__ == '__main__':
    JumpSearch().start()
    sys.exit(0)
