# Given a List of words,
# return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        result = []
        for i in words:
            a= i.lower()
            print(a,i)
            if set(i) <= set1 or set(i) <= set2 or set(i) <= set3:
                result.append(i)

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.findWords(['hello', 'alaska', 'dad', 'Peace']))
