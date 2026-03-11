class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        # Convert to binary (remove '0b')
        binary = bin(n)[2:]
        
        # Flip bits
        flipped = ""
        for bit in binary:
            if bit == '0':
                flipped += '1'
            else:
                flipped += '0'
        
        # Convert back to integer
        return int(flipped, 2)
