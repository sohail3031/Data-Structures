"""
Circular Linked List:

Brief Explanation:
    A circular linked list is a linked list where the last node points to the first node. If the linked list contains a
    single node then the node points to itself.

Structure:

    -------------------------------------------------------------------------
    |                                                                       |
    |       ---------------------------     ---------------------------     |
     --->   |    Data    |    Next    | ->  |    Data    |    Next    | ----
            ---------------------------     ---------------------------

    1. The data part contains the data to be stored.
    2. The next contains the pointer (i.e: the location to the next node). If the list contains a single node then the
        next points to itself. If the node is the last node in the list, then it points to the first node in the list.
        If the node is present in the middle, then it points to its next node.

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
        self.data = data
        self.next = None


class CircularLinkedList:
    """ Circular LinkedList """

    def __init__(self):
        """ Constructor """
        self.head = None
        self.tail = None

    @staticmethod
    def __display_options() -> None:
        """ Display's the selectable options """
        print("""
                ****************************
                    Circular Linked List
                    
                    0. Exit
                    1. Add At End
                    2. Add At Beginning
                    3. Add At Position
                    4. Display
                    5. Count
                    6. Delete
                ****************************
            """)

    def __add_at_end(self) -> None:
        """ Add node at the end """
        value: int = int(input("Enter a number: "))

        if self.head is None:
            self.head = Node(value)
            self.head.next = self.head
        else:
            if self.tail is None:
                self.tail = Node(value)
                self.head.next = self.tail
                self.tail.next = self.head
            else:
                current_node = Node(value)
                self.tail.next = current_node
                current_node.next = self.head
                self.tail = current_node

        print(f"Value: {value} is added at the end!")

    def __add_at_beginning(self) -> None:
        """ Add node at the beginning """
        value: int = int(input("Enter a number: "))
        temp = Node(value)
        current_node = self.head
        self.head = temp
        self.head.next = current_node
        self.tail.next = self.head

        print(f"Value: {value} is added at the beginning!")

    def __add_after(self) -> None:
        """ Add node at the given position """
        value: int = int(input("Enter a number: "))
        position: int = int(input("Enter position: ")) - 1

        if position == 0:
            temp: Node = Node(value)
            current_node = self.head
            self.head = temp
            self.head.next = current_node
            self.tail.next = self.head

            print(f"Value: {value} is added at the position: {position}!")
        elif position < self.__list_length():
            temp: Node = Node(value)
            previous_node, next_node, count = self.__get_details_by_position(position=position)
            previous_node.next = temp
            temp.next = next_node

            if count == self.__list_length():
                self.tail = next_node
                self.tail.next = self.head

            print(f"Value: {value} is added at the position: {position}!")
        else:
            print("Invalid index position!")

    def __count_element(self):
        """ Count the number occurrence of a given number """
        value: int = int(input("Enter a number: "))
        temp: (None, Node) = self.head
        count: int = 0

        while temp:
            if temp.data == value:
                count += 1

            temp = temp.next

            if temp == self.head:
                break

        if count == 0:
            print(f"No element with value: {value} found!")
        else:
            print(f"The value: {value} occurs {count} times!")

    def __delete_node(self):
        """ Delete a node """
        value: int = int(input("Enter a number: "))
        count: int = 0
        temp: (None, Node) = self.head

        while temp:
            if temp.data.__eq__(value):
                count += 1

            temp = temp.next

            if temp == self.head:
                break

        if count >= 1:
            if self.head.data == value:
                self.__delete_first()
            elif self.tail.data == value:
                self.__delete_last()
            else:
                self.__delete_middle(value=value)

            print(f"Node with value: {value} is deleted!")
        else:
            print(f"No element with the value: {value} is found!")

    def __delete_first(self) -> None:
        """ Delete the initial node """
        temp: (None, Node) = self.head.next
        self.head.next = temp.next
        self.head = temp
        self.tail.next = self.head

    def __delete_last(self) -> None:
        """ Delete the last node """
        temp: (None, Node) = self.head

        for _ in range(self.__list_length() - 2):
            temp = temp.next

        self.tail = temp
        temp.next = self.head

    def __delete_middle(self, value: object) -> None:
        """ Delete the middle node """
        value_index: int = 0
        temp: (None, Node) = self.head
        previous_node: (None, Node) = None
        next_node: (None, Node) = None

        while temp:
            if temp.data == value:
                break

            temp = temp.next
            value_index += 1

        temp = self.head

        for i in range(self.__list_length()):
            if i == (value_index - 1):
                previous_node = temp
            if i == (value_index + 1):
                next_node = temp

            temp = temp.next

        previous_node.next = next_node

    def __get_details_by_position(self, position) -> list:
        """ Return's the previous and the next node of a given node """
        previous_node: (None, Node) = None
        next_node: (None, Node) = None
        temp: (None, Node) = self.head
        count: int = 0

        while temp:
            if count == (position - 1):
                previous_node = temp
            if count == position:
                next_node = temp

            temp = temp.next
            count += 1

            if temp == self.head:
                break

        return [previous_node, next_node, count]

    def __list_length(self) -> int:
        """ Return's the length of the circular linked list """
        count: int = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

            if temp == self.head:
                break

        return count

    def __display_data(self) -> None:
        """ Display the circular linked list """
        temp = self.head
        data: list[int] = []

        if temp:
            while temp:
                data.append(temp.data)
                temp = temp.next

                if temp == self.head:
                    break
            print("Circular Linked List: ", end="")
            print(*data, sep=" -> ")
        else:
            print(f"No data to display!")

    def start(self) -> None:
        """ Main method """
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
                        self.__add_after()
                    case 4:
                        self.__display_data()
                    case 5:
                        self.__count_element()
                    case 6:
                        self.__delete_node()
                    case _:
                        print("Invalid option!")
            except ValueError:
                print("Invalid option!")


if __name__ == '__main__':
    CircularLinkedList().start()
    sys.exit(0)
