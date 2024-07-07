class Solution:
    def toh(self, n, fromm, to, aux):
        if n == 1:
            print("Move disk 1 from rod " + str(fromm) + " to rod " + str(to))
            return 1
        
        moves = 0
        moves += self.toh(n - 1, fromm, aux, to)
        moves += 1
        print("Move disk " + str(n) + " from rod " + str(fromm) + " to rod " + str(to))
        moves += self.toh(n - 1, aux, to, fromm)
        return moves

if __name__ == "__main__":
    solution = Solution()
    n = 3  
    moves = solution.toh(n, 'A', 'C', 'B')
    print(f"Total number of moves: {moves}")
