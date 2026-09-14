class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        max_heap = []
        i = 0
        n = len(projects)
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                required_capital, profit = projects[i]
                heapq.heappush(max_heap, -profit)
                i += 1

            if not max_heap:
                break

            w += -heapq.heappop(max_heap)

        return w