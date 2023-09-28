#!/usr/bin/env python
# coding: utf-8

# In[20]:


from collections import defaultdict

class Graph(object):
    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        # add connection between two paths as a list of tuple
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        # add connection between two nodes
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

#     def remove(self, node):
#         # remove specific node
#         for n, cxns in self._graph.items():  # python3: items(); python2: iteritems()
#             try:
#                 cxns.remove(node)
#             except KeyError:
#                 pass
#         try:
#             del self._graph[node]
#         except KeyError:
#             pass

    def is_connected(self, node1, node2):
        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None


# In[14]:


class MyStack:
    # class constructor
    def __init__(self):
        self.list = []
    # push method to insert items
    def push(self, item):
        self.list.append(item)
    # pop method to push-out the top item
    def pop(self):
        if not self.is_empty():
            return self.list.pop()
        return None
    # return length of list if it is empty
    def is_empty(self):
        return len(self.list) == 0

def depth_first_search(graph, start, goal):
    stack = MyStack()
    stack.push((start, [start]))
    # run the loop until queue is not empty
    while not stack.is_empty():
        current_node, path = stack.pop()
        if current_node == goal:
            return path
        # Explore neighbors in reverse order to maintain DFS behavior
        neighbors = reversed(graph.get(current_node, []))
        for nodes in neighbors:
            if nodes not in path:
                new_path = path + [nodes]
                stack.push((nodes, new_path))
    return []


# In[21]:


class MyQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

def breadth_first_search(graph, start, goal):
    queue = MyQueue()
    queue.enqueue((start, [start]))

    while not queue.is_empty():
        current_node, path = queue.dequeue()
        if current_node == goal:    # return if current_node is equal to goal
            return path
        for nodes in graph.get(current_node, []):
            if nodes not in path: 
                new_path = path + [nodes]
                queue.enqueue((nodes, new_path))
    return []


# In[ ]:




