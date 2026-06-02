class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        # binary search 

        def binarySearch(left, right): # left = 0, right = 50
            middle = left + ((right - left ) // 2)
            # if the middle is smaller, include it, if greater, don't
            if (middle ** 2) == x:
                return middle
            elif middle == left:
                if (right ** 2) == x:
                    return right
                else:
                    return left
            else:
                # multiple in range
                if (middle ** 2) > x:
                    return binarySearch(left, middle)
                else:
                    return binarySearch(middle, right)
        return binarySearch(0, x)




        