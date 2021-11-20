from graph import Graph
from dsatur import Dsatur

print("##################### exemple 1 ###################")
g = Graph()
g.insertion_noeuds([0,1,2,3,4,5])
g.ajout_arcs([(0,1),(0,2),(0,3),(1,3),(1,4),(2,3),(2,5),(3,4),(3,5),(4,5)])
print(f"nbre de noeuds {len(g)}")
d = {n.element() : len(g.elements[n]) for n in g.elements.keys()}
print(f"noeuds et degrés {d}")
ds = Dsatur(g)
out = ds.colorer()
print(f"nbre de couleurs utilisées {len(out)}")
print(f"couleurs et noeuds {out}")

print("##################### exemple 2 ####################")
g1 = Graph()
g1.insertion_noeuds([1,2,3,4,5,6,7,8,9,10,11])
g1.ajout_arcs([(1,2),(1,3),(1,4),(2,3),(2,4),(3,4),(3,8),(4,5),(4,6),(4,7),(5,6),(5,7),(6,7),(6,8),(6,10),(7,11),(8,10),(9,10)])
print(f"nbre de noeuds {len(g1)}")
d1 = {n.element() : len(g1.elements[n]) for n in g1.elements.keys()}
print(f"noeuds et degrés {d1}")
ds1 = Dsatur(g1)
out1 = ds1.colorer()
print(f"nbre de couleurs utilisées {len(out1)}")
print(f"couleurs et noeuds {out1}")
