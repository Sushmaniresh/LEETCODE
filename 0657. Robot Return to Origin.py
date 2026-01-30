class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0 
        y = 0
        for i in moves:
            if i == 'U': x += 1
            elif i == 'D': x -= 1
            elif i == 'R': y += 2
            else: y -= 2
        return x == 0 and y == 0

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counter = Counter(moves)
        return counter['R'] == counter['L'] and counter['U']==counter['D']

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')



