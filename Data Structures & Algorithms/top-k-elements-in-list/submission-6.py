class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = Counter(nums)
        counted_freq = defaultdict(list)

        # Now we are flipping the numbers and counts
        for num, count in counted.items(    ):
            counted_freq[count].append(num)

        highest_freq = max(counted_freq)
        result = []

        while k > 0:    
            if highest_freq not in counted_freq:
                highest_freq -= 1
                continue
            result.extend(counted_freq[highest_freq])
            length = len(counted_freq[highest_freq])
            k -= length
            highest_freq -= 1

        return result
