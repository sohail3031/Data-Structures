"""
Ternary Search:
    Ternary search is a searching technique which is used to search whether a number is present in the lost or not. For
    ternary search, it is important that the list should be sorted. It is similar to binary search but the only
    difference is instead of dividing the list into two, it divides into three.

Working:
    In the initial iteration, the value is compared with the middle 1 of the list. If the value is equal to the middle
    1, then the search will stop and the index of middle 1 is returned. Else if the value is less than the middle 2
    value, the search will stop and the index of middle 2 is returned. If the value is less than the middle 1, then the
    search will continue only in the first part of the list (i.e: from index 0 to index middle 1 minus 1). If this is
    not the case than the value is checked if it is greater than middle 2. If it is than the search will continue in the
    third part of the list (i.e: from index middle 2 plus 1 to index length of list). Finally, if all the above
    conditions are false, it wil check for the value in the middle part of the list (i.e: from index middle 1 plus 1 to
    index middle 2 minus 1). This process will repeat itself until the value is found or there is no values left to
    traverse.

Note:
    The index position starts from 0.
"""

import sys


class TernarySearch:
    __data: list[int] = []

    @staticmethod
    def _display_options() -> None:
        """ Display available options """
        print("""
            ***********************
                Ternary Search

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
        result: int = self.__ternary_search(value=value, low=0, high=len(self.__data) - 1)

        if result != -1:
            print(f"The position of {value} is {result}!")
        else:
            print(f"No element with value: {value} found!")

    def __ternary_search(self, value: int, low: int, high: int) -> int:
        """ Ternary Search """
        while low <= high:
            mid_1: int = low + (high - low) // 3
            mid_2: int = high - (high - low) // 3

            if value == self.__data[mid_1]:
                return mid_1
            if value == self.__data[mid_2]:
                return mid_2
            if value < self.__data[mid_1]:
                high = mid_1 - 1
            elif value > self.__data[mid_2]:
                low = mid_2 + 1
            else:
                low = mid_1 + 1
                high = mid_2 - 1

        return -1

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
                        print("Invalid Option")
            except ValueError:
                print("Invalid input!")


if __name__ == '__main__':
    TernarySearch().start()
    sys.exit(0)
