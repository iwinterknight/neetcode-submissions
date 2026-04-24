class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:            
        def scanning_approach():
            pos = 0
            break_flag = False
            while True:
                for i, s in enumerate(strs):
                    if pos == len(strs[i]) or strs[i][pos] != strs[0][pos]:
                        break_flag = True
                        break
                if break_flag:
                    break
                pos += 1
            return strs[0][:pos]

        return scanning_approach()

        