class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        return (n % 2 == 0) and self.isPowerOfTwo(n // 2)


solution = Solution()

test_value = 16
result = solution.isPowerOfTwo(test_value)
print(f"Is {test_value} a power of two? {result}")
