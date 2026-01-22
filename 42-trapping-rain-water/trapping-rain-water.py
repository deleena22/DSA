class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left, right = 0, len(height) - 1
        water = 0
        maxleft = height[left]
        maxright = height[right]

        while left < right:
            if height[left] < height[right]:
                # left wall is shorter
                left = left + 1 # bottom
                maxleft = max(maxleft, height[left]) # take the higher of bottom/maxleft?
                water = water + max(0, maxleft - height[left])
            else:
                right = right - 1 # bottom
                maxright = max(maxright, height[right]) # take the higher of bottom/maxleft?
                water = water + max(0, maxright - height[right])

        return water









        
