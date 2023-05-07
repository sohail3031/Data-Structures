"""
Bubble Sort:
    In bubble sort, to sort n elements, we need n-1 iterations. In every iteration, the element is compared with its
    neighbouring element. If the current element is bigger than its neighbour, then we swap them else move on to next
    comparison.
"""

import sys


class BubbleSort:
    """ Bubble Sort """
    __data: list[int] = []

    @staticmethod
    def _display_options() -> None:
        """ Display the display options """
        print("""
        Bubble Sort
            0. Exit
            1. Add
            2. Sort
            3. Display
        """)

    def __add_element(self) -> None:
        """ Adds the element into the list """
        try:
            value: int = int(input("Enter a number: "))
            self.__data.append(value)
            print(f"Value {value} is added!")
        except ValueError:
            print("Invalid input format. Number is required.")

    def __sort_data(self) -> None:
        """ Sort list """
        flag: bool

        for i in range(len(self.__data) - 1):
            flag = False

            for j in range(len(self.__data) - 1 - i):
                if self.__data[j] > self.__data[j + 1]:
                    temp: int = self.__data[j]
                    self.__data[j] = self.__data[j + 1]
                    self.__data[j + 1] = temp
                    flag = True

            if not flag:
                break

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
                        if self.__data:
                            self.__sort_data()
                            print("Data sorted!")
                        else:
                            print("No elements to sort!")
                    case 3:
                        if self.__data:
                            print(*self.__data, sep=", ")
                        else:
                            print("No elements to sort!")
                    case _:
                        print("Invalid Option")
            except ValueError:
                print("Invalid input format. Number is required.")


if __name__ == '__main__':
    BubbleSort().start()
    sys.exit(0)
