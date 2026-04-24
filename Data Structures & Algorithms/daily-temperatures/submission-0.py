class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                popped_index = stack.pop()[1]
                res[popped_index] = i - popped_index
            stack.append((temp, i))
        return res

                