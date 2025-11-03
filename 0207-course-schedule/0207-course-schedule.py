from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list) # quick setup my value as list
        visited = set()
        for c, p in prerequisites:
            prereq[c].append(p)
        
        # {1: [0], 0: [1]}
        def is_cycle(course):
            if course in visited:
                return True
            else: 
                visited.add(course)
                for p in prereq[course]:
                    if is_cycle(p):
                        return True
                prereq[course] = []
                visited.remove(course)
                return False
            return True

        for course in range(numCourses):
            if is_cycle(course):
                return False
        return True

        
        