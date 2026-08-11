class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted  = Counter(nums)
        reversed_counts = defaultdict(list)

        for num, count in counted.items():
            reversed_counts[count].append(num)
        
        highest_freq = max(reversed_counts)
        results = []
        while highest_freq >= 0:
            if highest_freq in reversed_counts:
                results.extend(reversed_counts[highest_freq])

                if len(results) >= k:
                    return results[:k]

            highest_freq -= 1
        
        return results