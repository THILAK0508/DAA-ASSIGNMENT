class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n == -1:
            return 1/x
        
        if n == 1:
            return x

        return self.myPow(x*x, n//2) * self.myPow(x, n % 2)

if __name__ == "__main__":
    solution = Solution()

    x, n = 2.0, 10  
    
    result = solution.myPow(x, n)
    print(f"myPow({x}, {n}) = {result}")
