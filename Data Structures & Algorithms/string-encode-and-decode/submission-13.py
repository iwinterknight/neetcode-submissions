class Solution:
    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for s in strs:
            encoding += f"{len(s)},"
        encoding += "#"
        encoding += "".join(strs)
        return encoding
        

    def decode(self, s: str) -> List[str]:
        strs = []
        print(s)
        if s == "#":
            return []
        splts = s.split("#", 1)
        numbers = splts[0].split(",")
        if numbers == ['0', '']:
            return [""] 
        start = 0
        i = 0
        for end, c in enumerate(splts[1]):
            if end == start + int(numbers[i]):
                strs.append(splts[1][start : end])
                start = end
                i += 1
        strs.append(splts[1][start : end+1])
        start = end
        i += 1
        return strs