import numpy as np
from main import Point, NearestPointSet


class SmallCorrectnessEdgeCaseTests:
    def __init__(self, x_coords, y_coords):
        self.x_coords = x_coords
        self.y_coords = y_coords
        self.pointSet = NearestPointSet()

        def create_plot():
            for i in range(0, len(x_coords)):
                self.pointSet.insert(Point(self.x_coords[i], self.y_coords[i]))
        create_plot()

        if len(x_coords) > 1:
            result_brute_force = self.pointSet.find_closest_brute_force(self.pointSet.pointList)
            print(f"brute force: point1: ({result_brute_force[0].coords[0]},{result_brute_force[0].coords[1]}) point2: ({result_brute_force[1].coords[0]},{result_brute_force[1].coords[1]}), distance: {result_brute_force[2]}")

        if len(x_coords) > 1:
            result_faster = self.pointSet.find_closest_faster(self.pointSet.pointList)
            print(f"faster: point1: ({result_faster[0].coords[0]},{result_faster[0].coords[1]}) point2: ({result_faster[1].coords[0]},{result_faster[1].coords[1]}), distance: {result_faster[2]}")

        else:
            print("looks like you need to add more points!")

class ClosestPointsTest:
    def __init__(self, set_size):
        set = NearestPointSet()

        x_coords = np.random.randint(0, high=200000, size=set_size, dtype=int)
        y_coords = np.random.randint(0, high=200000, size=set_size, dtype=int)
        def create_plot(pointSet):
            for i in range(0, len(x_coords)):
                pointSet.pointList.append(Point(x_coords[i], y_coords[i]))

        create_plot(set)



#small_correct_test1 = SmallCorrectnessEdgeCaseTests([3, 3, 7, 8], [3, 3, 4, 6])
#small_correct_test2 = SmallCorrectnessEdgeCaseTests([2, 1, 9, 8], [1, 3, 8, 9])
#small_correct_test3 = SmallCorrectnessEdgeCaseTests([1, 5, 600, 7000], [1, 3, 90000, 10])
#small_correct_test4 = SmallCorrectnessEdgeCaseTests([4, 7, 9000, 70, 2590, 32, 16], [4, 3, 90, 725, 22500, 10, 11])
#small_correct_test5 = SmallCorrectnessEdgeCaseTests([2, 67, 35, 42, 17, 22, 3897], [2, 45, 25, 9890, 22311, 78961, 250])

edge_case_0_points = SmallCorrectnessEdgeCaseTests([], [])
edge_case_1_point = SmallCorrectnessEdgeCaseTests([5], [2])
edge_case_2_points = SmallCorrectnessEdgeCaseTests([3, 4], [2, 7])
edge_case_negative_numbers = SmallCorrectnessEdgeCaseTests([-3, 0, 5], [-2, 0, -1])
edge_case_multiple_options_for_correct_answer = SmallCorrectnessEdgeCaseTests([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])



#points_test0 = ClosestPointsTest(0)
#points_test1 = ClosestPointsTest(1)
#points_test1 = ClosestPointsTest(2)
#points_test10 = ClosestPointsTest(10)

#points_test100 = ClosestPointsTest(100)

#points_test1000 = ClosestPointsTest(1000)

#points_test1000000 = ClosestPointsTest(1000000)

