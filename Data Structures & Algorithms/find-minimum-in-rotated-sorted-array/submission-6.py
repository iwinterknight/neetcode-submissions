class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        def linear_search():
            for i, num in enumerate(nums):
                prev, next = (i-1)%n, (i+1)%n
                if nums[prev] >= num and num <= nums[next]:
                    return num
        
        def binary_search(l, r):
            mid = l + (r-l) // 2
            num = nums[mid]
            if nums[l] <= nums[r]:
                return nums[l]
            if nums[l] <= num:
                return binary_search(mid+1, r)
            return binary_search(l, mid)

        return binary_search(0, n-1)
