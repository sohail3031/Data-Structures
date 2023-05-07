"""
Selection Sort:
    In selection sort, in every iteration, the first element is compared with all the remaining elements in the list. If
    the first element is greater than the element we are comparing with, than we swap them else compare next element.
"""

import sys


class SelectionSort:
    """ Selection Sort """
    __data: list[int] = []

    @staticmethod
    def _display_options() -> None:
        """ Display the display options """
        print("""
            **************************
                Selection Sort
                
                    0. Exit
                    1. Add
                    2. Sort
                    3. Display
            **************************
        """)

    def __add_element(self) -> None:
        """ Adds the element into the list """
        value: int = int(input("Enter a number: "))
        self.__data.append(value)
        print(f"Value {value} is added!")

    def __sort_data(self) -> None:
        """ Sort list """
        flag: bool

        for i in range(len(self.__data)):
            flag = False

            for j in range(i, len(self.__data)):
                if self.__data[i] > self.__data[j]:
                    temp: int = self.__data[i]
                    self.__data[i] = self.__data[j]
                    self.__data[j] = temp
                    flag = True

            if not flag:
                break

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
    SelectionSort().start()
    sys.exit(0)
