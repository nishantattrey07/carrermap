import webbrowser
from pyvis.network import Network
import networkx as nx
nodes=[]
edges=[]
nodesize=[]
def getdata(fname):
    f=open(fname,"r")
    l=f.read().split('\n')
    for x in l:
        x=x.split('-')
        z=x[0]
        if z not in nodes and z[0] not in "123":
            nodes.append(z)
            nodesize.append(4)
        for y in x[1][1:-1].split(','):
            k = z[1:] if z[0] in '123' else z
            if not ((k,y) in edges or (y,k) in edges or k==y):
                edges.append((k,y))
            if y not in nodes:
                nodes.append(y)
                nodesize.append(4)
                if z[0] in "123":
                    nodesize[nodes.index(y)]=int(z[0])
    nodesize[0]=7
getdata("cyber1.txt")
net = Network("840px", "100%", bgcolor="black", font_color="white")
net.force_atlas_2based()
net.add_nodes(nodes, value=nodesize,color=["grey"]*len(nodes))
net.add_edges(edges)
net.show("proj.html")
webbrowser.open('proj.html')