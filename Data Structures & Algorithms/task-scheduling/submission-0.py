class Solution:
    import heapq
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = []
        queue = deque()

        task_freqs = Counter(tasks)
        for task, freq in task_freqs.items():
            heapq.heappush(max_heap, -freq)

        time = 0
        while max_heap or queue:
            time += 1

            if max_heap:
                freq = 1 + heapq.heappop(max_heap)
                if freq:
                    queue.append((freq, time + n))

            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        
        return time