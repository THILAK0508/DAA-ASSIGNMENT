class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 2 == 0:
            return self.numberOfSteps(num // 2) + 1
        else:
            return self.numberOfSteps(num - 1) + 1


solution = Solution()
test_cases = [14, 8, 123]

for num in test_cases:
    result = solution.numberOfSteps(num)
    print("Number of steps : ", result)
