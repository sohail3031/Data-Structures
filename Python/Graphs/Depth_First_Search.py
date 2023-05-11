"""
Depth First Search (DFS):
    DFS is an undirected graph in which the nodes are traversed in the depth wise manner. For example, if a node has two
    nodes, we will select only one node and traverse all the nodes of that node. Once all the nodes are traversed, we
    will then traverse tha remaining nodes of that node. Generally we use stack to keep track of the nodes to be
    visited.

E.g:
    5       4       7      6
      \   /           \   /
        1 ------------ 2 ----------- 3

    The DFS of the above graph is
        1, 2, 3, 6, 7, 4, 5
"""

import sys


class DFS:
    __graph: dict = {}

    @staticmethod
    def __display_options() -> None:
        """ Display the available options """
        print("""
            ********************************
                Depth First Search (DFS)
                
                0. Exit
                1. Add a node
                2. Add a adjacent node
                3. Find DFS
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

    def __find_dfs(self, node: int, visited: list) -> None:
        """ Find the DFS """
        if node not in visited:
            visited.append(node)

            for i in self.__graph[node]:
                self.__find_dfs(node=i, visited=visited)

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
                        visited: list[int] = []
                        self.__find_dfs(node=int(list(self.__graph.keys())[0]), visited=visited)
                        print("DFS: ", end="")
                        print(*visited, sep=", ")
                    case 4:
                        self.__display()
                    case _:
                        print("Invalid option!")
            except ValueError:
                print("Invalid input!")


if __name__ == "__main__":
    DFS().start()
    sys.exit(0)
