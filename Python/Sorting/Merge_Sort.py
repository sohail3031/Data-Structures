"""
Merge Sort:
    In merge sort, more than one sorted lists are combined into one single one.
"""

import sys


class MergeSort:
    """ Merge Sort """
    _merge_list_1: list[int] = []
    _merge_list_2: list[int] = []
    _merge_list_3: list[int] = []

    @staticmethod
    def _display_options() -> None:
        print("""
            ******************
                Merge Sort
                
                0. Exit
                1. Insert In List 1
                2. Insert In List 2
                3. Sort
            ******************
        """)

    def _sort_list_1(self) -> None:
        """ Sort first list using bubble sort """
        flag: bool = False

        for i in range(len(self._merge_list_1)):
            for j in range(len(self._merge_list_1) - 1 - i):
                if self._merge_list_1[j] > self._merge_list_1[j + 1]:
                    self._merge_list_1[j], self._merge_list_1[j + 1] = self._merge_list_1[j + 1], self._merge_list_1[j]
                    flag = True

            if not flag:
                break

    def _sort_list_2(self) -> None:
        """ Sort second list using bubble sort """
        flag: bool = False

        for i in range(len(self._merge_list_2)):
            for j in range(len(self._merge_list_2) - 1 - i):
                if self._merge_list_2[j] > self._merge_list_2[j + 1]:
                    self._merge_list_2[j], self._merge_list_2[j + 1] = self._merge_list_2[j + 1], self._merge_list_2[j]
                    flag = True

            if not flag:
                break

    def _sort(self) -> None:
        """ Perform merge sort """
        length_1: int = len(self._merge_list_1)
        length_2: int = len(self._merge_list_2)
        index_1 = index_2 = 0

        while (index_1 < length_1) and (index_2 < length_2):
            if self._merge_list_1[index_1] < self._merge_list_2[index_2]:
                self._merge_list_3.append(self._merge_list_1[index_1])
                index_1 += 1
            else:
                self._merge_list_3.append(self._merge_list_2[index_2])
                index_2 += 1

        for i in range(index_1, length_1):
            self._merge_list_3.append(self._merge_list_1[i])
        for i in range(index_2, length_2):
            self._merge_list_3.append(self._merge_list_2[i])

    def start(self) -> None:
        """ Main function """
        while True:
            self._display_options()

            try:
                match int(input("Select your option: ")):
                    case 0:
                        break
                    case 1:
                        value: int = int(input("Enter a number: "))
                        self._merge_list_1.append(value)
                        print(f"Value: {value} is added!")
                    case 2:
                        value: int = int(input("Enter a number: "))
                        self._merge_list_2.append(value)
                        print(f"Value: {value} is added!")
                    case 3:
                        if self._merge_list_1 or self._merge_list_2:
                            self._sort_list_1()
                            self._sort_list_2()
                            self._sort()
                            print("Sorted Data: ")
                            print(*self._merge_list_3, sep=" -> ")
                        else:
                            print("Lists are empty!")
            except ValueError:
                print("Invalid input!")


if __name__ == '__main__':
    MergeSort().start()
    sys.exit(0)
