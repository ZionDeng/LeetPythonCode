class RecentCounter:

    def __init__(self):
        self.nums = []

    def ping(self, t: int) -> int:
        # self.nums.append(t)
        # copy = self.nums.copy()
        # for num in self.nums:
        #     if num < t - 3000:
        #         copy.pop(0)
        #     else:
        #         return len(copy)

        # 这道题用for循环好像很吃内存
        while (len(self.nums) is not 0) and (self.nums[0] < t - 3000):
            self.nums.pop(0)
        return len(self.nums)


if __name__ == '__main__':
    count = RecentCounter()
    pings = [ 642, 1849, 4921, 5936, 5957]
    for ping in pings:
        print(count.ping(ping),end= " ")
