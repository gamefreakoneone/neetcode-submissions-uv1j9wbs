class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted_numbers = Counter(nums)
        count_dict = defaultdict(list)

        for num, count in counted_numbers.items():
            count_dict[count].append(num)
        
        highest_freq = max(count_dict)
        result = []

        while highest_freq> 0:
            if highest_freq in count_dict:
                result.extend(count_dict[highest_freq])

                if len(result) >=k:
                   return result[:k]
            
            highest_freq -= 1

        return result