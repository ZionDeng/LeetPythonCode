# 拼写单词
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        for word in words:
            if set(word) <= set(chars):
                can_spell = True
                for letter in word:
                    if word.count(letter) > chars.count(letter):
                        can_spell = False
                if can_spell:
                    result += len(word)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.countCharacters(["cat", "bt", "hat", "tree"], "atach"))
