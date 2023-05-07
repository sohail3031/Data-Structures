"""
Binary Tree Sort:
    Binary Tree Sort is a sorting algorithm in which the data inserted in the tree can be retried in a sorted manner.
    The best technique to traverse is in-order traversal. In in-order traversal, the left node is traversed first, then
    the root and last the right node.
"""

import sys


class Node:
    """ Node """

    def __init__(self, data: int):
        self.left: (None, Node) = None
        self.data: int = data
        self.right: (None, Node) = None


class BinaryTreeSort:
    """ Binary Tree Sort """

    def __init__(self):
        """ Constructor """
        self.root: (None, Node) = None
        self.node_is_present: bool = False

    @staticmethod
    def _display_options() -> None:
        """ Display's the option for main function """
        print("""
            ************************
                Binary Tree Sort
                
                0. Exit
                1. Insert
                2. Delete
                3. Display Tree
                4. Sort
            ************************
        """)

    def _insert_node(self, value: int, current_node: (None, Node)) -> None:
        """ Insert node in binary tree """
        if current_node is None:
            current_node = Node(value)
            self.root = current_node
        else:
            if value < current_node.data:
                if current_node.left is None:
                    current_node.left = Node(value)
                else:
                    self._insert_node(value, current_node.left)
            else:
                if current_node.right is None:
                    current_node.right = Node(value)
                else:
                    self._insert_node(value, current_node.right)

    def _check_delete_conditions(self, value: int, current_node: (None, Node)) -> None:
        """ Checks the condition for deletion """
        if self.root:
            self._check_if_node_is_present(value=value, current_node=current_node)

            if self.node_is_present:
                self._delete_node(value=value, current_node=current_node)
            else:
                print(f"Value: {value} is not present in the node")

            self.node_is_present = False
        else:
            print("Binary Tree is Empty!")

    def _delete_node(self, value: int, current_node: Node) -> Node:
        """ Delete node from binary tree """
        if value < current_node.data:
            current_node.left = self._delete_node(value=value, current_node=current_node.left)
        elif value > current_node.data:
            current_node.right = self._delete_node(value=value, current_node=current_node.right)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            temp: Node = self._get_inorder_successor(current_node=current_node.right)
            current_node.data = temp.data
            current_node.right = self._delete_node(value=temp.data, current_node=current_node.right)

        return current_node

    @staticmethod
    def _get_inorder_successor(current_node: Node) -> Node:
        """ Returns the inorder successor """
        temp: Node = current_node

        while temp.left is not None:
            temp = temp.left

        return temp

    def _check_if_node_is_present(self, value: int, current_node: Node) -> None:
        """ Checks if the node is present in the binary tree """
        if current_node.data == value:
            self.node_is_present = True
        if current_node.left:
            self._check_if_node_is_present(value=value, current_node=current_node.left)
        if current_node.right:
            self._check_if_node_is_present(value=value, current_node=current_node.right)

    def _sort(self, current_node: Node) -> list[int]:
        """ Sort the tree in inorder format """
        elements: list[int] = []

        if current_node:
            elements = self._sort(current_node=current_node.left)
            elements.append(current_node.data)
            elements += self._sort(current_node=current_node.right)

        return elements

    def _display(self, current_node: (None, Node)) -> None:
        """ Prints the tree """
        lines, *_ = self._display_tree(current_node=current_node)

        for line in lines:
            print(line)

    def _display_tree(self, current_node: (None, Node)):
        """ Create tree from the given data """
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

    def start(self) -> None:
        """ Main function """
        while True:
            self._display_options()

            try:
                match int(input("Select your option: ")):
                    case 0:
                        break
                    case 1:
                        value: int = int(input("Enter a number: "))

                        self._insert_node(value=value, current_node=self.root)
                    case 2:
                        value: int = int(input("Enter a number: "))

                        self._check_delete_conditions(value=value, current_node=self.root)
                    case 3:
                        if self.root:
                            self._display(current_node=self.root)
                        else:
                            print("Binary Tree is Empty!")
                    case 4:
                        if self.root:
                            print(*self._sort(current_node=self.root), sep=" -> ")
                        else:
                            print("Binary Tree is Empty!")
            except ValueError:
                print("Invalid input format. Number is required!")


if __name__ == '__main__':
    BinaryTreeSort().start()
    sys.exit()
