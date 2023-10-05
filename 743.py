class HeapNode:
    def __init__(self,val: (int,int)):
        self.val = val
        self.node = val[0]
        self.min_dist = val[1]

    def __lt__(self,other):
        return self.min_dist < other.min_dist


class Neighbour:
    def __init__(self, index, edge_wt):
        self.index = index
        self.edge_wt = edge_wt


class Graph:
    def __init__(self, adj):
        self.adjacency_list = adj
        self.graph_size = len(adj)
        self.visited = set()
        self.min_distance = {}
        self.heap = []

    def shortest_path(self,source_node):
        current_node = source_node
        self.min_distance[current_node] = 0

        heapq.heappush(self.heap,HeapNode((source_node,0)))

        while(self.heap):
            current_heap_node = heapq.heappop(self.heap)
            current_node = current_heap_node.node
            current_dist = current_heap_node.min_dist
            if current_node in self.visited:
                continue
            self.visited.add(current_node)
            self.min_distance[current_node] = current_dist
            for n in self.adjacency_list[current_node]:
                heapq.heappush(self.heap, HeapNode((n.index, current_dist+n.edge_wt)))

    def min_dist(self):
        if len(self.min_distance.keys()) < self.graph_size:
            return -1
        ans = 0
        for dist in self.min_distance.values():
            ans = max(ans,dist)
        return ans

            
        

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        
        for i in range(1,n+1):
            adj[i] = []
        for item in times:
            adj[item[0]].append(Neighbour(item[1],item[2]))
        
        

        graph = Graph(adj)
        graph.shortest_path(k)
        return graph.min_dist()

