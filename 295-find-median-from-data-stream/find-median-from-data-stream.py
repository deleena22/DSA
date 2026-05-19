import heapq
class MedianFinder(object):
 

    def __init__(self):

        self.left = []
        self.right = []
        heapq.heapify(self.left)
        heapq.heapify(self.right)
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """


        heapq.heappush(self.left, -num)
        if self.left and self.right and ((-1 * self.left[0]) > self.right[0]):
            val = heapq.heappop(self.left)
            heapq.heappush(self.right, -val)
        if len(self.left) > len(self.right):
            val = heapq.heappop(self.left)
            heapq.heappush(self.right, -val)
        if len(self.left) < len(self.right):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)
        
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left) > len(self.right):
            val = -1 * self.left[0]
        elif len(self.right) > len(self.left):
            val = self.right[0]
        else:
            valleft = -1 * self.left[0]
            valright = self.right[0]
            val = (valleft + valright) / 2.0
        return val


            


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()