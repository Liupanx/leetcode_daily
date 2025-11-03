"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def clone_helper(self, node, visited):
        if node in visited:
            return visited[node]
        new_node = Node(node.val)
        visited[node] = new_node
        for nei in node.neighbors:
            new_node.neighbors.append(self.clone_helper(nei, visited))
        return new_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return
        visited = {}
        return self.clone_helper(node, visited)
        