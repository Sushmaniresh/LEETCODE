class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
    
        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)
        
        return list(groups.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            anagram_map = defaultdict(list)
    
            for word in strs:
                count = [0] * 26
                for c in word:
                    count[ord(c) - ord('a')] += 1
                
                key = tuple(count)
                anagram_map[key].append(word)
            
            return list(anagram_map.values())
