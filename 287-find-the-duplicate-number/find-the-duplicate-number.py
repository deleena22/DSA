class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # fast and slow

        #floyds

        slow, fast = nums[0], nums[nums[0]]

        while fast != slow:

            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = 0

        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        