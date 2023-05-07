"""
Stack:
    Stack is a data structure, in which the element which we inserted first will be the last one to be deleted. It
    follows LIFO (Last In First Out) terminology.

Implementation:
    This program uses linked list to store the elements of stack.

Operations:
    0. Exit: Exit the program.
    1. Push: Push element into the stack.
    2. Pop: Remove the top element from the stack.
    3. Display: Display all the elements present in the stack.

Structure:

                ---------------------------
           ---> |    Data    |    Next    |
           |    ---------------------------
           --------------------------
                                    |
               ---------------------------
               |    Data    |    Next    |
               ---------------------------
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    @staticmethod
    def __display_options() -> None:
        print("""
                0. Exit
                1. Push
                2. Pop
                3. Display
            """)

    def __push(self) -> None:
        value: object = input("Enter a value: ")
        current_node: Node = Node(value)

        if self.head is None:
            self.head = current_node
            self.tail = current_node
        else:
            self.tail.next = current_node
            self.tail = current_node

    def __pop(self) -> None:
        if self.head:
            if self.__get_list_length() == 1:
                print(f"Element {self.tail.data} is removed from stack")
                self.head = None
                self.tail = None
            else:
                previous_node: Node = self.__get_previous_node()
                previous_node.next = None

                print(f"Element {self.tail.data} is removed from stack")

                self.tail = previous_node

        else:
            print("The stack is empty")

    def __get_previous_node(self) -> Node:
        temp: Node = self.head
        previous_node: (None, Node) = None

        while temp:
            if temp.data == self.tail.data:
                break

            previous_node = temp
            temp = temp.next

        return previous_node

    def __display(self) -> None:
        temp: (None, Node) = self.head
        data: list[int] = []

        if temp:
            while temp:
                data.append(temp.data)
                temp = temp.next

            self.__display_stack(data=data)
        else:
            print("The stack is empty")

    @staticmethod
    def __display_stack(data: list[int]) -> None:
        """ Display elements in the form of stack """
        for i in range(len(data) - 1, -1, -1):
            print(f"|    {data[i]}    ", " " * (len(str(max(data))) - len(str(data[i]))), "|")
            print("-" * (12 + len(str(max(data)))))

    def __get_list_length(self) -> int:
        list_length: int = 0
        temp: (None, Node) = self.head

        while temp:
            list_length += 1
            temp = temp.next

        return list_length

    def start(self) -> None:
        while True:
            self.__display_options()

            match int(input("Select your option: ")):
                case 0:
                    break
                case 1:
                    self.__push()
                case 2:
                    self.__pop()
                case 3:
                    self.__display()
                case _:
                    print("Invalid option")

        exit(0)


if __name__ == '__main__':
    Stack().start()
