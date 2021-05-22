class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        def dfs(node, Sum, visited, answer):
            if not node: return
            visited.append(node.val)
            if Sum == node.val and not node.left and not node.right:
                answer.append(list(visited))
            else:
                dfs(node.left, Sum - node.val, visited, answer)
                dfs(node.right, Sum - node.val, visited, answer)
            visited.pop()
        
        answer = []
        dfs(root, targetSum, [], answer)
        return answer