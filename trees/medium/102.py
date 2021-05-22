from collections import deque

# bfs
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue, results = deque([root]), []
        
        while queue:
            queue_length, level = len(queue), []
        
            for i in range(queue_length):
                node = queue.popleft()
                level.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                
            results.append(level)
            
        return results

# dfs
class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        def dfs(node, depth):
            if node is None: return
            if len(results) == depth: results.append([])
            results[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return results