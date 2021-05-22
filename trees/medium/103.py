from collections import deque

# modified dfs
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        def traversal(node, depth):
            if node is None: return
            if depth >= len(results): results.append(deque([node.val]))
            else:
                if depth % 2 == 0:
                    results[depth].append(node.val)
                else:
                    results[depth].appendleft(node.val)
            traversal(node.left, depth + 1)
            traversal(node.right, depth + 1)
            
        traversal(root, 0)
        return results

# modified bfs
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue, results = deque([root]), []
        
        while queue:
            queue_length, level = len(queue), deque([])
            
            for i in range(queue_length):
                node = queue.popleft()
                if len(results) % 2 == 0:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        
            results.append(list(level))
        return results