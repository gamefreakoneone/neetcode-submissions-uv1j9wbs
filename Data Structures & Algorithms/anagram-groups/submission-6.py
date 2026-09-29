class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        for word in strs:
            sorted_word = sorted(word)
            key = "".join(sorted_word)
            if key not in dictionary:
                dictionary[key] = []
            dictionary[key].append(word)

        result = []
        for key in dictionary.keys():
            result.append(dictionary[key])

        return result