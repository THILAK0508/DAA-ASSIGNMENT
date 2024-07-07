class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        return self.isPowerOfThree(n // 3)


solution = Solution()

test_value = 27
result = solution.isPowerOfThree(test_value)
print(f"Is {test_value} a power of three? {result}")
