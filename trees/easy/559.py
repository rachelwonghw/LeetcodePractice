class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        elif not root.children: return 1
        else:
            height = [self.maxDepth(child) for child in root.children]    
            return max(height) + 1