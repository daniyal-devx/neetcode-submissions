class Solution:
    def reorganizeString(self, s: str) -> str:
        freq=Counter(s)
        n=len(s)
        max_count=max(freq.values())
        if max_count>(n+1)//2:
            return ""
        heap=[(-count, char) for char,count in freq.items()]
        heapq.heapify(heap)
        result=[]
        prev_char=''
        prev_count=0
        while heap:
            count, char = heapq.heappop(heap)
            result.append(char)
            count+=1
            if prev_count<0:
                heapq.heappush(heap,(prev_count,prev_char))
            prev_char=char
            prev_count=count
        return ''.join(result)

