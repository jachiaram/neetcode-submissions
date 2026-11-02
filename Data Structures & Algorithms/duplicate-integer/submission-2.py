class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found_nums = {}
        for i in nums:
            if i in found_nums:
                return True;
            else:
                found_nums[i] = True;
        return False