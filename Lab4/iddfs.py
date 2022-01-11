from collections import defaultdict

class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def Dls(self, source, target, maxDepth):
		if source == target:
			return True
		if maxDepth < 0:
			return False

		for i in self.graph[source]:
			if self.Dls(i, target, maxDepth-1):
				return True
		return False

	def iddfs(self, source, target, maxDepth):
		for i in range(maxDepth):
			if self.Dls(source, target, i):
				return True
		return False

def path(source, target, maxdepth):
	graph = Graph(10)
	graph.addEdge(0, 1)
	graph.addEdge(0, 2)
	graph.addEdge(1, 3)
	graph.addEdge(1, 4)
	graph.addEdge(2, 5)
	graph.addEdge(2, 6)
	graph.addEdge(2, 7)
	graph.addEdge(3, 8)
	graph.addEdge(3, 9)

	if graph.iddfs(source, target, maxdepth):
		print("Path Exist")
	else:
		print("No Path")
    
path(0, 4, 3)
