class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count frequencies of each character
        counts = collections.Counter(s)
        
        # Python heap is a min-heap by default; use negative counts to simulate a max-heap
        max_heap = [[-count, char] for char, count in counts.items()]
        heapq.heapify(max_heap)
        
        # Check if the most frequent character exceeds the possible limit
        if -max_heap[0][0] > (len(s) + 1) // 2:
            return ""
            
        res = []
        prev_count, prev_char = 0, ""
        
        while max_heap:
            # Pop the most frequent character remaining
            count, char = heapq.heappop(max_heap)
            res.append(char)
            
            # If the previously used character still has remaining count, push it back
            if prev_count < 0:
                heapq.heappush(max_heap, [prev_count, prev_char])
                
            # Update the "on hold" pointer with the current character decremented
            prev_count = count + 1  # Adding 1 moves it closer to 0 since counts are negative
            prev_char = char
            
        return "".join(res)
            