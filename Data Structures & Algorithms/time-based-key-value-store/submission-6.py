class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # greatest element lte
        def bisect_right_iterative(arr):
            nonlocal res
            l, r = 0, len(arr)-1
            while l <= r:
                mid = l + (r-l) // 2
                if arr[mid][0] <= timestamp:
                    res = arr[mid][1]
                    l = mid + 1 
                else:
                    r = mid - 1
            return res

        arr = self.cache.get(key, None)
        if arr:
            res = bisect_right_iterative(arr)
        return res