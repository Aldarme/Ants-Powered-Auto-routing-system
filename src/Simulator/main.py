'''
Created on 27 avr. 2020

@author: promet
'''

from Graph.Vertex import Vertex
from Graph.Edge import Edge
from Graph.Numerotation import Numerotation

if __name__ == '__main__':
    print("test")
    beg = Vertex("Belfort")
    end = Vertex("Vienne")
    
    edg = Edge(380, beg, end)
    
    print(beg.get_ID())
    print(end.get_ID())
    print("{},{},{}".format(edg.get_lgth(), edg.get_vtx_in().get_ID(), edg.get_vtx_out().get_ID()))
    
    Num = Numerotation()
    Num.add_element(beg)
    Num.add_element(end)
    
    print("{}".format(Num.size()))
    print("{}".format(Num.get_vtxPos(beg)))
    print("{}".format(Num.get_vtxPos(end)))
  
    print("{}".format(Num.get_vtxAt(0)))
    print("{}".format(Num.get_vtxAt(1)))
    
    print("{}".format(Num.get_vtxArray()))
    for vtx in Num.get_vtxArray():
        print(vtx.get_ID())
    
    #To debug AdjMtx
    
else:
    print("the file is not the main")