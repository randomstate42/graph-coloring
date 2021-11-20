class Dsatur:

    def __init__(self, G, lc=None):
        self.graph = G
        self.list_couleurs = [i for i in range(len(G))] if lc == None else lc 
        self.sat_degrees = {n : len(self.graph.elements[n]) for n in self.graph.elements.keys()}
        self.output = {}


    def colorer(self):
        colored = 0
        while colored<len(self.graph):
            noeud = max(
                self.sat_degrees,
                key= lambda n : (
                    self.sat_degrees[n], 
                    len(self.graph.elements[n])     
                )
            )
            neighbor_colors = [n.get_color() for n in self.graph.elements[noeud] ]

            for c in self.list_couleurs:
                if c not in neighbor_colors:
                    noeud.set_color(c)
                    if c not in self.output.keys():
                        self.output[c] = [noeud.element()]
                    else :
                        self.output[c].append(noeud.element()) 
                    self.sat_degrees[noeud] = 0
                    #del self.sat_degrees[noeud]
                    for n in self.graph.elements[noeud]:
                        if n.get_color() == None:
                            if colored == 0 or n.not_changed:
                                self.sat_degrees[n] = 1
                            else:
                                self.sat_degrees[n] += 1
                            if n.not_changed:
                                n.not_changed = False
                    break
            colored += 1
                  
        return self.output
        
