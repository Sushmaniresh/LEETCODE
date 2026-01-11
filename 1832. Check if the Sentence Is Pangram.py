class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence)<26: return False
        counter = Counter(sentence.lower())
        print(len(counter))
        if len(counter) >= 26: return True
        else: return False
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set(sentence)
        print(len(letters))
        if len(letters)==26: return True
        else: return False
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence))==26
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return set('abcdefghijklmnopqrstuvwxyz') <= set(sentence)
