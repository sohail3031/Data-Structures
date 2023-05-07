"""
Binary Search:
    Binary search is a searching technique which is used to search whether a number is present in the lost or not. For
    binary search, it is important that the list should be sorted.

Working:
    In the initial iteration, the value is compared with the middle of the list. If the value is equal to the middle
    value, then the search will stop. Else is the value is less than the middle value, same process will repeat in the
    left, else if the value is greater than the middle than the search will continue in the right. This process will
    repeat itself until the value is found or there is no values left to traverse.
"""

import sys


class BinarySearch:
    """ Binary Search """
    __data: list[int] = []

    @staticmethod
    def _display_options() -> None:
        """ Display available options """
        print("""
            *********************
                Binary Search
                
                    0. Exit
                    1. Add
                    2. Search
                    3. Display
            *********************
        """)

    def __add_element(self) -> None:
        """ Add element in the list """
        value: int = int(input("Enter a number: "))
        self.__data.append(value)
        self.__sort_data()
        print(f"Value {value} is added!")

    def __sort_data(self) -> None:
        """ Sort the list """
        for i in range(len(self.__data)):
            for j in range(i + 1, len(self.__data)):
                if self.__data[i] > self.__data[j]:
                    temp: int = self.__data[i]
                    self.__data[i] = self.__data[j]
                    self.__data[j] = temp

    def __search_element(self) -> None:
        """ Search the element in the list """
        value: int = int(input("Enter a number: "))
        result: int = self.__binary_search(value=value)

        if result != -1:
            print(f"The position of {value} is {result + 1}!")
        else:
            print(f"No element with value: {value} found!")

    def __binary_search(self, value: int) -> int:
        """ Binary Search """
        low: int = 0
        high: int = len(self.__data)

        while low <= high:
            mid = (low + high) // 2

            if value == self.__data[mid]:
                return mid
            elif value < self.__data[mid]:
                high = mid - 1
            else:
                low = mid + 1

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
    BinarySearch().start()
    sys.exit(0)
