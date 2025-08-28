class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        i = 0
        for num in nums:
            diff = target - num
            if diff in map:
                return [map[diff], i]
            map[num] = i
            i += 1
        