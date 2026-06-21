from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        queue = deque()

        for ch in s:
            if ch in ["(" , "{", "["]:
                stack.append(ch)
            
            if ch in [")", "}" , "]"]:
                if not stack:
                    return False
                peek = stack[-1]
                if (peek == "(" and ch == ")") or (peek == "[" and ch == "]") or peek == "{" and ch == "}":
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False