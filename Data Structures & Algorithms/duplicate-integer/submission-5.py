class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True

var = Solution().hasDuplicate([1, 2, 3, 3])