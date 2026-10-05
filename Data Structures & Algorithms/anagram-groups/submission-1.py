from collections import defaultdict
class Solution:
    # Add 'self' as the first parameter
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
                
            anagram_map[tuple(count)].append(s)
            
        return list(anagram_map.values())

