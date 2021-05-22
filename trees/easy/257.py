class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        answer = []
        def dfs(node, visited, answer):
            if not node: return
            visited.append(node.val)
            if not node.left and not node.right:
                str_output = ""
                for i in range(len(visited)):
                    str_output += str(visited[i])
                    if i + 1 != len(visited):
                        str_output += "->"
                answer.append(str_output)
                        
            dfs(node.left, visited, answer)
            dfs(node.right, visited, answer)
            visited.pop()
        
        
        dfs(root, [], answer)
        return answer

class Solution2:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        answer = []
        def dfs(node, path):
            if node:
                path += str(node.val)
                if not node.left and not node.right:
                    answer.append(path)
                else:
                    path += "->"
                    dfs(node.left, path)
                    dfs(node.right, path)
        
        
        dfs(root, "")
        return answer