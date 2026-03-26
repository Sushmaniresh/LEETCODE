class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1   # check last bit
            n = n >> 1       # shift right
        return count
