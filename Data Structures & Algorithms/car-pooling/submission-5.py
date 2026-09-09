class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        heap=[]
        passengers=0
        for num,start,end in trips:
            while heap and heap[0][0]<=start:
                drop_end,drop_num=heapq.heappop(heap)
                passengers-=drop_num
            passengers+=num
            if passengers>capacity:
                return False
            heapq.heappush(heap,(end,num))
        return True



        