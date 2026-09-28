class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for a ,b in prerequisites:
            adjList[a].append(b)

        visited = set()

        def discover(course):
            if course in visited:
                return False
            preReq = adjList[course]
            if preReq == []:
                return True
            visited.add(course)
            for c in preReq:
                result = discover(c)
                if not result:
                    return False
            visited.remove(course)
            adjList[course] = []
            return True
        
        for i in range(numCourses):
            result = discover(i)
            if not result:
                return False
        
        return True