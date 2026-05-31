class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l_idx = None
        def binarysearch(nums, l, r):
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
                return binarysearch(nums, mid+1, r)
            else:
                return binarysearch(nums, l, mid-1)

        def boundarysearch_recursive(l, r):
            if l >= r:
                return l
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return boundarysearch_recursive(mid+1, r)
            else:
                return boundarysearch_recursive(l, mid)


        # return binarysearch(nums, 0, len(nums)-1)
        return boundarysearch_recursive(0, len(nums))