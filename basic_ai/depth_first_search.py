# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:33:18 2021

@author: Arijit
"""


## The nodes in the graph ##
nodes = ['A' , 'B' , 'C' , 'D']

## The graph representation using edge list ##
graph = [('A' , 'B') , ('A' , 'C') , ('B' , 'A') , ('B' , 'C') ,
         ('B' , 'D') , ('C' , 'A') , ('C' , 'B') , ('D' , 'B')]

## Visited or not ##
visited = [False , False , False , False] 


## Depth First Search Algorithm ##
def dfs(current , nodes , graph , visited):
    
    ## Getting the current node index ##
    visit_node = nodes.index(current)
    
    ## Setting the neighbor nodes ##
    neighbor_nodes = []
    
    ## If the node is visited just skip ##
    if visited[visit_node] == True:
        return
    
    ## If node is not visited ##
    else:
        ## Print the current node ##
        print(current)
        
        ## Setting the visit to true ##
        visited[visit_node] = True
        for edge in graph:
            if edge[0] == current:
                
                ## Getting the neighboring node ##
                neighbor_nodes.append(edge[1])
        
        ## Move to next node ##
        for visit_next in neighbor_nodes: 
            dfs(visit_next , nodes , graph , visited)


## Test Case ##
dfs('A' , nodes , graph , visited)

    