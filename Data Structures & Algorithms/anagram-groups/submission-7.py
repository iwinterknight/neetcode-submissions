class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            ctr = Counter(s)
            key = tuple(sorted(ctr.items()))
            d[key].append(s)
        return list(d.values())
            
