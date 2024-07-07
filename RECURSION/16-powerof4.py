class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 4 != 0:
            return False
        return self.isPowerOfFour(n // 4)

solution = Solution()

test_value = 64
result = solution.isPowerOfFour(test_value)
print(f"Is {test_value} a power of four? {result}")
