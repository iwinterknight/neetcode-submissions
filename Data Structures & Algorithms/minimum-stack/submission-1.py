class MinStack:

    def __init__(self):
        self.st = []
        self.hp = []
        self.n = 0

    def push(self, val: int) -> None:
        self.st.append(val)
        self.n += 1
        heapq.heappush(self.hp, (val, self.n))

    def pop(self) -> None:
        for e, i in self.hp:
            if i == self.n:
                self.hp.remove((e, i))
        heapq.heapify(self.hp)
        self.st.pop()
        self.n -= 1

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.hp[0][0]
