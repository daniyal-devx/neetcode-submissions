class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
       rows,cols=len(matrix),len(matrix[0])
       self.sumMat=[[0]*(cols+1) for _ in range(rows+1)]
       for i in range(rows):
        for j in range(cols):
            self.sumMat[i+1][j+1]=(matrix[i][j]
            +self.sumMat[i][j+1]
            +self.sumMat[i+1][j]
            -self.sumMat[i][j])
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,r2,c1,c2=row1+1,row2+1,col1+1,col2+1
        return (self.sumMat[r2][c2]
        -self.sumMat[r1-1][c2]
        -self.sumMat[r2][c1-1]
        +self.sumMat[r1-1][c1-1])
       
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)