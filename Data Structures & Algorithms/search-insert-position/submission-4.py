class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l_idx = None
        def search(nums, l, r):
            nonlocal l_idx
            if l > r:
                if l_idx is None:
                    return 0
                return l_idx + 1
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l_idx = mid
                return search(nums, mid+1, r)
            else:
                return search(nums, l, mid-1)

        return search(nums, 0, len(nums)-1)