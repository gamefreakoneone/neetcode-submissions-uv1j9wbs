class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #Creating a dictionary with list within
        for word in strs:
            key = tuple(sorted(word))
            result[key].append(word)
        
        return list(result.values())