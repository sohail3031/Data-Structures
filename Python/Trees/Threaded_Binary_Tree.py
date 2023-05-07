"""
Threaded Binary Tree:
    Threaded binary tree is similar to binary tree except that empty reference of left and right parts of the node
    points to its neighbour from in-order traversal.

Operations:
    0. Exit: Exit the program.
    1. Insert: Insert an element into the tree.
    2. Delete: Delete an element from the tree.
    3. Display: Display the AVL Tree.
    4. Pre-order Traversal: Display the pre-order traversal of the tree.
    5. In-order Traversal: Display the in-order traversal of the tree.
    6. Post-order Traversal: Display the post-order traversal of the tree.

Structure:
                        -----------------------------------------
                        |    Left    |    Data    |    Right    |    <- Root Node / Parent Node
                        -----------------------------------------
                            /                                   \
                          /                                      \
-----------------------------------------          -----------------------------------------
|    Left    |    Data    |    Right    |          |    Left    |    Data    |    Right    | <- Leaf Node / Child Node
-----------------------------------------          -----------------------------------------

Left: Left part contains the reference of the left child.
Data: Data contains the data to be stored in that node.
Right: Right part contains the reference of the right child.
"""

import sys


class Node:
    def __init__(self, data: int):
        self.data: data = data
        self.left: (None, Node) = None
        self.right: (None, Node) = None


class ThreadedBinaryTree:
    def __init__(self):
        self.root: (None, Node) = None
        self.inorder_data: list[int] = []
        self.inorder_successors: list = []

    @staticmethod
    def __display_options() -> None:
        """ Display's options """
        print("""
            ****************************
                Threaded Binary Tree
            
                0. Exit
                1. Insert
                2. Remove
                3. Search
                4. Display
                5. Pre-order Traversal
                6. In-order Traversal
                7. Post-order Traversal
            ****************************
        """)

    def __insert_node(self, value: int, current_node: (None, Node)) -> None:
        """ Insert an element into the tree """
        if current_node is None:
            current_node = Node(value)
            self.root = current_node
        else:
            if value < current_node.data:
                if current_node.left is None:
                    current_node.left = Node(value)
                else:
                    self.__insert_node(value=value, current_node=current_node.left)
            else:
                if current_node.right is None:
                    current_node.right = Node(value)
                else:
                    self.__insert_node(value=value, current_node=current_node.right)

    def __create_thread(self) -> None:
        """ Find nodes to create thread """
        if len(self.inorder_data) > 1:
            for i in range(len(self.inorder_data)):
                if i == 0:
                    result: (None, Node) = self.__get_node(value=self.inorder_data[i], current_node=self.root)

                    if result:
                        if result.right is None:
                            next_node: (None, Node) = self.__get_node(value=self.inorder_data[i + 1],
                                                                      current_node=self.root)

                            if next_node:
                                result.right = next_node
                elif i == len(self.inorder_data) - 1:
                    result: (None, Node) = self.__get_node(value=self.inorder_data[i], current_node=self.root)

                    if result:
                        if result.left is None:
                            previous_node: (None, Node) = self.__get_node(value=self.inorder_data[i - 1],
                                                                          current_node=self.root)

                            if previous_node:
                                result.left = previous_node
                else:
                    result: (None, Node) = self.__get_node(value=self.inorder_data[i], current_node=self.root)

                    if result:
                        if result.left is None:
                            previous_node: (None, Node) = self.__get_node(value=self.inorder_data[i - 1],
                                                                          current_node=self.root)

                            if previous_node:
                                result.left = previous_node
                        if result.right is None:
                            next_node: (None, Node) = self.__get_node(value=self.inorder_data[i + 1],
                                                                      current_node=self.root)

                            if next_node:
                                result.right = next_node

    def __get_node(self, value: int, current_node: (None, Node)) -> (None, Node):
        """ Return the node based on the value given """
        if current_node:
            if current_node.left:
                self.__get_node(value=value, current_node=current_node.left)

            if current_node.data == value:
                return current_node

            if current_node.right:
                self.__get_node(value=value, current_node=current_node.right)

    def __get_inorder(self, current_node: (None, Node)) -> None:
        """ Generate the inorder for the existing tree """
        if current_node:
            self.__get_inorder(current_node=current_node.left)
            self.inorder_data.append(current_node.data)
            self.__get_inorder(current_node=current_node.right)

    def __delete_node(self, value: int):
        if self.root:
            self.check_value(value, self.root)

            if self.inorder_successors:
                result: (None, Node) = self._delete(value=value, current_node=self.root)

                if result:
                    print(f"Node with value {value} is deleted")
                else:
                    print("Node deleted")
            else:
                print(f"No node with value {value} found")
                self.inorder_successors.clear()
        else:
            print("Binary Tree is empty")

    def _delete(self, value: int, current_node: (None, Node)) -> (None, Node):
        if current_node is None:
            return current_node

        if value < current_node.data:
            current_node.left = self._delete(value=value, current_node=current_node.left)
        elif value > current_node.data:
            current_node.right = self._delete(value=value, current_node=current_node.right)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            temp: Node = self.get_inorder_successor(current_node=current_node.right)
            current_node.data = temp.data
            current_node.right = self._delete(value=temp.data, current_node=current_node.right)

        return current_node

    @staticmethod
    def get_inorder_successor(current_node: Node) -> Node:
        temp: Node = current_node

        while temp.left is not None:
            temp = temp.left

        return temp

    def check_value(self, value: int, current_node: (None, Node)) -> None:
        if current_node.data == value:
            self.inorder_successors = [True, current_node]

        if current_node.left:
            self.check_value(value, current_node.left)

        if current_node.right:
            self.check_value(value, current_node.right)

    def __display(self, current_node: (None, Node)) -> None:
        lines, *_ = self.__display_tree(current_node=current_node)

        for line in lines:
            print(line)

    def __display_tree(self, current_node: (None, Node)):
        if (current_node.right is None) and (current_node.left is None):
            line: str = "%i" % current_node.data
            width: int = len(line)
            height: int = 1
            middle: int = width // 2

            return [line], width, height, middle

        if current_node.right is None:
            lines, n, p, x = self.__display_tree(current_node=current_node.left)
            s: str = "%i" % current_node.data
            u: int = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "-" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]

            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if current_node.left is None:
            lines, n, p, x = self.__display_tree(current_node=current_node.right)
            s: str = "%i" % current_node.data
            u: int = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]

            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        left, n, p, x = self.__display_tree(current_node=current_node.left)
        right, m, q, y = self.__display_tree(current_node=current_node.right)
        s: str = "%s" % current_node.data
        u: int = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "

        if isinstance(left, str):
            left = list(left)
        if isinstance(right, str):
            left = list(right)

        if p < q:
            left += [n * " "] * (q - p)
        else:
            right += [m * " "] * (p - q)

        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]

        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def __pre_order_traverse(self, current_node: (None, Node)) -> list[int]:
        elements: list[int] = []

        if current_node:
            elements.append(current_node.data)
            elements += self.__pre_order_traverse(current_node=current_node.left)
            elements += self.__pre_order_traverse(current_node=current_node.right)

        return elements

    def __in_order_traverse(self, current_node: (None, Node)) -> list[int]:
        elements: list[int] = []

        if current_node:
            elements = self.__in_order_traverse(current_node=current_node.left)
            elements.append(current_node.data)
            elements += self.__in_order_traverse(current_node=current_node.right)

        return elements

    def __post_order_traverse(self, current_node: (None, Node)) -> list[int]:
        elements: list[int] = []

        if current_node:
            elements = self.__post_order_traverse(current_node=current_node.left)
            elements += self.__post_order_traverse(current_node=current_node.right)
            elements.append(current_node.data)

        return elements

    def start(self) -> None:
        """ Main function """
        while True:
            self.__display_options()

            try:
                match int(input("Select your option: ")):
                    case 0:
                        break
                    case 1:
                        try:
                            value: int = int(input("Enter a number: "))
                            self.__insert_node(value=value, current_node=self.root)
                            self.__get_inorder(current_node=self.root)
                            self.__create_thread()
                        except ValueError:
                            print("Invalid input format. Number is required.")
                    case 2:
                        try:
                            value: int = int(input("Enter a number: "))
                            self.__delete_node(value=value)
                            self.__get_inorder(current_node=self.root)
                            self.__create_thread()
                        except ValueError:
                            print("Invalid input format. Number is required.")
                    case 3:
                        try:
                            value: int = int(input("Enter a number: "))

                            if value in self.inorder_data:
                                print(f"Value {value} found!")
                            else:
                                print(f"Value {value} is not present!")
                        except ValueError:
                            print("Invalid input format. Number is required.")
                    case 4:
                        self.__display(current_node=self.root)
                    case 5:
                        if self.root:
                            print(*self.__pre_order_traverse(current_node=self.root))
                        else:
                            print("Threaded Binary Tree is empty")
                    case 6:
                        if self.root:
                            print(*self.__in_order_traverse(current_node=self.root))
                        else:
                            print("Threaded Binary Tree is empty")
                    case 7:
                        if self.root:
                            print(*self.__post_order_traverse(current_node=self.root))
                        else:
                            print("Threaded Binary Tree is empty")
                    case _:
                        print("Invalid option")
            except ValueError:
                print("Invalid input format. Number is required.")


if __name__ == '__main__':
    ThreadedBinaryTree().start()
    sys.exit(0)
