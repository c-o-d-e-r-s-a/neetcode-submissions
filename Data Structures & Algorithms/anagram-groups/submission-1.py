class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #This defaults a dictionary value to a list if a key is not found
        anagram_map = defaultdict(list)
        
        for s in strs:
            sorted_s = "".join(sorted(s))
        
            anagram_map[sorted_s].append(s)
            
        #Convert all the values to a list and return
        return list(anagram_map.values())