# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        q = collections.deque([])
        
        result = 0
        
        q.append((root, 0))
        
        while q:
            
            node, cumulative_value = q.popleft()
            
            new_sum = cumulative_value*10
            
            if node and node.left:
                q.append((node.left, new_sum+ node.val))
                
                
            if node and node.right:
                q.append((node.right, new_sum+ node.val))
                
            if not node.left and not node.right: 
                
                result += new_sum+ node.val
                
        
        return result
                
        