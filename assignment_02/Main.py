from Map import MapObj
from assignment_02.AStar import search
from assignment_02.Heuristics import euclidian_distance


def main():
    """
    The main function finds the most cost-efficient route
    for all maps using the A-star algorithm. Each map is
    printed before and after the application of the algorithm
    and the path is highlighted in green. I did not optimise
    A-star with respect to the moving goal (in other words:
    I skipped the optional task).
    """
    for task in range(1, 6):
        # get map object for the current task
        map_obj = MapObj(task=task)
        # display map
        map_obj.show_map()
        # find cost optimal path using a-star
        node = search(
            map_obj=map_obj,
            heuristic=euclidian_distance,
            moving_goal=(task == 5)
        )
        # draw optimal path on map
        map_obj.draw_path(node)
        # display the map
        map_obj.show_map()


if __name__ == '__main__':
    main()
