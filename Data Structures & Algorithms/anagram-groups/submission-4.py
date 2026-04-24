class Solution:
    from collections import Counter
    
    def match(self, a: str, b: str) -> bool:
        return Counter(a) == Counter(b)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            is_anagram = False
            for k, v in d.items():
                if self.match(k, s):
                    is_anagram = True
                    v.append(s)
                    break
            if not is_anagram:
                d[s] = [s]
        return list(d.values())