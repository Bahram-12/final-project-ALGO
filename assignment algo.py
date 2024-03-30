#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the necessary library for handling CSV files.
import csv

#define a list named edges.
edges = [
    ('A', 'B', 6), ('A', 'F', 8), ('B', 'C', 5), ('B', 'G', 9), ('C', 'D', 7),
    ('C', 'H', 12), ('D', 'E', 5), ('D', 'I', 15), ('E', 'J', 9), ('F', 'G', 7),
    ('F', 'K', 8), ('G', 'H', 9), ('G', 'L', 13), ('H', 'I', 7), ('H', 'M', 8),
    ('I', 'J', 5), ('I', 'N', 9), ('J', 'O', 8), ('K', 'L', 5), ('L', 'M', 7),
    ('M', 'N', 8), ('N', 'O', 11), ('O', 'P', 8), ('P', 'Q', 8), ('P', 'U', 9),
    ('Q', 'R', 5), ('R', 'S', 8), ('R', 'V', 12), ('S', 'T', 9), ('T', 'U', 7),
    ('U', 'V', 5), ('V', 'W', 8)
]

# save this information in a file format
with open('graph_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Node1', 'Node2', 'Distance'])
    # we loop through each connection
    for edge in edges:
        writer.writerow(edge)
import os

if os.path.isfile('graph_data.csv'):
    print('The file graph_data.csv has been created successfully.')
else:
    print('The file graph_data.csv does not exist.')


# In[2]:


#'csv' module
import csv
from collections import defaultdict

#define a function named 'load_graph_from_csv'
def load_graph_from_csv(file_path):
    #graph
    graph = defaultdict(list)
    
    # Open the CSV file
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        #read the node identifiers
        for row in csv_reader:
            node1, node2, distance = row
            #add an edge to our graph
            graph[node1].append((node2, int(distance)))
            graph[node2].append((node1, int(distance)))

    return graph

#call our function
graph = load_graph_from_csv('graph_data.csv')

print(graph)


# In[3]:


# Import the heapq module
import heapq

# Define a function named 'dijkstra'
def dijkstra(graph, start):
    # Initialize a dictionary
    distances = {node: float('infinity') for node in graph}
    # Set the distance to 0
    distances[start] = 0
    # Initialize a priority queue
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            # Calculate the new distance
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    # Return the dictionary
    return distances

# Specify the starting node
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(shortest_paths)


# In[4]:


# Charging stations are at nodes 'H', 'K', 'Q', 'T'
charging_stations = ['H', 'K', 'Q', 'T']

# Function to find the shortest path to each charging station
def find_routes_to_stations(paths, stations):
    routes = {}
    for station in stations:
        routes[station] = paths[station]
    return routes

# Get the routes to the charging stations
routes_to_stations = find_routes_to_stations(shortest_paths, charging_stations)
print(routes_to_stations)


# In[ ]:




