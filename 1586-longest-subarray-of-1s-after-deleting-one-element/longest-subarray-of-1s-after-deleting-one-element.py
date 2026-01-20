class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [0,1,1,0,0]

        currmax = 0
        lastzero = 0
        windowhaszero = False
        if 0 not in nums:
            return len(nums) - 1

        p1 = 0

        for p2 in range(len(nums)):
            if nums[p2] == 0:
                if windowhaszero == False:
                    # no zeros are in, allowed one
                    lastzero = p2
                    windowhaszero = True
                    currmax = max(currmax, p2 - p1 + 1)
                else:
                    p1 = lastzero + 1
                    lastzero = p2
            else: # at a 1
                currmax = max(currmax, p2 - p1 + 1)
                # equal to 1
        return currmax - 1



        