class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)
        for a, b in prerequisites:
            prereqs[a].append(b)

        state = [0] * numCourses
        order: List[int] = []

        def dfs(u: int) -> bool:
            if state[u] == 1:   
                return False
            if state[u] == 2: 
                return True

            state[u] = 1
            for p in prereqs[u]:
                if not dfs(p):
                    return False
            state[u] = 2
            order.append(u) 
            return True

        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return []  

        return order

        