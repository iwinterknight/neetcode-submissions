class MinStack:

    def __init__(self):
        self.st = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        self.min_val = min(self.min_val, val)
        self.st.append((val, self.min_val))
        
    def pop(self) -> None:
        self.st.pop()
        self.min_val = self.st[-1][1] if self.st else float('inf')

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]
