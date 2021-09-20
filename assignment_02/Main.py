from Map import MapObj
from assignment_02.AStar import search
from assignment_02.Heuristics import euclidian_distance


def main():
    for task in range(1, 5):
        map_obj = MapObj(task=task)
        map_obj.show_map()
        node = search(
            map_obj=map_obj,
            heuristic=euclidian_distance
        )
        map_obj.draw_path(node)
        map_obj.show_map()


if __name__ == '__main__':
    main()
