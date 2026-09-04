class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for c , p in prerequisites:
            adjList[c].append(p)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False # We have reached a cycle

            if adjList[crs] == []:
                return True # NO prerequisities

            visiting.add(crs)
            for p_crs in adjList[crs]:
                if not dfs(p_crs):
                    return False
            visiting.remove(crs)
            adjList[crs] = [] # Since all prerequisites returned True
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
                