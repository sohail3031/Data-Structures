"""
Quick Sort:
    In this sorting algorithm, a pivot element is selected and along with it, low and high are used. The pivot element
    acts as an element to be compared and low and high are the initial and final index positions in the list. Initially,
    low is compared with high and if it's greater than high, then swap happens else move low moves to next element.
    Similarly, high is compared with low and if it's lesser than low, then we swap values else moves to the next
    element. This process will continue until high crosses low. After that, the list is divided into two and the same is
    repeated. In this step, we will get the data in the sorted order.
"""

import sys


class QuickSort:
    """ Quick Sort """
    __data: list[int] = []

    @staticmethod
    def _display_options() -> None:
        """ Display the display options """
        print("""
            **********************
                Quick Sort
                
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

    def __sort_data(self, low: int, high: int) -> None:
        """ Sort list """

        if low < high:
            j = self.__partition(low=low, high=high)
            self.__sort_data(low=low, high=j - 1)
            self.__sort_data(low=j + 1, high=high)

    def __partition(self, low: int, high: int) -> int:
        """ Sort the partition list """
        pivot = self.__data[high]
        i: int = low - 1

        for j in range(low, high):
            if self.__data[j] <= pivot:
                i += 1

                self.__data[i], self.__data[j] = self.__data[j], self.__data[i]

        self.__data[i + 1], self.__data[high] = self.__data[high], self.__data[i + 1]

        return i + 1

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
                            self.__sort_data(low=0, high=len(self.__data) - 1)
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
    QuickSort().start()
    sys.exit(0)
