

class Graph:

    # Constructor
    def __init__(self, edges, N):
        self.adj = [[] for _ in range(N)]
        # to find adjacent vertices
        for source, dest in edges:
            self.adj[source].append(dest)
            self.adj[dest].append(source)
        print("\nThe neighbours of the vertices: ")
        for i in range(N):
            print("{}: {}".format(i,self.adj[i]))
        print()

#dfs funcction
def dfs(g,i,N):

    v[i]=True
    print(i)
    for j in g.adj[i]:
        if(v[j]==False):
            dfs(g,j,N)

N = int(input("Enter number of nodes: "))
E = int(input("Enter number of edges: "))
edges=[]
#edges
for ii in range(E):
    i,j=input("Edge {}: ".format(ii+1)).split(",")
    edges.append(tuple((int(i),int(j))))

start=int(input("Start node: "))


print("\nEdges are: " + str(edges))
g = Graph(edges, N)


#to know if visited
v=[]
v=[False for i in range(N)]

i=start

print("DFS: ")
#call to dfs
dfs(g,i,N)

#to know if the nodes have been visited or not
print("\n\nNODES VISITED: \n")
for i in range(N):
    print(str(i) + " : " + str(v[i]),end=" ")
print()









