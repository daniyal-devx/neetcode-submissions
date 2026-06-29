class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes={}
        rows={}
        cols={}
        for i in range(len(board)):
            for j in range(len(board[0])):
                val=board[i][j]
                if val==".":
                    continue
                r=i//3
                c=j//3
                box_no=r*3+c
                if i not in rows:   rows[i]=set()
                if j not in cols:   cols[j]=set()
                if box_no not in boxes: boxes[box_no]=set()
                if val in rows[i] or val in cols[j] or val in boxes[box_no]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_no].add(val)
        return True
                  


        