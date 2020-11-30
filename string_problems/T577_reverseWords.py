# Given a string,
# you need to reverse the order of characters in each word
# within a sentence while still preserving whitespace
# and initial word order.


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        result = ""
        for word in words:
            result += word[::-1] + " "
        return result[:-1]

        # return " ".join(i[::-1] for i in s.split())


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("Let's take LeetCode contest"))
