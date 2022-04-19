# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import collections
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        # Idea: do level order traversal AND put nodes in a queue
        # tuple (node, level, direction)
        
        # pop stack, read children left to right into stack
        # when result level is odd, 1,3,5... append to sub-array
        # when result level is even 0,2,4,6.. appendLeft to sub-array
        
        '''
        (3,0)
        (9,1)
        (91,900)
        '''
        # q= [3,9, 91, 900, 911, 902, 901 ]
        # result = [[3],[9],[91, 900], [911, 902, 901]]
        
        
        '''
        q = [151] 
        result = [3] [20] [15, 7] [150] [151]
        
        
        '''
        
        stack = collections.deque([(root,0)])
        result = collections.defaultdict(collections.deque)


        while stack:

            node, level = stack.pop()
            # print(node)
            
            if node:

                if level % 2 == 0:
                    result[level].appendleft(node.val)
                else:
                    result[level].append(node.val)

                if node.left:
                    stack.append((node.left, level+1))

                if node.right:   
                    stack.append((node.right, level+1))

        
        output = []
        for k in result:
            output.append(result[k])
        
        return output
    
    