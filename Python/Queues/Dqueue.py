"""
Dequeue:

Brief Explanation:
    About Queue:
        Queue is a data structure where the first inserted element will be removed first. Insertion is done at the back
        and deletion is done at the back.
    About Dqueue:
        Dequeue is a data structure where the insertion and deletion happens at both the ends.

Implementation:
    Dequeue is implemented using array.

Structure:
                            ----------------------------------------
    Insertion/Deletion   -> |    Data    |    Data    |    Data    | <- Insertion/Deletion
            Front           ----------------------------------------       Rear

Operations:
    0. Exit: Exit the program.
    1. Add At End: Data is added at the end of the list.
    2. Add At Beginning: Data is added at the beginning of the list.
    3. Delete At Beginning: Data is deleted at the beginning.
    4. Delete At End: Data is deleted at the end.
    5. Display: Display the entire list.
    6. Count: Return the occurrence of a given number.
"""

import sys


class Dqueue:
    """ Dequeue """

    def __init__(self):
        """ Constructor """
        self.d_queue: list[int] = []

    @staticmethod
    def __display_options() -> None:
        """ Display's the available options """
        print("""
                ***************
                    Dequeue
                    
                    0. Exit
                    1. Add At Beginning
                    2. Add At End
                    3. Delete At Beginning
                    4. Delete At End
                    5. Display
                    6. Count
                ***************
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
                        self.d_queue.insert(0, value)
                        print(f"Value {value} is added to D-Queue!")
                    case 2:
                        value: int = int(input("Enter a number: "))
                        self.d_queue.append(value)
                        print(f"Value {value} is added to D-Queue!")
                    case 3:
                        if self.d_queue:
                            value: int = self.d_queue.pop(0)
                            print(f"Value {value} has been removed from D-Queue!")
                        else:
                            print("Dequeue is empty!")
                    case 4:
                        if self.d_queue:
                            value: int = self.d_queue.pop(len(self.d_queue) - 1)
                            print(f"Value {value} has been removed from D-Queue!")
                        else:
                            print("Dequeue is empty!")
                    case 5:
                        if self.d_queue:
                            print(*self.d_queue, sep=" ")
                        else:
                            print("Dequeue is empty!")
                    case 6:
                        if self.d_queue:
                            value: int = int(input("Enter a number: "))

                            if value in self.d_queue:
                                print(f"Value {value} is present {self.d_queue.count(value)} time's!")
                            else:
                                print(f"Value {value} is not present in Dequeue!")
                        else:
                            print("Dequeue is empty!")
                    case _:
                        print("Invalid option!")
            except ValueError:
                print("Invalid input!")


if __name__ == '__main__':
    Dqueue().start()
    sys.exit(0)
