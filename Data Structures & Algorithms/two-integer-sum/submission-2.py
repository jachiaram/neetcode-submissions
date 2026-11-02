class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found_nums = {}

        for i in range(0, len(nums)):
            if nums[i] in found_nums:
                return [found_nums[nums[i]], i]
            else:
                found_nums[target - nums[i]] = i



