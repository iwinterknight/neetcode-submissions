class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_rect = 0
        for i, h in enumerate(heights):
            popped_i = None
            while stack and h < stack[-1][0]:
                popped_h, popped_i = stack.pop()
                max_rect = max(max_rect, popped_h * (i-popped_i))
            if popped_i is not None:
                stack.append((h, popped_i))
            else:
                stack.append((h, i))
        n = len(heights)
        while stack:
            popped_h, popped_i = stack.pop()
            max_rect = max(max_rect, popped_h * (n-popped_i))
        return max_rect