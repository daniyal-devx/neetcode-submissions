class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(row_start, row_end, col_start, col_end):
            # Check if all values in this region are the same
            first_val = grid[row_start][col_start]
            is_uniform = True
            
            for i in range(row_start, row_end):
                for j in range(col_start, col_end):
                    if grid[i][j] != first_val:
                        is_uniform = False
                        break
                if not is_uniform:
                    break
            
            # If uniform, create a leaf node
            if is_uniform:
                return Node(first_val == 1, True, None, None, None, None)
            
            # Otherwise, split into 4 quadrants
            row_mid = (row_start + row_end) // 2
            col_mid = (col_start + col_end) // 2
            
            topLeft = dfs(row_start, row_mid, col_start, col_mid)
            topRight = dfs(row_start, row_mid, col_mid, col_end)
            bottomLeft = dfs(row_mid, row_end, col_start, col_mid)
            bottomRight = dfs(row_mid, row_end, col_mid, col_end)
            
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
        
        n = len(grid)
        return dfs(0, n, 0, n)