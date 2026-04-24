class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        def mat_to_lin(r, c):
            return r * n + c

        def lin_to_mat(i):
            r, c = i // n, i % n
            return r, c

        l, r = 0, m*n-1
        while l <= r:
            mid = l + (r-l) // 2
            row, col = lin_to_mat(mid)
            num = matrix[row][col]

            print(l, r, mid, num)

            if num == target:
                return True
            if num < target:
                l = mid + 1
            else:
                r = mid - 1
        return False