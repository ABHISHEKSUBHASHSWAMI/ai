#Abhishek Subhash Swami 21 AIML
#Program for depth first search


#generate tree using dictionary 
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

#create a set for storing visited node
visited=set()

#define a function dfs 

def dfs(tree,visited,node):
    if node not in visited:                     #check if node is visited or not
        print(node)
        visited.add(node)                       #add node to visited
        for neighbour in tree[node]:            #traverse neighbour 
            dfs(tree,visited,neighbour)         #call dfs recursively


#main
print("Folllowing is depth first search :\n")
dfs(tree,visited,'A')
