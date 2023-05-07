"""
Dequeue:

Brief Explanation:
    Queue is a data structure where the first inserted element will be removed first. Insertion is done at the back and
    deletion is done at the back.

Implementation:
    Dequeue is implemented using linked list.

Structure:
                  ----------------------------------------
    Deletion   -> |    Data    |    Data    |    Data    | <- Insertion
    Front         ----------------------------------------    Rear

Operations:
    0. Exit: Exit the program.
    1. Add: Data is added at the end of the list.
    2. Delete: Data is deleted at the beginning.
    3. Display: Display the entire list.
"""

import sys


class Node:
    """ Node """

    def __init__(self, data: int):
        """ Constructor """
        self.data: int = data
        self.next: (None, Node) = None


class Queue:
    """ Queue """

    def __init__(self):
        """ Constructor """
        self.head: (None, Node) = None
        self.tail: (None, Node) = None

    @staticmethod
    def __display_options() -> None:
        """ Display's available options """
        print("""
                ****************************
                    Queue as Linked List
                    
                    0. Exit
                    1. Push
                    2. Pop
                    3. Display
                ****************************
                """)

    def __append(self) -> None:
        """ Add node at the end """
        current_node: Node = Node(int(input("Enter a number: ")))

        if self.head is None:
            self.head = self.tail = current_node
        else:
            self.tail.next = current_node
            self.tail = current_node

        print(f"Value {current_node.data} is added to queue!")

    def __delete(self) -> None:
        """ Delete node """
        if self.head:
            print(f"Value {self.head.data} has been removed from queue!")

            current_node = self.head.next
            self.head.next = None
            self.head = current_node
        else:
            print("Queue is empty!")

    def __display(self) -> None:
        """ Display the queue """
        if self.head:
            current_node: (None, Node) = self.head
            data: str = ""

            while current_node:
                data += f"{current_node.data} "
                current_node = current_node.next

            print(*data.strip(), sep=" -> ")
        else:
            print("Queue is empty!")

    def start(self) -> None:
        """ Main method """
        while True:
            self.__display_options()

            try:
                match int(input("Select your option: ")):
                    case 0:
                        break
                    case 1:
                        self.__append()
                    case 2:
                        self.__delete()
                    case 3:
                        self.__display()
                    case _:
                        print("Invalid option!")
            except ValueError:
                print("Invalid input!")


if __name__ == '__main__':
    Queue().start()
    sys.exit(0)
