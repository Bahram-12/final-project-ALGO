#!/usr/bin/env python
# coding: utf-8
#_______________GROUP PROJECT_____BAHRAM-HASSANZADA-100817345_____JACOB-KORIN-100860365_____
#___________________________________Fahad-Shafiq-100831055______ Munim-Melaque-100847597____
# In[1]:


#import the necessary library for handling CSV files.
import csv

#define a list named edges.
edges = [
  ('A', 'B', 6), ('A', 'F', 5), ('B', 'C', 5), ('B', 'G', 6), ('C', 'D', 7), ('C', 'H', 5),
  ('D', 'E', 7), ('D', 'I', 8), ('E', 'I', 6), ('E', 'N', 15), ('F', 'G', 8), ('F', 'J', 7),
  ('G', 'H', 9), ('G', 'K', 8), ('H', 'I', 12),('I', 'M', 10), ('J', 'K', 5), ('J', 'O', 7),
  ('K', 'L', 7), ('L', 'M', 7), ('L', 'P', 7), ('M', 'N', 9), ('N', 'R', 7), ('O', 'P', 13), 
    ('O', 'S', 9), ('P', 'Q', 8), ('P', 'U', 11), ('Q', 'R', 9), ('R', 'W', 10), ('S', 'T', 9), 
    ('T', 'U', 8), ('U', 'V', 8), ('V', 'W', 5)
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
        # Initialize paths dictionary, where each node's path starts as an empty list
    paths = {node: [] for node in graph}
    # Set the distance to 0
    distances[start] = 0
    paths[start] = [start]
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
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappush(priority_queue, (distance, neighbor))
    # Return the dictionary
    return distances, paths

# Specify the starting node
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
distances, paths = dijkstra(graph, start_node)
print(shortest_paths)

# Example: Print the shortest path and distance to node 'B'
print(f"Shortest path to B: {paths['B']}, Distance: {distances['B']}")


# In[4]:


start_node = 'A'

# Function to find the shortest path to each charging station
def find_routes_to_stations(paths, stations):
    routes = {}
    for station in stations:
        routes[station] = paths.get(station, [])
    return routes

# Specify the charging stations
charging_stations = ['H', 'K', 'Q', 'T']

# Get the routes to the charging stations
routes_to_stations = find_routes_to_stations(paths, charging_stations)

# Print the shortest paths to the charging stations
for station, route in routes_to_stations.items():
    print(f"Shortest path to {station}: {route} with distance: {distances.get(station, 'Unknown')}")


# In[ ]:




