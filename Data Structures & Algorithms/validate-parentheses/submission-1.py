class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bkts = {"(": ")", "{": "}", "[": "]"}
        for c in s:
            if c in bkts:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    if bkts[stack[-1]] != c:
                        return False
                    else:
                        stack.pop()
        if stack:
            return False
        return True