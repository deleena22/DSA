class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals = sorted(intervals, key = lambda x: x[0])
        curr_end = 0
        for interval in intervals:
            start, end = interval
            if start >= curr_end:
                curr_end = end
            else:
                return False
        return True

