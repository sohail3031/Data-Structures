"""
Breadth First Search (BFS):
    BFS is an undirected graph in which the nodes are traversed in the breadth wise manner. For example, if a node is
    selected, we will explore all the adjacent nodes of that node and move on to the next node. Generally we use queue
    to keep track of the nodes to be visited.

E.g:
    5       4       7      6
      \   /           \   /
        1 ------------ 2 ----------- 3

    The BFS of the above graph is
        1, 2, 4, 5, 7, 3, 6
"""
import collections
import sys


class BFS:
    __graph: dict = {}

    @staticmethod
    def __display_options() -> None:
        """ Display the available options """
        print("""
            ********************************
                Breadth First Search (BFS)

                0. Exit
                1. Add a node
                2. Add a adjacent node
                3. Find BFS
                4. Display
            ********************************
        """)

    def __add_node(self) -> None:
        """ Add a node in the graph """
        value: int = int(input("Enter a number: "))

        if value in self.__graph.keys():
            print(f"Node with value: {value} already exists!")
        else:
            self.__graph.update({value: []})
            print(f"Node with value: {value} added!")

    def __add_adjacent_node(self) -> None:
        """ Add adjacent node to the existing node """
        key: int = int(input("Enter a key: "))

        if key in self.__graph.keys():
            value: int = int(input("Enter a value: "))
            self.__graph.get(key).append(value)
            print(f"Adjacent node with value: {value} is added to the node: {key}")
        else:
            print(f"No node with value: {key} found!")

    def __find_bfs(self, node: int) -> list[int]:
        """ Find the DFS """
        visited, queue = list(), collections.deque([node])
        visited.append(node)

        while queue:
            vertex = queue.popleft()

            for i in self.__graph[vertex]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)

        return visited

    def __display(self) -> None:
        """ Display the entire graph """
        if self.__graph.keys():
            for i in self.__graph.keys():
                print(f"Node: {i}, Adjacent Nodes: {self.__graph.get(i)}")
        else:
            print("No elements to display!")

    def start(self) -> None:
        """ Main method """
        while True:
            self.__display_options()

            try:
                match int(input("Select your option: ")):
                    case 0:
                        break
                    case 1:
                        self.__add_node()
                    case 2:
                        self.__add_adjacent_node()
                    case 3:
                        visited: list[int] = self.__find_bfs(node=int(list(self.__graph.keys())[0]))
                        print("DFS: ", end="")
                        print(*visited, sep=", ")
                    case 4:
                        self.__display()
                    case _:
                        print("Invalid option!")
            except ValueError:
                print("Invalid input!")


if __name__ == "__main__":
    BFS().start()
    sys.exit(0)
