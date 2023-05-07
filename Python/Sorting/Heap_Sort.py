"""
Heap Sort:
    In heap sort, the deletion always happens at the root. By deleting all the nodes present in the tree, we will get
    the sorted data.
"""

import sys


class Node:
    """ Node """

    def __init__(self, data: int):
        self.left: (None, Node) = None
        self.data: int = data
        self.right: (None, Node) = None


class HeapMax:
    """ Max Heap """

    def __init__(self):
        self.root: (None, Node) = None
        self.heap_data: list[int] = []
        self.sorted_data: list[int] = []

    @staticmethod
    def _display_option() -> None:
        """ Display the options """
        print("""
            *****************
                Max Heap

                0. Exit
                1. Insert
                2. Delete
            *****************
        """)

    def _check_heap_conditions(self) -> None:
        """ Check if the heap is satisfying all the conditions or not """
        for i in range(len(self.heap_data) - 1, -1, -1):
            parent_index = self._get_parent_position(position=i + 1) - 1

            if parent_index >= 0 and i >= 0:
                if self.heap_data[parent_index] < self.heap_data[i]:
                    self.heap_data[parent_index], self.heap_data[i] = self.heap_data[i], self.heap_data[parent_index]

        print("Heap Data: ", end="")
        print(*self.heap_data, sep=" -> ")

    def _delete_heap_node(self) -> None:
        """ Delete root of the heap """
        if len(self.heap_data) > 1:
            first: int = self.heap_data[0]
            self.sorted_data.insert(0, first)
            self.heap_data[0] = self.heap_data.pop(-1)
            self._check_heap_conditions()

            print(f"{first} is deleted!")
        elif len(self.heap_data) == 1:
            first: int = self.heap_data[0]
            self.sorted_data.insert(0, first)
            self.heap_data.pop(0)
            self._check_heap_conditions()

            print(f"{first} is deleted!")

    def _sort(self) -> None:
        """ Sort the deleted data """
        for i in range(len(self.sorted_data) - 1):
            if self.sorted_data[i] > self.sorted_data[i + 1]:
                self.sorted_data[i], self.sorted_data[i + 1] = self.sorted_data[i + 1], self.sorted_data[i]

    @staticmethod
    def _get_parent_position(position) -> int:
        """ Returns the position of the parent element """
        return position // 2

    def start(self) -> None:
        """ Main method """
        while True:
            self._display_option()

            try:
                match int(input("Select your option: ")):
                    case 0:
                        break
                    case 1:
                        try:
                            value: int = int(input("Enter a number: "))

                            self.heap_data.append(value)

                            print(f"Value: {value} is inserted in heap")

                            self._check_heap_conditions()
                        except ValueError:
                            print("Invalid input. Number is required!")
                    case 2:
                        if self.heap_data:
                            self._delete_heap_node()
                            self._sort()

                            print("Sorted Data: ", end="")
                            print(*self.sorted_data, sep=" -> ")
                        else:
                            print("Heap is empty")
            except ValueError:
                print("Invalid option!")


if __name__ == '__main__':
    HeapMax().start()
    sys.exit()
