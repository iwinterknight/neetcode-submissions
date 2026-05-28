class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        valid = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for c in s:
            if c not in valid:
                st.append(c)
            else:
                if st and st[-1] == valid[c]:
                    st.pop()
                else:
                    return False
        return True if not st else False