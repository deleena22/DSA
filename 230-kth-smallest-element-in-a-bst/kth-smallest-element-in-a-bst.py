# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution(object):
    def kthSmallest(self, root, k):
        minheap = []
        heapq.heapify(minheap)

        def pushall(node):
            heapq.heappush(minheap, node.val)
            if node.left:
                pushall(node.left)
            if node.right:
                pushall(node.right)
        pushall(root)

        for _ in range(k):
            r = heapq.heappop(minheap)
        
        return r
        


        