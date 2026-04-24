class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        def solution_1(s, t):
            hs, ht = Counter(s), Counter(t)
            for hs_key, hs_value in hs.items():
                if hs_key not in ht:
                    return False
                if ht[hs_key] == hs_value:
                    ht.pop(hs_key)
            if ht:
                return False
            return True

        def solution_2(s, t):
            if len(s) != len(t):
                return False
            hs, ht = Counter(s), Counter(t)
            for hs_key, hs_value in hs.items():
                if ht[hs_key] != hs_value:
                    return False
            return True


        return solution_2(s, t)