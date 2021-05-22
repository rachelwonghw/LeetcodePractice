class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        maps = {")": "(", "]" : "[", "}" : "{"}
        for char in s:
            if char in maps:
                top_ele = stack.pop() if stack else "#"
                if maps[char] != top_ele:
                    return False
            else:
                stack.append(char)
                
        return not stack