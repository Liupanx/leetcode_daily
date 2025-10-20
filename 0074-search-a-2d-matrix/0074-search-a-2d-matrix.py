class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m - 1
        row = -1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                row = mid
                break
            if target < matrix[mid][0]:
                hi = mid - 1
            else:
                lo = mid + 1
        if row == -1:
            return False

        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            x = matrix[row][mid]
            if x == target:
                return True
            if x < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False