class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            # ctr = Counter(s)
            # key = tuple(sorted(ctr.items()))
            charr = [0] * 26
            for c in s:
                idx = ord(c) - 97
                charr[idx] += 1
            d[tuple(charr)].append(s)
        return list(d.values())
            
