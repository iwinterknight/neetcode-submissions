class Solution:
    def simplifyPath(self, path: str) -> str:
        splts = path.split("/")
        res = []
        for splt in splts:
            splt = splt.strip()
            if not splt or splt == ".":
                continue
            if splt == "..":
                if res:
                    res.pop()
            else:
                res.append(splt)
        res = "/" + "/".join(res)
        return res