# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 00:47:59 2021

@author: Arijit
"""
import math

def explore_neighbor(current_node , current_dist, graph , visited , prior_list):
    neighbor_node = graph[current_node]
    
    prior_nodes = [prior[0] for prior in prior_list]
    prior_dist = [prior[1] for prior in prior_list]
    
    for node , dist in neighbor_node:
        
        if ((visited[node] == False) and (node not in prior_nodes)):
            prior_list.append((node , current_dist + dist))
            
        elif node in prior_nodes:
            node_idx = prior_nodes.index(node)
            if prior_dist[node_idx] > (dist + current_dist):
                prior_list.remove((node , prior_dist[node_idx]))
                prior_list.append((node , current_dist + dist))

def lazy_djikstra(g , nodes , start , end):
    
    ## Set visited dictionary
    visited = {}
    for node in nodes:
        visited[node] = False
    
    ## Setting the initial distance to infinity
    dist = {}
    for node in nodes:
        dist[node] = math.inf
    
    ## Setting the distance of start node as 0
    dist[start] = 0
    
    ## Setting the priority list
    prior_list = [(start , 0)]
    
    ## Looping over and calculating the distances
    while len(prior_list) != 0:
        print(prior_list)
        visit_node = prior_list.pop(0)
        dist[visit_node[0]] = min(dist[visit_node[0]] , visit_node[1])
        visited[visit_node[0]] = True
        if visit_node[0] == end:
            break
        explore_neighbor(visit_node[0] , visit_node[1] , graph , visited , prior_list)
        prior_list = sorted(prior_list , key = lambda prior : prior[1])
    

    return dist

graph = {'A' : [('B' , 1) , ('C' , 2)],
         'B' : [('D' , 2) , ('E' , 1)],
         'C' : [('D' , 2) , ('E' , 1)],
         'D' : [('F' , 4)],
         'E' : [('F' , 1)],
         'F' : [()]}
nodes = ['A' , 'B' , 'C' , 'D' , 'E' , 'F']

start = 'A'

end = 'F'
        
print(lazy_djikstra(graph , nodes , start , end))