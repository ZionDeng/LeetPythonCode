#
# Given numBottles full water bottles,
# you can exchange numExchange empty water bottles for one full water bottle.
# The operation of drinking a full water bottle turns it into an empty bottle.
# Return the maximum number of water bottles you can drink.
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        while numBottles >= numExchange:
            result += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.numWaterBottles(2,3))
