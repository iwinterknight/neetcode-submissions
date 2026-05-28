class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token.lstrip("-").isdigit():  #token.lstrip("-").replace(".", "", 1).isalnum()
                st.append(int(token))
            else:
                num1 = st.pop()
                num2 = st.pop()
                if token == "+":
                    st.append(num1 + num2)
                elif token == "-":
                    st.append(num2 - num1)
                elif token == "*":
                    st.append(num1 * num2)
                elif token == "/":
                    st.append(int(num2 / num1))
        return st[0]
