class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, r):
            if l > r:
                return -1
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[l] <= nums[mid]:
                    if nums[l] <= target and target < nums[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] <= nums[r]:
                    if nums[mid] < target and target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid - 1
                return binary_search(l, r)
        return binary_search(0, len(nums)-1)


            