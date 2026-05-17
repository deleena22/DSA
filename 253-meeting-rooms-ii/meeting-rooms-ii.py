class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        end_times = []
        num_rooms = 0

        intervals.sort(key=lambda x: x[0])
        start, end = intervals[0]
        num_rooms += 1
        end_times.append(end)

        currmin_endtime = end

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < currmin_endtime:
                num_rooms += 1
                end_times.append(end)
            else:
                i = end_times.index(currmin_endtime)
                end_times[i] = end
            currmin_endtime = min(end_times)
        return num_rooms

        