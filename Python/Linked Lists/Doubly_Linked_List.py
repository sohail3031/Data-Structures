"""
Doubly Linked List:

Brief Explanation:
    A doubly linked list is a linked list with two pointers. A previous pointer points to the previous node and a next
    pointer points to the next node in the list.

Structure:
    --------------------------------------------    --------------------------------------------
    |    Previous    |    Data    |    Next    | <-> |    Previous    |    Data    |    Next    |
    --------------------------------------------    --------------------------------------------

    1. The data part contains the data to be stored.
    2. The next contains the pointer (i.e: the location to the next node).
    3. The previous contains the pointer (i.e: the location to the previous node).

Operations:
    0. Exit: Exit the program.
    1. Add At End: Node is added at the end of the list.
    2. Add At Beginning: Node is added at the beginning of the list.
    3. Add At Position: Node is added at the given index.
    4. Display: Display the entire list.
    5. Count: Return the occurrence of a given number.
    6. Delete: Delete node.
"""

import sys


class Node:
    """ Node """

    def __init__(self, data):
        """ Constructor """
        self.previous = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    """ Doubly Linked List """

    def __init__(self):
        """ Constructor """
        self.head: (None, Node) = None
        self.tail: (None, Node) = None

    @staticmethod
    def __display_options() -> None:
        """ Display's the available option """
        print("""
                **************************
                    Doubly Linked List
                    
                    0. Exit
                    1. Add At End
                    2. Add At Beginning
                    3. Add At Position
                    4. Display
                    5. Count
                    6. Delete
                **************************
                """)

    def __add_at_end(self) -> None:
        """ Add node at the end """
        value: int = int(input("Enter a number: "))

        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            current_node: Node = Node(value)
            self.tail.next = current_node
            current_node.previous = self.tail
            self.tail = current_node

        print(f"Value: {value} is added at the end!")

    def __add_at_beginning(self) -> None:
        """ Add node at the beginning """
        value: int = int(input("Enter a number: "))
        temp: (None, Node) = self.head
        current_node: Node = Node(value)
        self.head = current_node
        self.head.next = temp
        temp.previous = self.head

        print(f"Value: {value} is added at the beginning!")

    def __add_at_position(self) -> None:
        """ Add node at the given position """
        value: int = int(input("Enter a number: "))
        position: int = int(input("Enter position: ")) - 1

        if position == 0:
            current_node: Node = Node(value)
            current_node.next = self.head
            self.head.previous = current_node
            self.head = current_node

            print(f"Value: {value} is added at the position: {position}!")
        elif 0 < position < self.__get_list_length():
            current_node: Node = Node(value)
            previous_node, next_node = self.__get_details_by_position(position=position)
            previous_node.next = current_node
            current_node.previous = previous_node
            current_node.next = next_node
            next_node.previous = current_node

            print(f"Value: {value} is added at the position: {position}!")
        elif position == self.__get_list_length():
            current_node: Node = Node(value)
            current_node.previous = self.tail
            self.tail.next = current_node
            self.tail = current_node

            print(f"Value: {value} is added at the position: {position}!")
        else:
            print("Invalid index position!")

    def __count_element(self) -> None:
        """ Count the occurrence of a given value """
        value: int = int(input("Enter a number: "))
        temp: (None, Node) = self.head
        count: int = 0

        while temp:
            if temp.data == value:
                count += 1

            temp = temp.next

        if count == 0:
            print(f"No element with value: {value} found!")
        else:
            print(f"The value: {value} occurs {count} times!")

    def __delete_node(self) -> None:
        """ Delete a node with the given value """
        value: int = int(input("Enter a number: "))
        temp: (None, Node) = self.head
        count: int = 0

        while temp:
            if temp.data == value:
                count += 1

            temp = temp.next

        if count >= 1:
            if self.head.data == value:
                self.head = self.head.next
            elif self.tail.data == value:
                current_node: (None, Node) = self.tail.previous
                current_node.next = None
                self.tail = current_node
            else:
                position: int = 0
                current_node: (None, Node) = self.head

                for _ in range(self.__get_list_length()):
                    if current_node.data == value:
                        break

                    current_node = current_node.next
                    position += 1

                previous_node, next_node = self.__get_details_by_position(position=position)
                next_node = next_node.next
                previous_node.next = next_node
                next_node.previous = previous_node

            print(f"Node with value: {value} is deleted!")
        else:
            print(f"No element with the value: {value} is found!")

    def __get_details_by_position(self, position: int) -> list[Node, Node]:
        """ Return's the neighbouring nodes of a given node """
        previous_node: (None, Node) = None
        next_node: (None, Node) = None
        current_node: Node = self.head

        for i in range(self.__get_list_length()):
            if i == (position - 1):
                previous_node = current_node
            if i == position:
                next_node = current_node

            current_node = current_node.next

        return [previous_node, next_node]

    def __get_list_length(self) -> int:
        """ Return's the list length """
        count: int = 0
        temp: (None, Node) = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    def __display_data(self) -> None:
        """ Display the node """
        temp: (None, Node) = self.head
        data: list[int] = []

        if temp:
            while temp:
                data.append(temp.data)

                temp = temp.next

            print("Doubly Linked List: ", end="")
            print(*data, sep=" <-> ")
        else:
            print("No data to display!")

    def start(self) -> None:
        while True:
            self.__display_options()

            try:
                match int(input("Select your option: ")):
                    case 0:
                        break
                    case 1:
                        self.__add_at_end()
                    case 2:
                        self.__add_at_beginning()
                    case 3:
                        self.__add_at_position()
                    case 4:
                        self.__display_data()
                    case 5:
                        self.__count_element()
                    case 6:
                        self.__delete_node()
                    case _:
                        print("Invalid option!")
            except ValueError:
                print("Invalid input!")


if __name__ == '__main__':
    DoublyLinkedList().start()
    sys.exit(0)
