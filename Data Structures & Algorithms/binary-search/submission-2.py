class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursive(nums, l, r):
            if l > r:
                return -1
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                 return recursive(nums, l, mid-1)
            else:
                return recursive(nums, mid+1, r)

        return recursive(nums, 0, len(nums)-1)