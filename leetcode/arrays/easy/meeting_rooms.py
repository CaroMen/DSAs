# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

"""
    INPUTS/OUTPUTS
        intervals = [[0,30],[5,10],[15,20]] => false

    NOTES
        - we should look if the start time is less than the end time
        - if the start time is less than the end time, that means we have an over lap
        ex: [[1, 10], [3, 20]]
        - in the example, our second meeting starts way before the first one ends because that start time is less than the end time of the first meeting

    SOLUTION
        - we should sort the list based on the first value in the inner lists
        - we then loop starting from the first index all the way to the end, so that we can compare to the prior meeting
        - if our start time of the current meeting is less than the end time of the previous meeting, return False because there's an over lap
"""


def canAttendMeetings(intervals):
    intervals.sort(key=lambda i: i[0])

    for idx in range(1, len(intervals)):
        if intervals[idx][0] < intervals[idx - 1][1]:
            return False

    return True
