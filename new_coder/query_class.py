# 班级分数查询
# input:
# 5 7
# 1 2 3 4 5
# Q 1 5
# U 3 6
import sys


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    results = list(map(int, input().split()))
    for line in sys.stdin:
        cmd = line.split()
        a, b = int(cmd[1]), int(cmd[2])
        if cmd[0] == 'Q':
            print(max(results[a - 1: int(b)]))
        if cmd[0] == 'U':
            # 更新命令
            results[a-1] = b
