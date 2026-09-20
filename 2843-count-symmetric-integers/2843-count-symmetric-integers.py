class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = []
        for num in range(low,high+1):
            i = str(num)
            n = len(i)
            if n%2 == 0:
                mid = len(i)//2
                first_sum  = sum(int(ch) for ch in i[:mid])
                sec = sum(int(ch) for ch in i[mid:])
                print(first_sum,sec)
                if first_sum == sec:
                    res.append(i)
        return len(res)