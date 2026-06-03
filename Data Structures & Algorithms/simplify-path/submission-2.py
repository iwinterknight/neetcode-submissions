class Solution:
    def simplifyPath(self, path: str) -> str:
        splts = path.split("/")
        res = []
        count = 0
        for splt in splts:
            splt = splt.strip()
            if not splt or splt == ".":
                continue
            if splt == "..":
                if count:
                    res.pop()
                    count -= 1
            else:
                res.append(splt)
                count += 1
        res = "/" + "/".join(res)
        return res