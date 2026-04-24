class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def recurse(digits, i, curr, res):
            if i == len(digits):
                res.append(curr)
                return

            for lttr in self.letters[digits[i]]:
                curr += lttr
                recurse(digits, i+1, curr, res)
                curr = curr[:-1]
            
        if not digits:
            return []
        res = []
        recurse(digits, 0, "", res)
        return res
        