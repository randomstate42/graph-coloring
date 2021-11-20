class Noeud:
        __slots__ = '_element', '_couleur', 'not_changed'
        
        def __init__(self, element):
            self._element = element
            self._couleur = None
            self.not_changed = True

        def element(self):
            return self._element

        def get_color(self):
            return self._couleur

        def set_color(self, c):
            self._couleur =  c
            
        def __hash__(self):
            return hash(id(self._element))

"""class Arc:
        __slots__ = '_elements'        
        
        def __init__(self, u, v):
            self._elements = (u, v)
        
        def element(self):
            return self._elements 
            
        def __eq__(self, other):
            rev_other = other[::-1]
            return self._elements == other.elements() or self._elements == rev_other"""

class Graph:
            
    def __init__(self):
        self.elements = {}

    def __len__(self):
        return len(self.elements)
    
    """def nbre_arcs(self):
        total = sum(len(self.elements[n]) for n in self.elements)
        return total//2"""
    
    def inserer_noeud(self, n):
        noeud = Noeud(n)
        self.elements[noeud] = []

    def insertion_noeuds(self, noeuds):
        for n in noeuds:
            self.inserer_noeud(n)
    
    def ajouter_arc(self, u, v):
        #arc = Arc(u, v)
        n1, n2 = None, None
        for n in self.elements:
            if n.element() == u:
                n1 = n
            elif n.element() == v:
                n2 = n
            if n1 and n2:
                break
        if not (n1 and n2):
            raise NoeudException
        self.elements[n1].append(n2)
        self.elements[n2].append(n1)

    def ajout_arcs(self, arcs):
        for arc in arcs:
            n1, n2 = arc
            self.ajouter_arc(n1, n2)

    def degree(self, n):
        return len(self.elements[n])

class NoeudException(Exception):
    "utiliser lorsque le noeud n'est pas trouvé dans le graphe"