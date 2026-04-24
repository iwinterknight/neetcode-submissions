class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lookup = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
                    "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(digits, start, curr, res):
            if len(curr) == len(digits):
                res.append(curr)
                return

            for lttr in lookup[digits[start]]:
                curr += lttr
                backtrack(digits, start+1, curr, res)
                curr = curr[:-1]


        res = []
        if digits:
            backtrack(digits, 0, "", res)
        return res
            
