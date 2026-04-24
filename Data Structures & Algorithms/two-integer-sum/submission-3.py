class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = [i]
            else:
                d[num].append(i)

        print(d)
        for i, num in enumerate(nums):
            if target-num in d:
                if target-num == num:
                    if len(d[num]) > 1:
                        return [i, d[num][1]]
                else:
                    return [i, d[target-num][0]]
