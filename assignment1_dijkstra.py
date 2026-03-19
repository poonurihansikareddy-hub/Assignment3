import heapq

# Completely different set of Indian cities and connections
graph = {
    "Hyderabad": {"Vijayawada": 275, "Bangalore": 570, "Nagpur": 500},
    "Vijayawada": {"Hyderabad": 275, "Chennai": 430, "Visakhapatnam": 350},
    "Visakhapatnam": {"Vijayawada": 350, "Bhubaneswar": 445},
    "Bhubaneswar": {"Visakhapatnam": 445, "Kolkata": 440},
    "Kolkata": {"Bhubaneswar": 440, "Patna": 580},
    "Patna": {"Kolkata": 580, "Ranchi": 330, "Varanasi": 250},
    "Ranchi": {"Patna": 330, "Raipur": 400},
    "Raipur": {"Ranchi": 400, "Nagpur": 295},
    "Nagpur": {"Raipur": 295, "Hyderabad": 500, "Bhopal": 350},
    "Bhopal": {"Nagpur": 350, "Indore": 190},
    "Indore": {"Bhopal": 190, "Surat": 380},
    "Surat": {"Indore": 380, "Mumbai": 280},
    "Mumbai": {"Surat": 280, "Pune": 150},
    "Pune": {"Mumbai": 150, "Bangalore": 840},
    "Bangalore": {"Hyderabad": 570, "Pune": 840, "Mysore": 145},
    "Mysore": {"Bangalore": 145},
    "Chennai": {"Vijayawada": 430, "Madurai": 460},
    "Madurai": {"Chennai": 460, "Kochi": 200},
    "Kochi": {"Madurai": 200, "Thiruvananthapuram": 205},
    "Thiruvananthapuram": {"Kochi": 205},
    "Varanasi": {"Patna": 250}
}


def dijkstra_search(graph, start, goal):
    pq = [(0, start)]
    dist = {city: float('inf') for city in graph}
    parent = {}

    dist[start] = 0

    while pq:
        current_dist, current_city = heapq.heappop(pq)

        if current_city == goal:
            break

        for neighbor, weight in graph[current_city].items():
            new_dist = current_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = current_city
                heapq.heappush(pq, (new_dist, neighbor))

    # reconstruct path
    path = []
    node = goal
    while node in parent or node == start:
        path.append(node)
        if node == start:
            break
        node = parent[node]

    path.reverse()
    return path, dist[goal]


# ---- Execution ----
print("Cities available:\n")
for c in graph:
    print(c)

start = input("\nEnter start city: ").strip()
goal = input("Enter goal city: ").strip()

path, distance = dijkstra_search(graph, start, goal)

print("\nShortest Path:")
print(" -> ".join(path))
print("Total Distance:", distance, "km")