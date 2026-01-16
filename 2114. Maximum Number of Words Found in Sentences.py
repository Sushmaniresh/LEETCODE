class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for i in sentences:
            a = len(i.split())
            ans = max(ans,a)
        return ans
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = 0
        for sentence in sentences:
            word_count = len(sentence.split(" "))
            if word_count > result:
                result = word_count
        return result