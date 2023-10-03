class HeapNode:
    def __init__(self,val: (int,int)):
        self.val = val

    def __lt__(self,other):
        return self.val[1] < other.val[1]

    def print_node(self):
        print(self.val[0], self.val[1])


class Node:
    def __init__(self):
        self.index = 0
        self.min_distance = 0

class Graph:
    def __init__(self, adj: {}, source_node: int):
        self.adjacency_list = adj
        self.graph_size = len(adj)
        self.heap = []
        self.visited = set()
        self.heap = []
        heapq.heappush(self.heap,HeapNode((source_node,0)))

        heapq.heappush(self.heap,HeapNode((source_node,-1)))
        heapq.heappush(self.heap,HeapNode((source_node,1)))



    def showHeap(self):
        print("heap is ")
        self.heap[0].print_node()
        self.heap[1].print_node()        
        self.heap[2].print_node()

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        
        for i in range(1,n+1):
            adj[i] = []
        for item in times:
            adj[item[0]].append((item[1],item[2]))
        
        graph = Graph(adj, 0)
        graph.showHeap()
        return 0
