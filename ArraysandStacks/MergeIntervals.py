"""
You are given a list of intervals where each interval is represented as [start, end].
Your job is to merge all overlapping intervals and return the result.

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Sort intervals by start time.

Use a result list and iterate through intervals:

    If current interval overlaps with the last in result, merge them.

    Else, just add the current interval.


Input: [[1,3], [2,6], [8,10], [15,18]]

    Sort: [[1,3], [2,6], [8,10], [15,18]]

    Start with first interval: [1,3]

    Compare with [2,6] → they overlap → merge to [1,6]

    Compare with [8,10] → no overlap → add as-is

    Compare with [15,18] → no overlap → add as-is

"""


def merge(intervals: list[list[int]]) -> list[list[int]]:

    if not intervals:
        return []

    # Step1: Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for interval in intervals:

        last = merged[-1]

        # If current overlaps with last, merge them

        if interval[0] <= last[1]:
            last[1] = max(last[1], interval[1])

        else:
            merged.append(interval)

    return


def main():
    tests = [
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
        [[1, 4], [0, 4]],
        [],
        [[1, 4]],
        [[1, 4], [2, 3]],
    ]

    for idx, intervals in enumerate(tests):
        result = merge(intervals)
        print(f"Test Case {idx + 1}:")
        print(f"Input: {intervals}")
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
