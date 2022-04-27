# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        left_bound = []
        right_bound = []
        leaves = []
        
        def walk_tree(node, check_left, check_right): # 1->9->8
            # Sanity
            if node == None:
                return
            
            v = node.val
            
            if node.left == None and node.right == None:
                leaves.append(v)
                return
            
            # Left bound checks
            if check_left:
                left_bound.append(v)
                # If left is None, walk right as bound
                
                if None == node.left:
                    walk_tree(node.right, check_left, check_right)
                else:
                    walk_tree(node.left, check_left, check_right)
                    walk_tree(node.right, False, check_right)
            
            # Right boun checks
            elif check_right:
                right_bound.append(v)
                # If right is None, walk left as bound
                if None == node.right:
                    walk_tree(node.left, check_left, check_right)
                else:
                    walk_tree(node.left, check_left, False)
                    walk_tree(node.right, check_left, check_right)
            else:
                walk_tree(node.left, False, False)
                walk_tree(node.right, False, False)
        
        walk_tree(root.left, True, False)
        walk_tree(root.right, False, True)
        
        return [root.val] + left_bound + leaves + right_bound[::-1]