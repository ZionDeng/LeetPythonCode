from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        a = []

        for pixels in A:
            a.append(pixels[::-1])
        for pixels in a:
            for i, pixel in enumerate(pixels):
                pixels[i] = 1 if pixel == 0 else 0

        return a


s = Solution()
print(s.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
