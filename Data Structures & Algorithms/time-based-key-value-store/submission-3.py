class TimeMap:

    def __init__(self):
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = [(timestamp, value)]
        else:
            self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.cache.get(key, None)
        result = ""
        if arr:
            l, r = 0, len(arr)-1
            while l <= r:
                mid = l + (r-l) // 2
                if arr[mid][0] <= timestamp:
                    result = arr[mid][1]
                    l = mid + 1
                else:
                    r = mid - 1
        return result