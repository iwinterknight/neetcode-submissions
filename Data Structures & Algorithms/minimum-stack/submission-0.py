class MinStack:
    import heapq
    def __init__(self):
        self.min_heap = []
        self.stack = []
        self.curr_len = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.curr_len += 1
        heapq.heappush(self.min_heap, (val, self.curr_len))

    def pop(self) -> None:
        for e, i in self.min_heap:
            if i == self.curr_len:
                self.min_heap.remove((e, i))
        heapq.heapify(self.min_heap)
        e = self.stack.pop()
        self.curr_len -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
           return self.min_heap[0][0]
