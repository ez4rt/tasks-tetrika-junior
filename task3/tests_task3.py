import unittest
from main import (create_group_intervals, get_lesson_times, calculate_overlap, appearance, clearing_intervals,
                  intersection_intervals)


class TestIntervalFunctions(unittest.TestCase):
    def test_create_group_intervals(self):
        self.assertEqual(create_group_intervals([1, 2, 3, 4]), [(1, 2), (3, 4)])
        self.assertEqual(create_group_intervals([]), [])
        self.assertEqual(create_group_intervals([1, 2, 3, 4, 5, 6, 7, 8]), [(1, 2), (3, 4), (5, 6), (7, 8)])

    def test_get_lesson_times(self):
        intervals_dict = {
            'lesson': [100, 200]
        }
        self.assertEqual(get_lesson_times(intervals_dict), [100, 200])

    def test_calculate_overlap(self):
        self.assertEqual(calculate_overlap((100, 200), 150, 250), 50)
        self.assertEqual(calculate_overlap((250, 350), 200, 300), 50)
        self.assertEqual(calculate_overlap((100, 150), 200, 250), 0)
        self.assertEqual(calculate_overlap((300, 450), 200, 250), 0)
        self.assertEqual(calculate_overlap((150, 250), 100, 300), 100)
        self.assertEqual(calculate_overlap((200, 100), 150, 250), 0)
        self.assertEqual(calculate_overlap((150, 150), 150, 250), 0)

    def test_appearance(self):
        intervals = {
            'lesson': [100, 200],
            'pupil': [],
            'tutor': []
        }
        self.assertEqual(appearance(intervals), 0)

        intervals = {
            'lesson': [100, 200],
            'pupil': [150, 199],
            'tutor': []
        }
        self.assertEqual(appearance(intervals), 0)

        intervals = {
            'lesson': [500, 1000],
            'pupil': [400, 600],
            'tutor': [700, 1200]
        }
        self.assertEqual(appearance(intervals), 0)

        intervals = {
            'lesson': [1000, 2000],
            'pupil': [10, 20],
            'tutor': [5000, 6000]
        }
        self.assertEqual(appearance(intervals), 0)

        intervals = {
            'lesson': [500, 600],
            'pupil': [100, 200, 300, 700],
            'tutor': [10, 900, 550, 650]
        }
        self.assertEqual(appearance(intervals), 100)

        intervals = {
            'lesson': [125, 678],
            'pupil': [100, 200, 200, 205, 45, 100, 105, 125],
            'tutor': [100, 300, 300, 350, 670, 780]
        }
        self.assertEqual(appearance(intervals), 80)


class TestClearingIntervals(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(clearing_intervals([]), [])

    def test_no_overlap(self):
        intervals = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(clearing_intervals(intervals), intervals)

    def test_overlap(self):
        intervals = [(1, 3), (2, 4), (5, 7), (6, 8)]
        self.assertEqual(clearing_intervals(intervals), [(1, 4), (5, 8)])

    def test_full_overlap(self):
        intervals = [(1, 5), (2, 4), (3, 6)]
        self.assertEqual(clearing_intervals(intervals), [(1, 6)])

    def test_adjacent_intervals(self):
        intervals = [(1, 2), (2, 3), (3, 4)]
        self.assertEqual(clearing_intervals(intervals), [(1, 4)])

    def test_unsorted_intervals(self):
        intervals = [(3, 4), (1, 2), (2, 3)]
        self.assertEqual(clearing_intervals(intervals), [(1, 4)])

    def test_single_interval(self):
        intervals = [(1, 2)]
        self.assertEqual(clearing_intervals(intervals), [(1, 2)])

    def test_complex_overlap(self):
        intervals = [(1, 5), (2, 6), (8, 10), (15, 18), (16, 20)]
        self.assertEqual(clearing_intervals(intervals), [(1, 6), (8, 10), (15, 20)])

    def test_intervals_with_same_start(self):
        intervals = [(1, 3), (1, 5)]
        self.assertEqual(clearing_intervals(intervals), [(1, 5)])

    def test_intervals_with_same_end(self):
        intervals = [(1, 5), (3, 5)]
        self.assertEqual(clearing_intervals(intervals), [(1, 5)])


class TestIntersectionIntervals(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(intersection_intervals([], []), [])

    def test_empty_list1(self):
        self.assertEqual(intersection_intervals([], [(1, 2)]), [])

    def test_empty_list2(self):
        self.assertEqual(intersection_intervals([(1, 2)], []), [])

    def test_no_intersection(self):
        list1 = [(1, 2)]
        list2 = [(3, 4)]
        self.assertEqual(intersection_intervals(list1, list2), [])

    def test_single_intersection(self):
        list1 = [(1, 3)]
        list2 = [(2, 4)]
        self.assertEqual(intersection_intervals(list1, list2), [(2, 3)])

    def test_multiple_intersections(self):
        list1 = [(1, 3), (5, 7)]
        list2 = [(2, 4), (6, 8)]
        self.assertEqual(intersection_intervals(list1, list2), [(2, 3), (6, 7)])

    def test_one_list_contains_other(self):
        list1 = [(1, 5)]
        list2 = [(2, 3), (4, 5)]
        self.assertEqual(intersection_intervals(list1, list2), [(2, 3), (4, 5)])

    def test_identical_intervals(self):
        list1 = [(1, 2), (3, 4)]
        list2 = [(1, 2), (3, 4)]
        self.assertEqual(intersection_intervals(list1, list2), [(1, 2), (3, 4)])

    def test_overlapping_intervals(self):
        list1 = [(1, 4)]
        list2 = [(2, 5)]
        self.assertEqual(intersection_intervals(list1, list2), [(2, 4)])

    def test_complex_intersections(self):
        list1 = [(1, 5), (8, 12), (15, 20)]
        list2 = [(0, 10), (11, 13), (18, 25)]
        self.assertEqual(intersection_intervals(list1, list2), [(1, 5), (8, 10), (11, 12), (18, 20)])

    def test_adjacent_intervals(self):
        list1 = [(1, 2)]
        list2 = [(2, 3)]
        self.assertEqual(intersection_intervals(list1, list2), [])

    def test_interval_contained_within_another(self):
        list1 = [(2, 4)]
        list2 = [(1, 5)]
        self.assertEqual(intersection_intervals(list1, list2), [(2, 4)])


if __name__ == '__main__':
    unittest.main()
