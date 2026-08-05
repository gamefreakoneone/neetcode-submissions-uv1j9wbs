class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in results:
                results[key] = []
            results[key].append(word)
        final_result = []
        for values in results.values():
            final_result.append(values)
        return final_result