import math


class Node:
    """Class that defines a node in a state space."""

    def __init__(self, x, y):
        self.location = x, y
        self.g = self.h = self.f = 0
        self.parent = 0


def calc_path_length(start_location, end_location):
    """Calculates the path length from a start node to an end node via
    trigonometry."""
    x = abs(start_location[0] - end_location[0])
    y = abs(start_location[1] - end_location[1])
    return math.sqrt((x ** 2) + (y ** 2))


def shortest_path(M, start, goal):
    """Finds the shortest path using the A* algorithm.

    Interpretation from Wikipedia A* Search Algorithm:
        https://en.wikipedia.org/wiki/A*_search_algorithm

    Walkthrough of algorithm to aid in understanding:
        https://www.youtube.com/watch?v=aKYlikFAV4k&t=1632s

    """
    path = [goal]
    nodes = [Node(x, y) for x, y in M.intersections.values()]

    explored = set()
    frontier = set()

    frontier.add(start)

    while len(frontier) > 0:

        # Find node in frontier with smallest f value.
        current_node = 0
        current_f = goal  # starting limiter
        for node in frontier:
            if nodes[node].f <= current_f:
                current_node = node
                current_f = nodes[node].f

        if current_node == goal:
            break

        frontier.remove(current_node)
        explored.add(current_node)

        for road in M.roads[current_node]:
            if road in explored:
                continue

            # Find g; current_node -> road.
            start_location = nodes[current_node].location
            road_location = nodes[road].location
            goal_location = nodes[goal].location
            temp_g = nodes[current_node].g + calc_path_length(start_location,
                                                              road_location)

            if road in frontier and temp_g >= nodes[road].g:
                continue
            else:
                frontier.add(road)

            # Set all road parameters
            nodes[road].g = temp_g
            nodes[road].h = calc_path_length(road_location, goal_location)
            nodes[road].f = nodes[road].g + nodes[road].h
            nodes[road].parent = current_node

            # insert parent trail to list.
    node = goal
    while node != start:
        node = nodes[node].parent
        path.insert(0, node)

    return path
