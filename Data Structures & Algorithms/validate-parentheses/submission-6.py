class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque

        chars = list(s)
        dq = deque()

        for char in chars:
            if char == "(" or char == "{" or char == "[":
                dq.append(char)
            elif char == ")":
                if len(dq) == 0:
                    return False
                if not dq.pop() == "(":
                    return False
            elif char == "]":
                if len(dq) == 0:
                    return False
                if not dq.pop() == "[":
                    return False
            elif char == "}":
                if len(dq) == 0:
                    return False
                if not dq.pop() == "{":
                    return False

        if not len(dq) == 0:
            return False
        
        return True