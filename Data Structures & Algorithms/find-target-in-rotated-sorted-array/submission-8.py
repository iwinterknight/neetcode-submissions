class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        def binary_search(l, r):
            if l > r:
                return -1
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    return binary_search(l, mid-1)
                else:
                    return binary_search(mid+1, r)
            elif nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    return binary_search(mid+1, r)
                else:
                    return binary_search(l, mid-1)

        return binary_search(l, r)
            