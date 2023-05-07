"""
Insertion Sort:
    In insertion sort, current value is compared with all its previous values. If the current value is less than the
    previous values, current is swapped with the comparing value and all other values from compared to current nodes
    will be shifted by one towards right.
"""

import sys


class InsertionSort:
    """ Insertion Sort """
    __data: list[int] = []

    @staticmethod
    def _display_options() -> None:
        """ Display the display options """
        print("""
            **********************
                Insertion Sort
                
                    0. Exit
                    1. Add
                    2. Sort
                    3. Display
            **********************
        """)

    def __add_element(self) -> None:
        """ Adds the element into the list """
        value: int = int(input("Enter a number: "))
        self.__data.append(value)
        print(f"Value {value} is added!")

    def __sort_data(self) -> None:
        """ Sort list """
        for i in range(1, len(self.__data)):
            j: int = i - 1
            temp: int = self.__data[i]

            while (j > -1) and (self.__data[j] > temp):
                self.__data[j + 1] = self.__data[j]
                j -= 1

            self.__data[j + 1] = temp

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
    InsertionSort().start()
    sys.exit(0)
