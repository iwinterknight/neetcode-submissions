class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def approach_1():
            index = 0
            while True:
                if index < len(strs[0]):
                    ch = strs[0][index]
                    for s in strs[1:]:
                        if index > len(s) or s[index] != ch:
                            return strs[0][:index]
                    index += 1
            return strs[0][:index]

        def approach_2():
            lengths = []
            if len(strs) == 0:
                return ""
            if len(strs) == 1:
                return strs[0]
            for s in strs:
                lengths.append(len(s))
            
            start = 0
            start_indices = []
            for l in lengths:
                start_indices.append(start)
                start += l
            start_indices.append(start)

            # print(start_indices,lengths)

            concat = "".join(strs)

            if not concat:
                return ""
                
            itr = 0
            res = ""
            while True:
                # print(concat, itr)
                char = concat[itr]
                for i, st in enumerate(start_indices[:-1]):
                    # print(itr + st, start_indices[i+1])
                    if itr + st == start_indices[i+1] or concat[itr+st] != concat[itr]:
                        return res
                res += concat[itr]
                itr += 1


            return ""
        
        return approach_2()

        