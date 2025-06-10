import unittest
from task3.main import create_group_intervals, get_merged_intervals, get_lesson_times, calculate_overlap, appearance


class TestIntervalFunctions(unittest.TestCase):
    def test_create_group_intervals(self):
        self.assertEqual(create_group_intervals([1, 2, 3, 4]), [(1, 2), (3, 4)])
        self.assertEqual(create_group_intervals([]), [])
        self.assertEqual(create_group_intervals([1, 2, 3, 4, 5, 6, 7, 8]), [(1, 2), (3, 4), (5, 6), (7, 8)])

    def test_get_merged_intervals(self):
        intervals_dict = {
            'pupil': [1, 2, 3, 4],
            'tutor': [4, 5, 6, 7]
        }
        self.assertEqual(get_merged_intervals(intervals_dict), [1, 2, 3, 4, 4, 5, 6, 7])

        intervals_dict = {
            'pupil': [],
            'tutor': []
        }
        self.assertEqual(get_merged_intervals(intervals_dict), [])

        intervals_dict = {
            'pupil': [1, 2],
            'tutor': []
        }
        self.assertEqual(get_merged_intervals(intervals_dict), [1, 2])

    def test_get_lesson_times(self):
        intervals_dict = {
            'lesson': [100, 200]
        }
        self.assertEqual(get_lesson_times(intervals_dict), (100, 200))

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
            'lesson': [1594663200, 1594666800],
            'pupil':[],
            'tutor':[]
        }
        self.assertEqual(appearance(intervals), 0)

        intervals = {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389],
            'tutor': []
        }
        self.assertEqual(appearance(intervals), 49)

        intervals = {
            'lesson': [500, 1000],
            'pupil': [400, 600],
            'tutor': [700, 1200]
        }
        self.assertEqual(appearance(intervals), 400)

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
        self.assertEqual(appearance(intervals), 250)


if __name__ == '__main__':
    unittest.main()
