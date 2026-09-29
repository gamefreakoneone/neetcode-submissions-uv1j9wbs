class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for course, pre in prerequisites:
            adjList[course].append(pre)
        
        visited = set()
        def discover(course):
            if course in visited:
                return False
            preReq = adjList[course]
            if preReq == []:
                return True
            visited.add(course)
            for p_course in preReq:
                result = discover(p_course)
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