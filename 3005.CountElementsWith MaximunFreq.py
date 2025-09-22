class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_freq = max(counter.values())  # step 2: highest frequency
        total = sum(freq for freq in counter.values() if freq == max_freq)  # step 3
        return total