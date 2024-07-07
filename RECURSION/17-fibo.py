class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)

solution = Solution()

n = 10
result = solution.fib(n)
print(f"The {n}th Fibonacci number is {result}")
