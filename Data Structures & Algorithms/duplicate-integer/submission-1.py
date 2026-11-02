class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0,len(nums)):
            if i + 1 <= len(nums) - 1 and nums[i] == nums[i + 1]:
                return True
        return False