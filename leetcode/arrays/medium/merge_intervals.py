# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

"""
    INPUTS/OUTPUTS
        [[1,3],[2,6],[8,10],[15,18]]
        =>
        [[1,6], [8,10], [15,18]]

    NOTES


"""


def mergeIntervals(intervals):
    intervals.sort(key=lambda i: i[0])

    res = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = res[-1][1]

        if start <= last_end:
            res[-1][1] = max(end, last_end)
        else:
            res.append([start, end])

    return res
