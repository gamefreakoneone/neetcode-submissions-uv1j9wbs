import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        listNodes = []
        for s ,d, w in times:
            adjList[s].append([d,w])
            listNodes.append(s)

        shortest = {}
        minHeap = [[0, k]]

        while minHeap:
            w1 , n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            for n2, w2 in adjList[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1+w2 , n2])

        
        return max(shortest.values()) if len(shortest) == n else -1