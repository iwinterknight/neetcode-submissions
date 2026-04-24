class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(start=0, curr=""):
            if len(curr) == len(digits):
                res.append(curr)
                return

            for char in digits_to_chars[digits[start]]:
                curr += char
                backtrack(start+1, curr)
                curr = curr[:-1]

        if digits:
            backtrack()
        return res