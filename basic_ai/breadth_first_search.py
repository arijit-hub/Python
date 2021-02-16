# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 00:59:01 2021

@author: Arijit
"""

class queue(object):
    '''
    Formulates the Queue Data Structure.
    '''
    def __init__(self):
        self.queue_list = []
        
    def enqueue(self , num):
        '''
        Inserting an element to the queue.
        '''
        if num not in self.queue_list:
            self.queue_list.append(num)
        
    def dequeue(self):
        '''
        Remove an element from the queue.
        '''
        self.queue_list.pop(0)
        
    def isEmpty(self):
        '''
        Check if the queue is empty.
        '''
        return len(self.queue_list) == 0
    
    def __iter__(self):
        for i in self.queue_list:
            yield i
            
    def get_member(self, idx):
        return self.queue_list[idx]
    
    def __repr__(self):
        return str(self.queue_list)

nodes = ['A' , 'B' , 'C' , 'D' , 'E' , 'F']

graph = [['A' , ('B' , 'C')],
         ['B' , ('A' , 'D' , 'E')],
         ['C' , ('A' , 'E')],
         ['D' , ('B' , 'F')],
         ['E' , ('C' , 'B' , 'F')],
         ['F' , ('D' , 'E')]]

visited = [False] * len(nodes)

q = queue()

def bfs(current , nodes , graph , visited):
    
    visited_idx = nodes.index(current)
    
    
    if visited[visited_idx] == True:
        return
    
    else:
        print(current)
        neighbors = []
        visited[visited_idx] = True
        
        q.enqueue(current)
        
        for adj in graph:
            if adj[0]  == current:
                for node in adj[1]:
                    neighbors.append(node)
                    if visited[nodes.index(node)] == False:
                        q.enqueue(node)
        
        
        print(q)
        q.dequeue()        
        
        for q_node in q:
            bfs(q_node , nodes , graph , visited)


bfs('A' , nodes , graph , visited)