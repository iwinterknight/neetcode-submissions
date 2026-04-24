class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return collections.Counter(s) == collections.Counter(t)
        if len(s) != len(t):
            return False

        counts = [0] * 26
        for ch in s:
            lttr_idx = ord(ch) - 97
            counts[lttr_idx] += 1
        for ch in t:
            lttr_idx = ord(ch) - 97
            counts[lttr_idx] -= 1
            if counts[lttr_idx] < 0:
                return False
        
        return True
        