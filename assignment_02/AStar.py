from heapq import heappush, heappop

from assignment_02.Map import MapObj


# data structure representing the nodes used in A-star
class Node:

    def __init__(self, state, parent, path_cost, est_total_cost):
        """
        :param state: coordinates of the cell, that is, (x, y)
        :param parent: parent node of the node
        :param path_cost: cost from the starting position to this node
        :param est_total_cost: estimated total costs from the starting
        across this node and to the goal, i.e, f(n) = g(n) + h(n)
        """
        self.parent = parent
        self.path_cost = path_cost
        self.est_total_cost = est_total_cost
        self.state = state

    def __lt__(self, other):
        return self.est_total_cost < other.est_total_cost

    def __gt__(self, other):
        return self.est_total_cost > other.est_total_cost

    def __eq__(self, other):
        return self.est_total_cost == other.est_total_cost


def search(map_obj: MapObj, heuristic, moving_goal=False):
    """
    Applies the A-star algorithm to construct a cost-optimal
    path in the map comprising a set of interconnected nodes

    :param map_obj: map object representing the map of samfundet
    :param heuristic: heuristic function used to estimate the cost to the goal
    :param moving_goal: if true, tick() function is called on every iteration of A-star
    :return: the leaf-node of the optimal path. Calling node.parent recursively reveals the optimal path.
    """

    # create the root node using the starting position
    node = Node(
        state=map_obj.start_pos,
        parent=None,
        path_cost=0,
        est_total_cost=0 + heuristic(map_obj.start_pos, map_obj.goal_pos)
    )

    if map_obj.is_goal(node.state):
        return node

    # initialise frontier priority queue and list of reached nodes
    frontier = []
    heappush(frontier, node)
    reached = [node.state]

    while len(frontier) > 0:

        # calls tick every iteration if the goal is moving
        if moving_goal:
            map_obj.tick()

        node = heappop(frontier)

        # expand each child_node of the current node
        for child_node in expand(map_obj, node, heuristic):

            # return the child_node if its coordinates (i.e. state) are the same
            # as the goal
            if map_obj.is_goal(child_node.state):
                return child_node

            # append the child node to the frontier and reached if the coordinates (i.e. state)
            # has not been reached yet
            if child_node.state not in reached:
                reached.append(child_node.state)
                heappush(frontier, child_node)
    return None


def expand(map_obj, node, heuristic):
    """
    Creates child nodes based on the possible actions (i.e. movement options)
    from the current node.

    :param map_obj: map object representing the map of samfundet
    :param node: to be expanded node
    :param heuristic: heuristic function used for estimating the cost to the goal
    :return: list containing all expanded child nodes
    """
    nodes = []

    # get the possible actions based on the current coordinates and the state of the
    # surrounding cells
    for action in map_obj.get_actions(node.state):

        # get destination coordinates of the cell based on executing the current action
        dest = map_obj.get_result(node.state, action)

        # calculate the path cost based on the amounted path cost to the current cell
        # and the cost of moving to the adjacent cell
        path_cost = node.path_cost + map_obj.get_cell_value(dest)

        # estimate costs to the goal from the child node using the given heuristic
        est_total_cost = path_cost + heuristic(dest, map_obj.get_goal_pos())

        # create a new child node based on the previously acquired information
        nodes.append(Node(
            state=dest,
            parent=node,
            path_cost=path_cost,
            est_total_cost=est_total_cost
        ))
    return nodes
