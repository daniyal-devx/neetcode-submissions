class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count =Counter(tasks)
        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)

        q = deque()

        time = 0

        while heap or q:

            time += 1
            if q and q[0][1] == time:
                freq = q.popleft()[0]
                heapq.heappush(heap, freq)

            if heap:
                freq = heapq.heappop(heap)

                freq += 1  

                if freq != 0:
                    q.append((freq, time + n + 1))

        return time
        