class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                result.extend(self.twoSum(nums, i))
        return result

    def twoSum(self, nums, i):
        partial_result = []
        low, high = i + 1, len(nums) - 1
        while low < high:
            s = nums[i] + nums[low] + nums[high]
            if s == 0:
                partial_result.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
                while low < high and nums[high] == nums[high + 1]:
                    high -= 1
            elif nums[i] + nums[low] + nums[high] < 0:
                low += 1
            else:
                high -= 1
        return partial_result