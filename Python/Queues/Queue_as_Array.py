"""
Dequeue:

Brief Explanation:
    Queue is a data structure where the first inserted element will be removed first. Insertion is done at the back and
    deletion is done at the back.

Implementation:
    Dequeue is implemented using array.

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


class Queue:
    """ Queue """

    def __init__(self):
        """ Constructor """
        self.queue: list[int] = []

    @staticmethod
    def __display_options() -> None:
        """ Display's the available options """
        print("""
                *************************
                    Queue as an Array
                    
                    0. Exit
                    1. Add
                    2. Delete
                    3. Display
                *************************
                """)

    def start(self) -> None:
        """ Main method """
        while True:
            self.__display_options()

            try:
                match int(input("Select your option: ")):
                    case 0:
                        break
                    case 1:
                        value: int = int(input("Enter a number: "))
                        self.queue.append(value)
                        print(f"Value {value} is added to queue!")
                    case 2:
                        if self.queue:
                            value: int = self.queue.pop(0)
                            print(f"Value {value} has been removed from queue!")
                        else:
                            print("Queue is empty!")
                    case 3:
                        if self.queue:
                            print(*self.queue, sep=" -> ")
                        else:
                            print("Queue is empty!")
                    case _:
                        print("Invalid option!")
            except ValueError:
                print("Invalid input!")


if __name__ == '__main__':
    Queue().start()
    sys.exit(0)
