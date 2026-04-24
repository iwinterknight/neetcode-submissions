class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        def recursive(open, close, res):
            if open == n and close == n:
                stack.append(res)
                return
            if open < n:
                recursive(open+1, close, res + "(")
            if close < open:
                recursive(open, close+1, res + ")")

        recursive(0, 0, "")
        return stack
