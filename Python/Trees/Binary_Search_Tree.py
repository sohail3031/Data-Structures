"""
Binary Search Tree:
    Binary search tree is a simple non-linear data structure in which the data is stored in tree format.

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
        self.left: (None, Node) = None
        self.data: int = data
        self.right: (None, Node) = None


class BinarySearchTree:
    def __init__(self):
        self.root: (None, Node) = None
        self.inorder_successors: list = []

    @staticmethod
    def _display_options() -> None:
        print("""
                0. Exit
                1. Insert
                2. Delete
                3. Display
                4. Pre-order Traversal
                5. In-order Traversal
                6. Post-order Traversal
        """)

    @staticmethod
    def _display_traverse_options() -> None:
        print("""
                1. Pre Order
                2. In Order
                3. Post Order
        """)

    def _insert(self, value: int, current_node: (None, Node)) -> None:
        if current_node is None:
            current_node = Node(value)
            self.root = current_node
        else:
            if value < current_node.data:
                if current_node.left is None:
                    current_node.left = Node(value)
                else:
                    self._insert(value, current_node.left)
            else:
                if current_node.right is None:
                    current_node.right = Node(value)
                else:
                    self._insert(value, current_node.right)

    def _delete_node(self, value: int) -> None:
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

    def _display(self, current_node: (None, Node)) -> None:
        lines, *_ = self._display_tree(current_node=current_node)

        for line in lines:
            print(line)

    def _display_tree(self, current_node: (None, Node)):
        if (current_node.right is None) and (current_node.left is None):
            line: str = "%i" % current_node.data
            width: int = len(line)
            height: int = 1
            middle: int = width // 2

            return [line], width, height, middle

        if current_node.right is None:
            lines, n, p, x = self._display_tree(current_node=current_node.left)
            s: str = "%i" % current_node.data
            u: int = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "-" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]

            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if current_node.left is None:
            lines, n, p, x = self._display_tree(current_node=current_node.right)
            s: str = "%i" % current_node.data
            u: int = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]

            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        left, n, p, x = self._display_tree(current_node=current_node.left)
        right, m, q, y = self._display_tree(current_node=current_node.right)
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

    def pre_order_traverse(self, current_node: (None, Node)) -> list[int]:
        elements: list[int] = []

        if current_node:
            elements.append(current_node.data)
            elements += self.pre_order_traverse(current_node=current_node.left)
            elements += self.pre_order_traverse(current_node=current_node.right)

        return elements

    def in_order_traverse(self, current_node: (None, Node)) -> list[int]:
        elements: list[int] = []

        if current_node:
            elements = self.in_order_traverse(current_node=current_node.left)
            elements.append(current_node.data)
            elements += self.in_order_traverse(current_node=current_node.right)

        return elements

    def post_order_traverse(self, current_node: (None, Node)) -> list[int]:
        elements: list[int] = []

        if current_node:
            elements = self.post_order_traverse(current_node=current_node.left)
            elements += self.post_order_traverse(current_node=current_node.right)
            elements.append(current_node.data)

        return elements

    def start(self) -> None:
        while True:
            self._display_options()

            try:
                match int(input("Select your option: ")):
                    case 0:
                        break
                    case 1:
                        value: int = int(input("Enter a number: "))
                        self._insert(value, self.root)
                    case 2:
                        value: int = int(input("Enter a number: "))
                        self._delete_node(value=value)
                    case 3:
                        self._display(self.root)
                    case 4:
                        if self.root:
                            print(*self.pre_order_traverse(current_node=self.root), sep=" -> ")
                        else:
                            print("Binary Tree is empty")
                    case 5:
                        if self.root:
                            print(*self.in_order_traverse(current_node=self.root), sep=" -> ")
                        else:
                            print("Binary Tree is empty")
                    case 6:
                        if self.root:
                            print(*self.post_order_traverse(current_node=self.root), sep=" -> ")
                        else:
                            print("Binary Tree is empty")
                    case _:
                        print("Invalid option")
            except ValueError:
                print("Invalid input format. Number is required.")


if __name__ == '__main__':
    BinarySearchTree().start()
    sys.exit(0)
