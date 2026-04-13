class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted_numbers = Counter(nums)
        freq_bucket = defaultdict(list)

        for num , count in counted_numbers.items():
            freq_bucket[count].append(num)

        result = []
        highest_freq = max(freq_bucket) # Apparently max checks the keys and not tis values

        while k > 0:
            if highest_freq  not in freq_bucket:
                highest_freq -=  1
                continue
            result.extend(freq_bucket[highest_freq])
            size_arr = len(freq_bucket[highest_freq])
            k -= size_arr
            highest_freq -= 1
        
        return result