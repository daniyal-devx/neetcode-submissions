class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks=[(enqueue,processing,i) for i,(enqueue,processing) in enumerate(tasks)]
        tasks.sort()
        heap=[]
        result=[]
        time=0
        i=0
        n=len(tasks)
        while i<n or heap:
            if not heap and time<tasks[i][0]:
                time=tasks[i][0]
            while i < n and tasks[i][0]<=time:
                enqueue,processing,index=tasks[i]
                heapq.heappush(heap,(processing,index))
                i+=1
            processing,index=heapq.heappop(heap)
            result.append(index)
            time+=processing
        return result

        
        