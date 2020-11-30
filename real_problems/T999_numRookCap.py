# 你现在可以控制车移动一次，
# 请你统计有多少敌方的卒处于你的捕获范围内
# （即，可以被一步捕获的棋子数）。
from typing import List


def findOne(line) -> int:
    if 'p' in line:
        if 'B' not in line:
            return 1
        else:
            if  line.index('B') > line.index('p'):
                return 1
    return 0



class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        result = 0
        for line in board:
            if "R" in line:
                loc_R = line.index("R")
                line_right = line[loc_R:]
                line_left = line[loc_R::-1]
                result += findOne(line_left)
                result += findOne(line_right)
        for line in zip(*board):
            if "R" in line:
                loc_R = line.index("R")
                result += findOne(line[loc_R:])
                result += findOne(line[loc_R::-1])
        return result


if __name__ == '__main__':
    s = Solution()
    # panel = [[".", ".", ".", ".", ".", ".", ".", "."],
    #          [".", ".", ".", "p", ".", ".", ".", "."],
    #          [".", ".", ".", "p", ".", ".", ".", "."],
    #          ["p", "p", ".", "R", ".", "p", "B", "."],
    #          [".", ".", ".", ".", ".", ".", ".", "."],
    #          [".", ".", ".", "B", ".", ".", ".", "."],
    #          [".", ".", ".", "p", ".", ".", ".", "."],
    #          [".", ".", ".", ".", ".", ".", ".", "."]]
    panel = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]


    print(s.numRookCaptures(panel))
