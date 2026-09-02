import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        N = len(points)
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1 , N):
                x2 , y2 = points[j]
                distance = abs(x1-x2) + abs(y1-y2)
                adj[i].append([distance , j])
                adj[j].append([distance, i])

        minHeap = []
        for distance, point in adj[0]:
            heapq.heappush(minHeap , [distance, 0 , point])

        visit = set()
        # mst = []
        min_cost = 0
        visit.add(0)
        while minHeap:
            distance , n1 , n2 = heapq.heappop(minHeap)
            if n2 in visit:
                continue

            visit.add(n2)
            min_cost+=distance
            for distance , neighbor in adj[n2]:
                if neighbor not in visit:
                    heapq.heappush(minHeap , [distance , n2 , neighbor])

        return min_cost