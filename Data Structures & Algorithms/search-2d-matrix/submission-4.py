class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l <= r:
            mid = l + (r-l) // 2
            if matrix[mid][0] <= target:
                l = mid + 1
            else:
                r = mid - 1
        row_idx = l-1

        l, r = 0, len(matrix[0])-1
        while l <= r:
            mid = l + (r-l) // 2
            curr = matrix[row_idx][mid]
            if curr == target:
                return True
            elif curr < target:
                l = mid + 1
            else:
                r = mid - 1
        return False