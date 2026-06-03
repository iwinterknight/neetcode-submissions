class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def binary_search(l, r):
            if l > r:
                return False
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return True
            else:
                while l < mid and nums[l] == nums[mid]:
                    l += 1
                while mid < r and nums[r] == nums[mid]:
                    r -= 1
                if nums[l] <= nums[mid]:
                    if nums[l] <= target < nums[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] <= nums[r]:
                    if nums[mid] < target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid - 1
                return binary_search(l, r)
        
        return binary_search(0, len(nums)-1)