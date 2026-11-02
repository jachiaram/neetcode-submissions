class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return_list = []
        found_nums = {}

        for i in range(0, len(nums)):
            if nums[i] in found_nums:
                return_list = [found_nums[nums[i]], i]
                break;
            else:
                found_nums[target - nums[i]] = i
        
        return return_list


