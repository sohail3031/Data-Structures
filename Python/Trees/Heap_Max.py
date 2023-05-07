"""
Heap:
    Heap is a non-linear data structure similar to binary search tree. But, the main difference between the two is, in
    heap deletion always happens at the root. After the root is deleted, it will adjust the elements and the root is now
    replaced with maximum element from the children.

Max Heap:
    In max heap, every parent is greater than its child node.

Implementation:
    The below program implemented max heap using array.

Array Operation:
    Current Node: The node is present at the index "i".
    Left Child: The left child of the current node is present at index "2 * i".
    Right Child: The left child of the current node is present at index "2 * i + 1".
    Parent Node: The parent of the current node is present at the index "i // 2" (i.e: Consider only floor values).

Operations:
    0. Exit: Exit the program.
    1. Insert: Insert element in the heap array.
    2. Delete: Delete element from the heap array.
"""

import sys


class Node:
    """ Node Class """

    def __init__(self, data: int):
        self.left: (None, Node) = None
        self.data: int = data
        self.right: (None, Node) = None


class HeapMax:
    """ Max Heap Class """

    def __init__(self):
        self.root: (None, Node) = None
        self.heap_data: list[int] = []

    @staticmethod
    def _display_option() -> None:
        """ Display the options """
        print("""
            *****************
                Max Heap
                
                0. Exit
                1. Insert
                2. Delete
        """)

    def _check_heap_conditions(self) -> None:
        """ Check if the heap is satisfying all the conditions or not """
        for i in range(len(self.heap_data) - 1, 0, -1):
            if self.heap_data[self._get_parent_position(position=i + 1) - 1] < self.heap_data[i]:
                self.heap_data[self._get_parent_position(position=i + 1) - 1], self.heap_data[i] = \
                    self.heap_data[i], self.heap_data[self._get_parent_position(position=i + 1) - 1]

        print(*self.heap_data, sep=" -> ")

    def _delete_heap_node(self) -> None:
        """ Delete root of the heap """
        if len(self.heap_data) > 1:
            print(f"{self.heap_data[0]} is deleted!")

            self.heap_data[0] = self.heap_data.pop(-1)

            self._check_heap_conditions()
        elif len(self.heap_data) == 1:
            print(f"{self.heap_data[0]} is deleted!")

            self.heap_data.pop(0)
        else:
            print("Heap is empty")

    @staticmethod
    def _get_parent_position(position) -> int:
        """ Returns the position of the parent element """
        return position // 2

    def start(self) -> None:
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
                            self._check_heap_conditions()
                        except ValueError:
                            print("Invalid input. Number is required!")
                    case 2:
                        self._delete_heap_node()
            except ValueError:
                print("Invalid option!")


if __name__ == '__main__':
    HeapMax().start()
    sys.exit()
