import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:

        count = Counter(s)

        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)

        result = []

        prev_freq = 0
        prev_char = ""

        while heap:

            freq, char = heapq.heappop(heap)

            result.append(char)

            # Put previous character back
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))

            # Use current character once
            freq += 1

            # Current character becomes previous
            prev_freq = freq
            prev_char = char

        # If something is left unused,
        # rearrangement is impossible
        if prev_freq < 0:
            return ""

        return "".join(result)