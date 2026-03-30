class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff],i]
            seen[num] = i 

sol = Solution().twoSum([3,4,5,6],7)
sol = Solution().twoSum([4,5,6],10)