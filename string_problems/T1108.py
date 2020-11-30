class Solution:
    def defangIPaddr(self, address: str) -> str:

        array = address.split(".")

        return "[.]".join(str(i) for i in array)


solution = Solution()
print(solution.defangIPaddr("1.1.1.1"))
