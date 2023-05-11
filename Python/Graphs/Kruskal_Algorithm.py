"""
Kruskal Algorithm:
    The kruskal algorithm says that we should always select the minimum cost edge from the graph until and unless it's
    not forming a cycle in the new graph. The graph is undirected.
"""

import sys


class Kruskal:
    __edge: list[list[int, int, int]] = []

    @staticmethod
    def __display_options() -> None:
        """ Display the available options """
        print("""
                **************************
                    Kruskal Algorithm

                    0. Exit
                    1. Add edge
                    2. Kruskal Algorithm
                    3. Display
                **************************
            """)

    def __vertices(self) -> int:
        """ Return the length of the graph """
        return len(self.__edge)

    def __add_edge(self) -> None:
        """ Add edge, vertices and cost """
        vertex_1 = int(input("Enter vertex 1: "))
        vertex_2 = int(input("Enter vertex 2: "))
        cost = int(input("Enter cost: "))

        self.__edge.append([vertex_1, vertex_2, cost])

        print(f"Vertices {vertex_1} and {vertex_2} with cost: {cost} is added to the graph!")

    def __kruskal_algorithm(self) -> None:
        """ Apply kruskal algorithm on the given graph """
        result: list = []
        i, e = 0, 0
        self.__edge = sorted(self.__edge, key=lambda item: item[2])
        parent: list = []
        rank: list = []

        for node in range(self.__vertices()):
            parent.append(node)
            rank.append(0)

        while i < self.__vertices() - 1:
            vertex_1, vertex_2, cost = self.__edge[i]
            i += 1
            x = self.__find(parent=parent, x=vertex_1)
            y = self.__find(parent=parent, x=vertex_2)

            if x != y:
                e += 1
                result.append([vertex_1, vertex_2, cost])
                self.__apply_union(parent=parent, rank=rank, x=x, y=y)

        minimum_cost: int = 0

        for v_1, v_2, weight in result:
            minimum_cost += weight
            print(f"{v_1} - {v_2}: {weight}")

        print(f"Minimum Cost: {minimum_cost}")

    def __find(self, parent: list, x: int) -> int:
        """ Return the value """
        if parent[x] == x:
            return x

        return self.__find(parent=parent, x=parent[x])

    def __apply_union(self, parent: list, rank: list, x: int, y: int) -> None:
        """ Apply union """
        x_root = self.__find(parent=parent, x=x)
        y_root = self.__find(parent=parent, x=y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def __display(self) -> None:
        """ Display all edges and nodes along with cost """
        if self.__edge:
            for i in self.__edge:
                print(f"""
{"-" * (10 + len(str(i[0])))}{" " * (12 + len(str(i[2])))}{"-" * (10 + len(str(i[0])))}
|    {i[0]}    | ---- {i[2]} ---- |    {i[1]}    |
{"-" * (10 + len(str(i[0])))}{" " * (12 + len(str(i[2])))}{"-" * (10 + len(str(i[0])))}
                """)
        else:
            print("Graph is empty!")

    def start(self) -> None:
        """ Main method """
        while True:
            self.__display_options()

            try:
                match int(input("Select your option: ")):
                    case 0:
                        break
                    case 1:
                        self.__add_edge()
                    case 2:
                        self.__kruskal_algorithm()
                    case 3:
                        self.__display()
                    case _:
                        print("Invalid input!")
            except ValueError:
                print("Invalid input!")


if __name__ == '__main__':
    Kruskal().start()
    sys.exit(0)
