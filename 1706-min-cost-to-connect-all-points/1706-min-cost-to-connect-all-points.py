import heapq
def two_point_distance(point1,  point2) -> int:
    distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    return distance

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's Algorithm
        n = len(points)
        visited = []*n

        all_dis = {i:[] for i in range(n)} #distance, point
        for i in range(n):
            for j in range(i+1, n):
                dist = (two_point_distance(points[i], points[j]))
                all_dis[i].append([dist, j])
                all_dis[j].append([dist, i])
        
        result = 0
        min_heap = [[0,0]] # cost, point

        while len(visited) < n:
            cost, point = heapq.heappop(min_heap)
            if point in visited:
                continue 
            result += cost
            visited.append(point)
            for neighbor_cost, neighbor in all_dis[point]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, [neighbor_cost, neighbor])
        
        return result


        # Kruskal's algorithm 

        # all_dis = []
        # for i in range(n):
        #     for j in range(i+1, n):
        #         all_dis.append(two_point_distance(points[i], points[j]))
        # all_dis.sort()

        
        