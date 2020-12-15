# https://leetcode-cn.com/problems/reorder-data-in-log-files/
class Solution:
    def reorderLogFiles(self, logs):
        l1, l2 = [],[]
        for i in logs:
            if i[-1].isdigit():
                l2.append(i)
            else:
                l1.append(i)
        l1.sort(key = lambda x:(x[x.index(' ')+1:],x[:x.index(' ')+1])) 
        # according to the regulation discribed in the question 
        return l1 + l2 

s = Solution()
print(s.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
