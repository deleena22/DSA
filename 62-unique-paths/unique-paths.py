class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        row = [1] * n

        
        for j in range((m-1)):
            for i in range(n):
                if i == 0:
                    row[i] = row[i]
                else:
                    row[i] = row[i] + row[i-1]
        
        return row[-1]



        