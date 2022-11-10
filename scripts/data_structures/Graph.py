import time

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.dict = {}
        for start, end in self.edges:
            if start in self.dict:
                self.dict[start].append(end)
            else:
                self.dict[start] = [end]
            
    # Returns all the links between two nodes.        
    def get_links(self, start, end, link=[]):
        link = link + [start]
        
        if start == end:
            return [link]
        
        if start not in self.dict:
            return []
        
        links = []
        for node in self.dict[start]:
            if node not in link:
                n_link = self.get_links(node, end, link)
                for l in n_link:
                    links.append(l)
                    
        return links
    
    # Returns the shortest link between two nodes.
    def shortest_link(self, start, end, link=[]):
        link = link + [start]
        
        if start == end:
            return link
        
        if start not in self.dict:
            return None
        
        short_link = None
        for node in self.dict[start]:
            if node not in link:
                new_link = self.shortest_link(node, end, link)
                if new_link:
                    if short_link is None or len(new_link) < len(short_link):
                        short_link = new_link
        return short_link

# Demo of Routes from places to places in Nigeria.
if __name__ == "__main__":
    print("This is a graph demo from ifunanyaScript\n")
    time.sleep(1)
    routes = [
    ("Ikeja", "Abeokuta"),
    ("Onitsha", "Asaba"),
    ("Benin", "Lokoja"),
    ("Ikeja", "Ibadan"),
    ("Ibadan", "Ilorin"),
    ("Lokoja", "Abuja"),
    ("Ado Ekiti", "Abuja"),
    ("Onitsha", "Ikeja"),
    ("Abeokuta", "Oshogbo"),
    ("Oshogbo", "Ado Ekiti"),
    ("Ilorin", "Abuja"),
    ("Ikeja", "Lokoja"),
    ("Abuja", "Onitsha"),
    ("Ilorin", "Minna")
    ]
    
    graph = Graph(routes)

    start = "Ikeja"
    end = "Abuja"
    print(f"Routes from {start} to {end}: ")
    for route in graph.get_links(start, end):
        print(list(route))
    print("_"*54)
    time.sleep(1)
    print(f"\nShortest route from {start} to {end}: ")
    print(graph.shortest_link(start, end))
    print("_"*35)
    
    start = "Abuja"
    end = "Ikeja"
    time.sleep(1)
    print(f"\nRoutes from {start} to {end}: ")
    for route in graph.get_links(start, end):
        print(list(route))
    print("_"*29)
    
    start = "Ibadan"
    end = "Minna"
    time.sleep(1)
    print(f"\nRoutes from {start} to {end}: ")
    for route in graph.get_links(start, end):
        print(list(route))


# ifunanyaScript 