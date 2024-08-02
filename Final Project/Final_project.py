# Final Project: EV Charging Station Route Optimization Application
# The context of this project focuses on leveraging algorithmic solutions to optimize
# route planning for Electric Vehicle users, making the process of locating and navigating
# to the nearest or most convenient charging station as seamless as possible.

# The objective of this script is to provide the shortest path from a specific location to the closest charging station.


# The case graph consist on 23 nodes (A to W) including 4 charging stations (H, K, Q and T).
# The graph will be represented using an array-based Map, containing entries (Key:Values) for each node;
# Defining the name of the node as the key and the cost as the value.

# Graph representation:
case_graph = {
    'A': {'B': 6, 'F': 5},
    'B': {'A': 6, 'C': 5, 'G': 6},
    'C': {'B': 5, 'D': 7, 'H': 5},
    'D': {'C': 7, 'E': 7, 'I': 8},
    'E': {'D': 7, 'I': 6, 'N': 15},
    'F': {'A': 5, 'G': 8, 'J': 7},
    'G': {'B': 6, 'F': 8, 'H': 9, 'K': 8},
    'H': {'C': 5, 'G': 9, 'I': 12},
    'I': {'D': 8, 'E': 6, 'H': 12, 'M': 10},
    'J': {'F': 7, 'K': 5, 'O': 7},
    'K': {'G': 8, 'J': 5, 'L': 7},
    'L': {'K': 7, 'M': 7, 'P': 7},
    'M': {'I': 10, 'L': 7, 'N': 9},
    'N': {'E': 15, 'M': 9, 'R': 7},
    'O': {'J': 7, 'P': 13, 'S': 9},
    'P': {'L': 7, 'O': 13, 'Q': 8, 'U': 11},
    'Q': {'P': 8, 'R': 9},
    'R': {'N': 7, 'Q': 9, 'W': 10},
    'S': {'O': 9, 'T': 9},
    'T': {'S': 9, 'U': 8},
    'U': {'P': 11, 'T': 8, 'V': 8},
    'V': {'U': 8, 'W': 5},
    'W': {'R': 10, 'V': 5}

}

charging_stations = {
    'H', 'K', 'Q', 'T'
}


# Next section defines the Dijkstra Algorithm that it will calculate the shortest path
# from a given node to all the other nodes.
# The input of this function requires the graph and the start node.
# The output of the graph is an array-based map, represented by entries (key:Value) where the key represents the
# target node, and the value represent two entries storing the lowest cost to that node and the parent of
# the target node (the node where the shortest path came from)

def dijkstra(graph, start):
    # initialize two lists, one for the unvisited nodes (open nodes) and another one for the visited nodes (closed
    # List)
    unvisited = {start}
    visited = []

    # Initialize the shortest distance from the start node to itself as zero and assume that the cost to the rest of the
    # nodes is +infinite

    shortest_distance = {node: {'distance': float('inf'), 'parent': None} for node in graph}
    # shortest distance to the specified node as: {Vertex:{distance from start : parent node}

    shortest_distance[start]['distance'] = 0

    while unvisited:

        current = min(unvisited, key=lambda x: shortest_distance[x]['distance'])
        # Pick the current node as the node with the closest distance to the start node

        # Let's analyze current node, Move the node to the visited list and delete it from unvisited list
        unvisited.remove(current)
        visited.append(current)

        # Evaluate each neighbor of the current vertex
        for neighbor in graph[current]:
            if neighbor in visited:
                continue                               # Ignore the node if already visited
            elif neighbor not in unvisited:
                unvisited.add(neighbor)                # Otherwise, if neighbor not yet in open list, add it to the list

            cost_from_current = shortest_distance[current]['distance'] + graph[current][neighbor]
            # The cost to the neighbor node from the current node

            # If the new cost is lower that the previous cost, then update the cost and the parent.
            if cost_from_current < shortest_distance[neighbor]['distance']:
                shortest_distance[neighbor]['distance'] = cost_from_current
                shortest_distance[neighbor]['parent'] = current

    # Return the list of nodes with its shortest distance from start and parent node
    return shortest_distance


# Next function compare the shortest distances to the available charge stations and return the nearest station.
def closest_station(dijkstra_table, stations):
    # First, get the charging stations nodes from the dijkstra results
    distance_station = {node: dijkstra_table[node]['distance'] for node in stations}

    # Then Pick the node with the minimum distance and get its cost
    closest_node = min(distance_station, key=distance_station.get)
    cost_to_closest = dijkstra_table[closest_node]['distance']

    return closest_node, cost_to_closest                # Return the nearest station with its cost


# The next function, construct the path to a specific node (nearest station). The backtracking is performed storing the
# parent of each node in an array and then reversing the array.
def path_to_closest(dijkstra_table, nearest_station):
    # Initialize an array containing the last node
    final_path = [nearest_station]
    parent = dijkstra_table[nearest_station]['parent']

    # For each parent node, attach its parent to the list
    while parent:                                       # The parent of the start node is null
        final_path.append(parent)
        parent = dijkstra_table[parent]['parent']

    # Reverse the array to get the final path
    final_path.reverse()
    return final_path


# --------> Main program

initial_node = input("Please enter starting node: ")
# Run the dijkstra algorithm for the given graph and an initial node
tabled = dijkstra(case_graph, initial_node)
# From the previous result, evaluate which is the nearest charging station
Station, cost_st = closest_station(tabled, charging_stations)
# Get the path to the selected station
path = path_to_closest(tabled, Station)

# Print the results
# Print the dijkstra table results to each node
for node in tabled:
    print(f"\n{node}: {tabled[node]}")

# Print the recommended station, with its cost and path
print(f"\n\nRecommended charging station --> {Station}\nDistance to station: {cost_st}\nPath to the station: {path}")
