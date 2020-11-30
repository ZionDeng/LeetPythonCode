# Alice and Bob take turns playing a game, with Alice starting first.
# Initially, there is a number N on the chalkboard. 
#  On each player's turn, that player makes a move consisting of:
# Choosing any x with 0 < x < N and N % x == 0.
# Replacing the number N on the chalkboard with N - x.
# Also, if a player cannot make a move, they lose the game.
# Return True if and only if Alice wins the game,
# assuming both players play optimally.
class Solution:
    def divisorGame(self, N: int) -> bool:
        # # x用公约数判断
        # # Alice = not Bob , alice = not self(n-x)

        # # 如果是1 返回false
        # result = False
        # if N == 1:
        #     return False

        # # 不是1 ：
        # for x in range(1, int(N ** 0.5) + 1):
        #     if N % x == 0:
        #         # 找到每一个x，递归
        #         if not self.divisorGame(N - x):
        #             result = True
        # return result

        # 偶数必胜：
        return not (N & 1)


if __name__ == '__main__':
    s = Solution()
    for x in range(1, 10):
        print(s.divisorGame(x), "是%d的结果" % x)
