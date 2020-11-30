class Solution:
    def isUnique(self, astr: str) -> bool:
        characters = []

        for ch in astr:
            for character in characters:
                if character == ch:
                    return False
            else:
                characters.append(ch)
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isUnique("abc"))
    print(set("leetcode"))
