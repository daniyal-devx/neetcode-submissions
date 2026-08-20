class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        
        # Build prefix sum matrix
        prefix = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                prefix[i+1][j+1] = (prefix[i][j+1] + 
                                     prefix[i+1][j] - 
                                     prefix[i][j] + 
                                     grid[i][j])
        
        def sum_region(row_start, row_end, col_start, col_end):
            """Get sum of a region using prefix sums"""
            return (prefix[row_end][col_end] - 
                    prefix[row_start][col_end] - 
                    prefix[row_end][col_start] + 
                    prefix[row_start][col_start])
        
        def dfs(row_start, row_end, col_start, col_end):
            total = sum_region(row_start, row_end, col_start, col_end)
            area = (row_end - row_start) * (col_end - col_start)
            
            # If all 1s or all 0s
            if total == area or total == 0:
                return Node(total > 0, True, None, None, None, None)
            
            # Split and recurse
            row_mid = (row_start + row_end) // 2
            col_mid = (col_start + col_end) // 2
            
            return Node(
                True, False,
                dfs(row_start, row_mid, col_start, col_mid),
                dfs(row_start, row_mid, col_mid, col_end),
                dfs(row_mid, row_end, col_start, col_mid),
                dfs(row_mid, row_end, col_mid, col_end)
            )
        
        return dfs(0, n, 0, n)