"""
Dijkstra Algorithm:
    Dijkstra algorithm is used to find the shortest path between two vertices of a graph. It differs from the minimum
    cost spanning tree because the shortest distance between two vertices might not include all the vertices of the
    graph.
"""

import sys


class Dijkstra:
    __vertices_length: (None, int) = None
    __edges: list = []
    __vertices: list = []
    __visited_and_distance: list = [[0, 0]]

    @staticmethod
    def __display_options() -> None:
        """ Display the available options """
        print("""
                    ***************************
                        Dijkstra Algorithm

                        0. Exit
                        1. Add edge
                        2. Dijkstra Algorithm
                        3. Display
                    ***************************
                """)

    def __display(self) -> None:
        """ Display all edges and nodes along with cost """
        if self.__edges:
            for i in range(self.__vertices_length):
                for j in range(self.__vertices_length):
                    if self.__vertices[i][j] == 1 and self.__vertices[j][i] == 1:
                        print(f"""
{"-" * (10 + len(str(i + 1)))}{" " * (12 + len(str(self.__edges[i][j])))}{"-" * (10 + len(str(j + 1)))} 
|    {i + 1}    | ---- {self.__edges[i][j]} ---- |    {j + 1}    |
{"-" * (10 + len(str(i + 1)))}{" " * (12 + len(str(self.__edges[i][j])))}{"-" * (10 + len(str(j + 1)))}
                                        """)
        else:
            print("Graph is empty!")

    def __fill_vertices_and_edges(self) -> None:
        """ Take the number of vertices as input from user """
        vertices: int = int(input("Enter the number of vertices: "))
        self.__vertices_length = vertices

        self.__edges = [[0 for _ in range(self.__vertices_length)] for _ in range(self.__vertices_length)]
        self.__vertices = [[0 for _ in range(self.__vertices_length)] for _ in range(self.__vertices_length)]

    def __add_edge(self) -> None:
        """ Add edge, vertices and cost """
        vertex_1 = int(input("Enter vertex 1: "))
        vertex_2 = int(input("Enter vertex 2: "))
        cost = int(input("Enter cost: "))

        if not vertex_1 <= self.__vertices_length:
            print(f"Invalid vertex 1 number: {vertex_1}")
        elif not vertex_2 <= self.__vertices_length:
            print(f"Invalid vertex 2 number: {vertex_2}")
        else:
            self.__vertices[vertex_1 - 1][vertex_2 - 1] = 1
            self.__vertices[vertex_2 - 1][vertex_1 - 1] = 1
            self.__edges[vertex_1 - 1][vertex_2 - 1] = cost
            self.__edges[vertex_2 - 1][vertex_1 - 1] = cost

            print(f"Vertices {vertex_1} and {vertex_2} with cost: {cost} is added to the graph!")

    def __dijkstra_algorithm(self) -> None:
        """ Apply dijkstra algorithm on the graph """
        for i in range(self.__vertices_length - 1):
            self.__visited_and_distance.append([0, sys.maxsize])

        for vertex in range(self.__vertices_length):
            to_visit = self.__to_be_visited()

            for neighbour_index in range(self.__vertices_length):
                # Updating new distance
                if self.__vertices[to_visit][neighbour_index] == 1 and \
                        self.__visited_and_distance[neighbour_index][0] == 0:
                    new_distance = self.__visited_and_distance[to_visit][1] + self.__edges[to_visit][neighbour_index]

                    if self.__visited_and_distance[neighbour_index][1] > new_distance:
                        self.__visited_and_distance[neighbour_index][1] = new_distance

                self.__visited_and_distance[to_visit][0] = 1

        self.__print_distance()

    def __print_distance(self) -> None:
        """ Printing the distance """
        i = 1

        for distance in self.__visited_and_distance:
            print(f"Distance from vertex {1} to vertex {i} is {distance[1]}")
            i += 1

    def __to_be_visited(self):
        """ Find next vertex to be visited """
        v = -10

        for index in range(self.__vertices_length):
            if (self.__visited_and_distance[index][0] == 0) and (
                    (v < 0) or (self.__visited_and_distance[index][1] <= self.__visited_and_distance[v][1])):
                v = index

        return v

    def start(self) -> None:
        """ Main method """
        try:
            self.__fill_vertices_and_edges()

            while True:
                self.__display_options()

                match int(input("Select your option: ")):
                    case 0:
                        break
                    case 1:
                        self.__add_edge()
                    case 2:
                        self.__dijkstra_algorithm()
                    case 3:
                        self.__display()
                    case _:
                        print("Invalid input!")
        except ValueError:
            print("Invalid input!")


if __name__ == '__main__':
    Dijkstra().start()
    sys.exit(0)
