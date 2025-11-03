from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        for c, p in prerequisites:
            prereqs[c].append(p)
            
        def cycle(course, visited):
            if course in visited:
                return True
            visited.add(course)
            for p in prereqs[course]:
                if cycle(p, visited):
                    return True
            prereqs[course] = []
            visited.remove(course)
            return False

        visited = set()
        for course in range(numCourses):
            if cycle(course, visited):
                return False
        return True