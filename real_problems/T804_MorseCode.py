from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {'a': '.-', 'b': '-...', 'c': '-.-.',
                 'd': '-..', 'e': '.', 'f': '..-.',
                 'g': '--.', 'h': '....', 'i': '..',
                 'j': '.---', 'k': '-.-', 'l': '.-..',
                 'm': '--', 'n': '-.', 'o': '---',
                 'p': '.--.', 'q': '--.-', 'r': '.-.',
                 's': '...', 't': '-', 'u': '..-',
                 'v': '...-', 'w': '.--', 'x': '-..-',
                 'y': '-.--', 'z': '--..',
                 }
        diffs = []
        for word in words:
            for char in word:
                word = word.replace(char, morse.get(char))
            if word not in diffs:
                diffs.append(word)
        # for diff in diffs:
        #     print(diffs.count(diff))
        #     if diffs.count(diff)>1:
        #         diffs.remove(diff)

        return len(diffs)


s = Solution()
print(s.uniqueMorseRepresentations(["rwjje","aittjje","auyyn","lqtktn","lmjwn"]))
