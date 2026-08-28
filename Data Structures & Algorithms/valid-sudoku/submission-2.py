class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        def traversal(sr , er , sc , ec):
            
            s = set()
            for i in range(sr,er):
                for j in range(sc , ec):
                    cur = board[i][j]
                    if cur != ".":
                        if cur in s :
                            return False
                        s.add(cur)
            return True

        # validate rows :
        
        for r in range(9):
            s = set()
            for c in range(9):
                cur = board[r][c]
                if cur != ".":
                    if cur in s :
                        return False
                    s.add(cur)
        
        # validate cols :

        for r in range(9):
            s = set()
            for c in range(9):
                cur = board[c][r]
                if cur != ".":
                    if cur in s :
                        return False
                    s.add(cur)
        
        # validate each grid

        for sr in range(0,9,3):
            er = sr+3
            for sc in range(0,9,3):
                ec = sc+3
                if not traversal(sr , er , sc , ec):
                    return False
        
        return True