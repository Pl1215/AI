#graph for containing the edges and neighbors
class Graph:

    # Constructor
    def __init__(self, edges, N):
        self.adj = [[] for _ in range(N)]
        # to add edges and find neighbours of the graph
        for (source, dest) in edges:
            self.adj[source].append(dest)
            self.adj[dest].append(source)

        print("\nThe neighbours of the vertices: ")
        for i in range(N):
            print("{}: {}".format(i, self.adj[i]))
        print()

#bfs function to visit the nodes of the graph
def bfs(g,v,q,i):
    #queue to store the neighbor values
    q.append(i)
    v[i]=True
    while q:
        val=q.pop(0)
        print(val,end=" ")
        for j in g.adj[val]:
            if v[j] == False:
                q.append(j)
                v[j]=True


#No. of nodes
N = int(input("\nEnter the number of nodes: "))
# No. of graph edges
E=int(input("Enter the number of edges: "))

ed = []
#to get the edges of the graph
for i in range(E):
    k,l=input("Edge {}: ".format(i+1)).split(",")
    ed.append(tuple((int(k),int(l))))

start = int(input("\nStart node: "))

#The edges
print("\nThe edges are: ")
print(ed)

#To keep track of the visited nodes
v=[]
v=[False for i in range(N)]

# build a graph from the given edges
g = Graph(ed, N)

#starting point
i=start

print("BFS : \n")

q=[]
#call to bfs function
bfs(g,v,q,i)

#to know if the nodes have been visited or not
print("\n\nNODES VISITED: \n")
for i in range(N):
    print(str(i) + " : " + str(v[i]),end=" ")
print()


# v=[False for i in range(N)]
#
# print("\n\nDFS : \n")
# dfs(g, start, N)
#
# print("\n\nNODES VISITED: ")
# for i in range(N):
#     print(str(i) + " : " + str(v[i]),end=" ")
#
# print("\n\n")


