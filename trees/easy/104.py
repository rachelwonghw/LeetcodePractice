# recursion
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root: return 0
        
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
            
        return max(left_height, right_height) + 1

# iteration
class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        
        stack = []
        if root:
            stack.append((root, 1))

        max_depth = 0
        while stack != []:
            node, curr_depth = stack.pop()
            if node:
                max_depth = max(curr_depth, max_depth)
                stack.append((node.left, curr_depth + 1))
                stack.append((node.right, curr_depth + 1))
            
        return max_depth