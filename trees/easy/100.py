class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if (p is None or q is None): return p == q;
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right);