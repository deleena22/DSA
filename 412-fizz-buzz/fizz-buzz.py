class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def output(i):
            # return the string fizz, buzz, fizzbuzz, or str(i)

            if i % 3 == 0 and i % 5 == 0:
                return "FizzBuzz"
            elif i % 3 == 0:
                return "Fizz"
            elif i % 5 == 0:
                return "Buzz"
            else:
                return str(i)
        res = []
        
        for i in range(n): # 0 .. n - 1
            res.append(output(i+1))
        
        return res