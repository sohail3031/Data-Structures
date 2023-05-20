"""
Exponential Search:
    Exponential search is also known as doubling or galloping search. This mechanism is used to find the range where the
    search key may present. If L and U are the upper and lower bound of the list, then L and U both are the power of 2.
    For the last section, the U is the last position of the list. For that reason, it is known as exponential. After
    finding the specific range, it uses the binary search technique to find the exact location of the search key. The
    list should be in sorted order.

Note:
    The index position starts from 0.
"""

import sys


class ExponentialSearch:
    __data: list[int] = []

    @staticmethod
    def _display_options() -> None:
        """ Display available options """
        print("""
                **************************
                    Exponential Search

                        0. Exit
                        1. Add
                        2. Search
                        3. Display
                **************************
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
        result: int = self.__exponential_search(value=value)

        if result != -1:
            print(f"The position of {value} is {result}!")
        else:
            print(f"No element with value: {value} found!")

    def __exponential_search(self, value: int) -> int:
        """ Exponential Search """
        high: int = len(self.__data) - 1

        if self.__data[0] == value:
            return 0

        i: int = 1

        while i <= high and self.__data[i] <= value:
            i *= 2

        return self.__binary_search(low=i // 2, high=min(i, high), value=value)

    def __binary_search(self, low: int, high: int, value: int) -> int:
        """ Binary Search """
        if low <= high:
            middle: int = low + (high - low) // 2

            if self.__data[middle] == value:
                return middle

            if self.__data[middle] > value:
                return self.__binary_search(low=low, high=middle - 1, value=value)
            else:
                return self.__binary_search(low=middle + 1, high=high, value=value)

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
    ExponentialSearch().start()
    sys.exit(0)
