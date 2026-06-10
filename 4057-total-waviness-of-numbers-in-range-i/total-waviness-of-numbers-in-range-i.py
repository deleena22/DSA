class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """

        def num_check(num):
            count = 0
            if num < 100:
                return count
            else:
                str_num = str(num)
                p1, p2, p3 = 0, 1, 2
                while p3 < len(str_num):
                    if str_num[p2] < str_num[p1] and str_num[p2] < str_num[p3]:
                        count += 1
                    elif str_num[p2] > str_num[p1] and str_num[p2] > str_num[p3]:
                        count += 1
                    p1 += 1
                    p2 += 1
                    p3 += 1
                return count
        
        total = 0
        for i in range(num1, num2 + 1):
            total += num_check(i)
        return total

        