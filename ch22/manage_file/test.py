class Myiter:
    def __init__(self,max):
        self.max = max
        self.current = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.max:
            raise StopIteration

        num = self.current
        self.current+=1
        return num


graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}


def dfs(node,visited = set()):
    if not node in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            dfs(i,visited)


dfs("A")