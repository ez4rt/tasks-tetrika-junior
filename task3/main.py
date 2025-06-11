def create_group_intervals(intervals: list) -> list:
    group_intervals = []
    for i in range(0, len(intervals), 2):
        if i + 1 < len(intervals):
            group_intervals.append((intervals[i], intervals[i + 1]))
        else:
            group_intervals.append((intervals[i],))
    return group_intervals


def clearing_intervals(intervals: list) -> list:
    intervals.sort()
    updated_intervals = list()
    for interval in intervals:
        if not updated_intervals or interval[0] > updated_intervals[-1][1]:
            updated_intervals.append(interval)
        else:
            updated_intervals[-1] = (updated_intervals[-1][0], max(interval[1], updated_intervals[-1][1]))
    return updated_intervals


def intersection_intervals(list1, list2):
    intersections = []
    for interval1 in list1:
        for interval2 in list2:
            start = max(interval1[0], interval2[0])
            end = min(interval1[1], interval2[1])
            if start < end:
                intersections.append((start, end))
    return intersections


def get_lesson_times(intervals: dict) -> tuple:
    return intervals['lesson']


def calculate_overlap(interval: tuple, lesson_start: int, lesson_end: int) -> int:
    enter_time = max(interval[0], lesson_start)
    exit_time = min(interval[1], lesson_end)
    return max(0, exit_time - enter_time)


def appearance(intervals: dict[str, list[int]]) -> int:
    group_intervals_tutor = create_group_intervals(intervals['tutor'])
    group_intervals_tutor = clearing_intervals(group_intervals_tutor)

    group_intervals_pupil = create_group_intervals(intervals['pupil'])
    group_intervals_pupil = clearing_intervals(group_intervals_pupil)

    group_intervals = intersection_intervals(group_intervals_pupil, group_intervals_tutor)

    start_lesson, end_lesson = get_lesson_times(intervals)

    total_time = sum(
        calculate_overlap(interval, start_lesson, end_lesson)
        for interval in group_intervals
    )

    return total_time


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                             1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                             1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                             1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
