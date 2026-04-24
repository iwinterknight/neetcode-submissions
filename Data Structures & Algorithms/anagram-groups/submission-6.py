class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            charr = [0] * 26
            for c in s:
                idx = ord(c) - 97
                charr[idx] += 1
            key = tuple(charr)
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        return list(d.values())
