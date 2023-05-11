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
                1. Enter a node
                2. Enter a adjacent node
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

    def __find_dfs(self, node: int, visited: list, component: list) -> None:
        """ Find the DFS """
        component.append(node)
        visited[node] = True

        for i in self.__graph.get(list(self.__graph.keys())[node]):
            if not visited[int(i)]:
                self.__find_dfs(node=int(i), visited=visited, component=component)

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
                        component: list = []
                        visited: list[bool] = [False] * len(self.__graph)
                        self.__find_dfs(node=int(list(self.__graph.keys())[0]), visited=visited, component=component)
                        print("DFS: ", end="")
                        print(*component, sep=" -> ")
                    case 4:
                        self.__display()
                    case _:
                        print("Invalid option!")
            except ValueError:
                print("Invalid input!")


if __name__ == '__main__':
    DFS().start()
    sys.exit(0)
