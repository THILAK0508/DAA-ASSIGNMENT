from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bSearch(nums, low, high, targ):
            if high >= low:
                mid = low + (high - low) // 2
                if nums[mid] == targ:
                    return mid
                elif nums[mid] > targ:
                    return bSearch(nums, low, mid - 1, targ)
                else:
                    return bSearch(nums, mid + 1, high, targ)
            else:
                return -1
        return bSearch(nums, 0, len(nums) - 1, target)
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6]
    target = 4
    
    result = solution.search(nums, target)
    print(f"search({nums}, {target}) = {result}")
