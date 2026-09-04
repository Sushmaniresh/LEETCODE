class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_set = set("aeiou")
        
        # 1. Count frequencies and track the first occurrence of each vowel
        vowel_counts = Counter(c for c in s if c in vowels_set)
        first_occurrence = {}
        for idx, char in enumerate(s):
            if char in vowels_set and char not in first_occurrence:
                first_occurrence[char] = idx
        
        # 2. Build the min-heap
        # Format: (-frequency, first_occurrence_index, character)
        heap = []
        for char, count in vowel_counts.items():
            heapq.heappush(heap, (-count, first_occurrence[char], char))
            
        # 3. Rebuild the string
        result = []
        current_count = 0
        current_char = ""
        
        for char in s:
            if char in vowels_set:
                # If we haven't started using a vowel or the current one is exhausted
                if current_count == 0:
                    _, _, current_char = heapq.heappop(heap)
                    current_count = vowel_counts[current_char]
                
                result.append(current_char)
                current_count -= 1
            else:
                result.append(char)
                
        return "".join(result)

