class Node:
    def __init__(self, edges):
        self.edges = edges
        self.dict = {}
        for start, end in self.edges:
            if start in self.dict:
                self.dict[start].append(end)
            else:
                self.dict[start] = [end]
            
            
    def getPath(self, start, end, path=[]):
        path = path + [start]
        
        if start == end:
            return [path]
        
        if start not in self.dict:
            return []
        
        paths = []
        for node in self.dict[start]:
            if node not in path:
                new_paths = self.getPath(node, end, path)
                for p in new_paths:
                    paths.append(p)
                    
        return paths
    
    
    def short(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        
        if start not in self.dict:
            return None
        
        short_path = None
        for node in self.dict[start]:
            if node not in path:
                new_path = self.short(node, end, path)
                if new_path:
                    if short_path is None or len(new_path) < len(short_path):
                        short_path = new_path
        return short_path

if __name__ == "__main__":
    routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto")
    ]
    graph = Node(routes)

    start = "Mumbai"
    end = "New York"

    print(f"Routes  between {start} and {end}: {graph.short(start, end)}")