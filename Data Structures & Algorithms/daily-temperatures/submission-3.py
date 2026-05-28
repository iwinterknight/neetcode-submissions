class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while st and st[-1][0] < temp:
                pop_temp, pop_i = st.pop()
                res[pop_i] = i - pop_i
            st.append((temp, i))
            
        while st:
            _, pop_i = st.pop()
            res[pop_i] = 0

        return res