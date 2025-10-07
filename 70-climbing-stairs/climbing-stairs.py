class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        memo = {}
        def helper(n):
            if n == 0:
                return 1
            elif n < 0:
                return 0
            elif n in memo:
                return memo[n]
            
            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]
            
        
        return helper(n)

        
        