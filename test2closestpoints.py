import numpy as np
from main import Point, NearestPointSet

class ClosestPointsTest:
    def __init__(self, set_size):
        set = NearestPointSet()

        x_coords = np.random.randint(0, high=200000, size=set_size, dtype=int)
        y_coords = np.random.randint(0, high=200000, size=set_size, dtype=int)

        def create_plot(pointSet):
            for i in range(0, len(x_coords) - 1):
                pointSet.pointList.append(Point(x_coords[i], y_coords[i]))

        create_plot(set)

        result_brute_force = set.find_closest_brute_force(set.pointList)
        print(f"brute force: point1: ({result_brute_force[0].coords[0]},{result_brute_force[0].coords[1]}) point2: ({result_brute_force[1].coords[0]},{result_brute_force[1].coords[1]}), distance: {result_brute_force[2]}")

        result_faster = set.find_closest_faster(set.pointList)
        print(f"faster: point1: ({result_faster[0].coords[0]},{result_faster[0].coords[1]}) point2: ({result_faster[1].coords[0]},{result_faster[1].coords[1]}), distance: {result_faster[2]}")


#points_test0 = ClosestPointsTest(0)
#points_test1 = ClosestPointsTest(1)
points_test10 = ClosestPointsTest(10)

#points_test100 = ClosestPointsTest(100)

#points_test1000 = ClosestPointsTest(1000)

#points_test1000000 = ClosestPointsTest(1000000)

