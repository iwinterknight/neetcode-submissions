class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursive(l, r):
            if l > r:
                return -1
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return recursive(mid+1, r)
            return recursive(l, mid-1)

        def iterative():
            l, r = 0, len(nums)-1
            while l <= r:
                mid = l + (r-l) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        

        # return recursive(0, len(nums)-1)
        return iterative()