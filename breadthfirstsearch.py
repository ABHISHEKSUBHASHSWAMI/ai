#Abhishek Subhash Swami 21 AIML
#Program for breadth first search

tree={
    'A':['B','C','D'],
    'B':['E'],
    'C':['F','G'],
    'D':['H'],
    'E':['I','J'],
    'F':[],
    'G':[],
    'H':['K'],
    'I':[],
    'J':[],
    'K':[]
}

#create visited list and queue list
visited=[]
queue=[]

def bfs(visited,queue,node):
    visited.append(node)
    queue.append(node)

    while queue:
        m=queue.pop(0)
        print(m,end=" ")

        for neighbour in tree[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

#main
print("Following is breadth first Search :\n")
bfs(visited,queue,"A")