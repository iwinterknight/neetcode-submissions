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

        def iterative(nums):
            l, r = 0, len(nums)-1
            while l <= r:
                mid = l + (r-l) // 2
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            return -1

        # return recursive(nums, 0, len(nums)-1)
        return iterative(nums)