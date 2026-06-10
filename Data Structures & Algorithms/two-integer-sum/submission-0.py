class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i in range(0 , len(nums)):
            value = nums[i]
            remaining = target - value
            if remaining in num_dict:
                return [num_dict[remaining], i]
            num_dict[value] = i