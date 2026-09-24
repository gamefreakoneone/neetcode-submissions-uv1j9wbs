import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted_nums = Counter(nums)
        maxHeap = []
        for key in counted_nums.keys():
            heapq.heappush(maxHeap , [-counted_nums[key] , key])
        results = []
        while k > 0:
            count , num = heapq.heappop(maxHeap)
            results.append(num)
            k -= 1

        return results