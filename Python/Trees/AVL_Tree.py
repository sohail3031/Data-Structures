"""
AVL Tree:
    AVL Tree is a balanced binary tree. The height of the left subtree munis height of right subtree should be either
    equal to -1, 0 and 1. To calculate the balance factor, traverse the maximum nodes on both sides of the tree. If the
    value is other than this, the tree will balance itself. To do so, it uses balance factor. It can balance itself by
    using four methods LL, RR, LR, and RL.

    e.g: height of left tree - height of right tree = {-1, 0, 1}

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
        self.height: int = 1


class AVLTree:
    def __init__(self):
        self.root: (None, Node) = None

    @staticmethod
    def _display_options() -> None:
        print("""
                ****************************
                    AVL Tree
                
                    0. Exit
                    1. Insert
                    2. Delete
                    3. Display
                    4. Pre-order Traversal
                    5. In-order Traversal
                    6. Post-order Traversal
                ****************************
        """)

    def _insert_node(self, value: int, current_node: (None, Node)) -> (None, Node):
        """ Insert an element into the tree """
        if self.root is None:
            self.root = current_node = Node(value)
        elif current_node is None:
            current_node = Node(value)
        elif value < current_node.data:
            current_node.left = self._insert_node(value=value, current_node=current_node.left)
        else:
            current_node.right = self._insert_node(value=value, current_node=current_node.right)

        """ Update the balance factor and balance the tree """
        current_node.height = 1 + max(self._get_height(current_node=current_node.left),
                                      self._get_height(current_node=current_node.right))
        balance_factor: int = self._get_balance(current_node=current_node)

        if balance_factor > 1:
            if current_node.data < current_node.left.data:
                return self._right_rotate(current_node=current_node)
            else:
                current_node.left = self._left_rotate(current_node=current_node.left)
                return self._right_rotate(current_node=current_node)

        if balance_factor < -1:
            if current_node.data > current_node.right.data:
                return self._left_rotate(current_node=current_node)
            else:
                current_node.right = self._right_rotate(current_node=current_node.right)
                return self._left_rotate(current_node=current_node)

        return current_node

    def _left_rotate(self, current_node: (None, Node)) -> (None, Node):
        """ Perform the left rotation """
        temp_right: (None, Node) = current_node.right
        temp_left: (None, Node) = temp_right.left
        temp_right.left = current_node
        current_node.right = temp_left

        current_node.height = 1 + max(self._get_height(current_node=current_node.left),
                                      self._get_height(current_node=current_node.right))
        temp_right.height = 1 + max(self._get_height(current_node=temp_right.left),
                                    self._get_height(current_node=temp_right.right))

        return temp_right

    def _right_rotate(self, current_node: (None, Node)) -> (None, Node):
        """ Perform the right rotation """
        temp_left: (None, Node) = current_node.left
        temp_right: (None, Node) = temp_left.right
        temp_left.right = current_node
        current_node.left = temp_right

        current_node.height = 1 + max(self._get_height(current_node=current_node.left),
                                      self._get_height(current_node=current_node.right))
        temp_left.height = 1 + max(self._get_height(current_node=temp_left.left),
                                   self._get_height(current_node=temp_left.right))

        return temp_left

    def _get_balance(self, current_node: (None, Node)) -> int:
        """ Get the balance factor of the node """
        if current_node is None:
            return 0

        return self._get_height(current_node=current_node.left) - self._get_height(current_node=current_node.right)

    @staticmethod
    def _get_height(current_node: (None, Node)) -> int:
        """ Returns the height of the tree or if the tree is empty it returns the zero(0) """
        if current_node is None:
            return 0

        return current_node.height

    def _delete_node(self, value: int, current_node: (None, Node)):
        """ Finds the node with the value and delete it """
        if current_node is None:
            return current_node
        elif value < current_node.data:
            current_node.left = self._delete_node(value=value, current_node=current_node.left)
        elif value > current_node.data:
            current_node.right = self._delete_node(value=value, current_node=current_node.right)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            temp: (None, Node) = self._get_min_value_node(current_node=current_node.right)
            current_node.data = temp.data
            current_node.right = self._delete_node(value=value, current_node=current_node.right)

        """ Update the balance factor of the nodes """
        if current_node is None:
            return current_node

        current_node.height = 1 + max(self._get_height(current_node=current_node.left),
                                      self._get_height(current_node=current_node.right))
        balance_factor = self._get_balance(current_node=current_node)

        """ Balance the tree """
        if balance_factor > 1:
            if self._get_balance(current_node=current_node.left) >= 0:
                return self._right_rotate(current_node=current_node)
            else:
                current_node.left = self._left_rotate(current_node=current_node.left)
                return self._right_rotate(current_node=current_node)

        if balance_factor < -1:
            if self._get_balance(current_node=current_node):
                return self._left_rotate(current_node=current_node)
            else:
                current_node.right = self._right_rotate(current_node=current_node.right)
                return self._left_rotate(current_node=current_node)

        return current_node

    def _get_min_value_node(self, current_node: (None, Node)) -> (None, Node):
        if (current_node is None) or (current_node.left is None):
            return current_node

        return self._get_min_value_node(current_node=current_node.left)

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

    def _pre_order_traverse(self, current_node: (None, Node)) -> list[int]:
        elements: list[int] = []

        if current_node:
            elements.append(current_node.data)
            elements += self._pre_order_traverse(current_node=current_node.left)
            elements += self._pre_order_traverse(current_node=current_node.right)

        return elements

    def _in_order_traverse(self, current_node: (None, Node)) -> list[int]:
        elements: list[int] = []

        if current_node:
            elements = self._in_order_traverse(current_node=current_node.left)
            elements.append(current_node.data)
            elements += self._in_order_traverse(current_node=current_node.right)

        return elements

    def _post_order_traverse(self, current_node: (None, Node)) -> list[int]:
        elements: list[int] = []

        if current_node:
            elements = self._post_order_traverse(current_node=current_node.left)
            elements += self._post_order_traverse(current_node=current_node.right)
            elements.append(current_node.data)

        return elements

    def start(self) -> None:
        """ Main function """
        while True:
            self._display_options()

            try:
                match int(input("Select your option: ")):
                    case 0:
                        break
                    case 1:
                        try:
                            value: int = int(input("Enter a number: "))

                            self._insert_node(value=value, current_node=self.root)
                        except ValueError:
                            print("Invalid input format. Number is required.")
                    case 2:
                        try:
                            value: int = int(input("Enter a number: "))

                            self._delete_node(value=value, current_node=self.root)
                        except ValueError:
                            print("Invalid input format. Number is required.")
                    case 3:
                        self._display(current_node=self.root)
                    case 4:
                        if self.root:
                            print(*self._pre_order_traverse(current_node=self.root))
                        else:
                            print("Threaded Binary Tree is empty")
                    case 5:
                        if self.root:
                            print(*self._in_order_traverse(current_node=self.root))
                        else:
                            print("Threaded Binary Tree is empty")
                    case 6:
                        if self.root:
                            print(*self._post_order_traverse(current_node=self.root))
                        else:
                            print("Threaded Binary Tree is empty")
                    case _:
                        print("Invalid option")
            except ValueError:
                print("Invalid input format. Number is required.")


if __name__ == '__main__':
    AVLTree().start()
    sys.exit(0)
