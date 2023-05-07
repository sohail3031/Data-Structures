"""
Linked List:

Brief Explanation:
    A linked list is a linked list with a pointer. The pointer contains the location of the next node.

Structure:
    ---------------------------     ---------------------------
    |    Data    |    Next    | ->  |    Data    |    Next    |
    ---------------------------     ---------------------------

    1. The data part contains the data to be stored.
    2. The next contains the pointer (i.e: the location to the next node).

Operations:
    0. Exit: Exit the program.
    1. Add At End: Node is added at the end of the list.
    2. Add At Beginning: Node is added at the beginning of the list.
    3. Add At Position: Node is added at the given index.
    4. Display: Display the entire list.
    5. Count: Return the occurrence of a given number.
    6. Delete: Delete node.
"""


class Node:
    """ Node """

    def __init__(self, data):
        """ Constructor """
        self.data = data
        self.next = None


class SingleLinkedList:
    """ Single Linked """

    def __init__(self):
        """ Constructor """
        self.head = None

    @staticmethod
    def __display_options() -> None:
        """ Display's the available options """
        print("""
            **************************
                Single Linked List
                
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
        current: (int, str) = self.head

        if self.head is None:
            self.head = Node(value)
        else:
            while current.next:
                current = current.next
            current.next = Node(value)

        print(f"Value: {value} is added at the end!")

    def __add_at_beginning(self) -> None:
        """ Add node at the beginning """
        value: int = int(input("Enter a number: "))
        temp = Node(value)
        initial_node = self.head
        self.head = temp
        self.head.next = initial_node

        print(f"Value: {value} is added at the beginning!")

    def __add_after(self) -> None:
        """ Add node at the given position """
        value: int = int(input("Enter a number: "))
        position: int = int(input("Enter position: ")) - 1

        if position == 0:
            temp = Node(value)
            previous_node = self.head
            self.head = temp
            self.head.next = previous_node

            print(f"Value: {value} is added at the position: {position}!")
        elif position < self.__count_length():
            temp = Node(value)
            previous_node, next_node = self.__get_details_by_position(position=position)
            previous_node.next = temp
            temp.next = next_node

            print(f"Value: {value} is added at the position: {position}!")
        else:
            print("Invalid index position!")

    def __count_element(self):
        """ Count the number of occurrences of a number """
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

    def __delete_node(self):
        """ Delete node """
        value: int = int(input("Enter a number: "))
        count: int = 0
        temp = self.head

        while temp:
            if temp.data == value:
                count += 1
            temp = temp.next

        if count >= 1:
            current_node = self.head
            previous_node = None

            if current_node.data == value:
                self.head = current_node.next
            else:
                while current_node:
                    if current_node.data == value:
                        break
                    previous_node = current_node
                    current_node = current_node.next

                if current_node is None:
                    return
                previous_node.next = current_node.next

            print(f"Node with value: {value} is deleted!")
        else:
            print(f"No element with the value: {value} is found!")

    def __get_details_by_position(self, position) -> list:
        """ Return's the neighbouring nodes of a given node """
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

        return [previous_node, next_node]

    def __count_length(self) -> int:
        """ Return the length of the list """
        count: int = 0
        temp: (None, Node) = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    def __display_data(self):
        """ Display list """
        temp: (None, Node) = self.head
        data: list[int] = []

        if temp:
            while temp:
                data.append(temp.data)
                temp = temp.next

            print("Single Linked List: ", end="")
            print(*data, sep=" -> ")
        else:
            print("No data to display!")

    def start(self):
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
                print("Invalid input!")


if __name__ == '__main__':
    SingleLinkedList().start()
