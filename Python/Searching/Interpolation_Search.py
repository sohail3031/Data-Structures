"""
Interpolation Search:
    Interpolation search is an improved variant of binary search. This search algorithm works on the probing position of
    the required value. For this algorithm to work properly, the data collection should be in a sorted form and equally
    distributed. Binary search has a huge advantage of time complexity over linear search. Linear search has worst-case
    complexity of Ο(n) whereas binary search has Ο(log n). There are cases where the location of target data may be
    known in advance. For example, in case of a telephone directory, if we want to search the telephone number of
    Morpheus. Here, linear search and even binary search will seem slow as we can directly jump to memory space where
    the names start from 'M' are stored. The list should be in sorted order.

Note:
    The index position starts from 0.
"""

import sys


class InterpolationSearch:
    __data: list[int] = []

    @staticmethod
    def _display_options() -> None:
        """ Display available options """
        print("""
                ****************************
                    Interpolation Search

                        0. Exit
                        1. Add
                        2. Search
                        3. Display
                ****************************
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
        result: int = self.__interpolation_search(value=value, low=0, high=len(self.__data) - 1)

        if result != -1:
            print(f"The position of {value} is {result}!")
        else:
            print(f"No element with value: {value} found!")

    def __interpolation_search(self, value: int, low: int, high: int) -> int:
        """ Interpolation Search """
        if low <= high and self.__data[low] <= value <= self.__data[high]:
            position = low + ((high - low) // (self.__data[high] - self.__data[low])) * (value - self.__data[low])

            if self.__data[position] == value:
                return position
            elif self.__data[position] < value:
                return self.__interpolation_search(value=value, low=position + 1, high=high)
            else:
                return self.__interpolation_search(value=value, low=low, high=position - 1)

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
    InterpolationSearch().start()
    sys.exit(0)
