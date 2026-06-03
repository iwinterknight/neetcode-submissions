class Solution:
    def calPoints(self, operations: List[str]) -> int:
        def is_number(e):
            try:
                float(e)
                return True
            except ValueError:
                return False

        st = []
        for op in operations:
            if is_number(op):
                st.append(int(op))
            elif op == "+":
                e1 = st.pop()
                e2 = st.pop()
                st.append(e2)
                st.append(e1)
                st.append(e1 + e2)
            elif op == "C":
                st.pop()
            elif op == "D":
                e = st[-1]
                st.append(e*2)
        res = 0
        while st:
            res += st.pop()
        return res