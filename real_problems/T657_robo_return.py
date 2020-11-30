class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y=0,0
        for move in moves:
            if move=="U":
                y+=1
            elif move=="D":
                y-=1
            elif move=="L":
                x-=1
            elif move=="R":
                x+=1
            else:
                return False
        return (x==0 and y==0)

        #  return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
s=Solution()
print(s.judgeCircle("UDLRRL"))