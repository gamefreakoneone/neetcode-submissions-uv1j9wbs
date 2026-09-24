class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for word in strs:
            key = sorted(word)
            grouped["".join(key)].append(word)

        results = []
        for key in grouped.keys():
            result = grouped[key]
            results.append(result)
        
        return results