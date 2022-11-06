class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in ["(","{","["]:
                stack.append(x)
            else:
                if not stack:
                    return False
                char=stack.pop()
                if char =='(' and x !=')':
                    return False
                if char =='[' and x !=']':
                    return False
                if char =='{' and x !='}':
                    return False
        if stack:
                return False
        return True
                    
