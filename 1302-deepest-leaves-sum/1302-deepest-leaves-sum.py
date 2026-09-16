# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que = deque([root])
        while que:
            level_sum = 0
            level_size = len(que)
            for _ in range(level_size):
                node = que.popleft()
                level_sum+=node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return level_sum
        

        
            
        