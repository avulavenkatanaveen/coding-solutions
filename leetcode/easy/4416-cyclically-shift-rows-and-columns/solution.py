class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        
        after_row_shift=[[0] * n for _ in range(n)]
        for i in range(n):
            k=rowShift[i]
            for j in range(n):
                new_col=(j-k+n)%n
                after_row_shift[i][new_col]=grid[i][j]
        result = [[0] * n for _ in range(n)]
        for j in range(n):
            k=colShift[j]
            for i in range(n):
                new_row=(i-k+n)%n
                result[new_row][j]=after_row_shift[i][j]             
        return result
        