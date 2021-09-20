from heapq import heappush, heappop

from assignment_02.Map import MapObj


class Node:

    def __init__(self, state, parent, path_cost, est_total_cost):
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
    node = Node(
        state=map_obj.start_pos,
        parent=None,
        path_cost=0,
        est_total_cost=0 + heuristic(map_obj.start_pos, map_obj.goal_pos)
    )
    if map_obj.is_goal(node.state):
        return node
    frontier = []
    heappush(frontier, node)
    reached = [node.state]

    while len(frontier) > 0:
        if moving_goal:
            map_obj.tick()
        node = heappop(frontier)

        for child_node in expand(map_obj, node, heuristic):
            if map_obj.is_goal(child_node.state):
                return child_node
            if child_node.state not in reached:
                reached.append(child_node.state)
                heappush(frontier, child_node)
    return None


def expand(map_obj, node, heuristic):
    nodes = []
    for action in map_obj.get_actions(node.state):
        dest = map_obj.get_result(node.state, action)
        path_cost = node.path_cost + map_obj.get_cell_value(dest)
        est_total_cost = path_cost + heuristic(dest, map_obj.get_goal_pos())
        nodes.append(Node(
            state=dest,
            parent=node,
            path_cost=path_cost,
            est_total_cost=est_total_cost
        ))
    return nodes
