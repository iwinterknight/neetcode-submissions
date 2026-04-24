class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def is_anagram(s, t):
            return Counter(s) == Counter(t)
        
        res = {}
        for s in strs:
            in_dict = False
            for k, v in res.items():
                if is_anagram(s, k):
                    v.append(s)
                    in_dict = True
            if not in_dict:
                res[s] = [s]
        return list(res.values())