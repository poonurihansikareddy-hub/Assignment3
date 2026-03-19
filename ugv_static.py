import heapq
import random
import math
import time

ROWS = 70
COLS = 70

FREE = 0
OBSTACLE = 1


# Generate battlefield with obstacle density
def generate_grid(density):
    grid = [[FREE for _ in range(COLS)] for _ in range(ROWS)]

    for i in range(ROWS):
        for j in range(COLS):
            if random.random() < density:
                grid[i][j] = OBSTACLE

    return grid


# Heuristic function (Euclidean distance)
def heuristic(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


# A* algorithm for shortest path
def astar(grid, start, goal):
    start_time = time.time()

    open_list = [(0, start)]
    g_cost = {start: 0}
    parent = {}
    visited = set()

    nodes_explored = 0

    while open_list:
        _, current = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)
        nodes_explored += 1

        if current == goal:
            break

        x, y = current

        # 4-direction movement
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < ROWS and 0 <= ny < COLS:
                if grid[nx][ny] == FREE:
                    new_cost = g_cost[current] + 1

                    if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                        g_cost[(nx, ny)] = new_cost
                        f_cost = new_cost + heuristic((nx, ny), goal)
                        heapq.heappush(open_list, (f_cost, (nx, ny)))
                        parent[(nx, ny)] = current

    end_time = time.time()

    # Reconstruct path
    path = []
    node = goal

    while node in parent or node == start:
        path.append(node)
        if node == start:
            break
        node = parent[node]

    path.reverse()

    runtime = (end_time - start_time) * 1000  # ms

    return path, nodes_explored, runtime


# Measure performance (MOE)
def performance_report(grid, path, explored, runtime, start, goal, density):
    total_cells = ROWS * COLS
    obstacle_cells = sum(row.count(OBSTACLE) for row in grid)

    print("\n==============================")
    print("MEASURES OF EFFECTIVENESS")
    print("==============================")

    print("Grid Size:", ROWS, "x", COLS)
    print("Obstacle Density:", density)
    print("Obstacle Cells:", obstacle_cells, "/", total_cells)
    print("Start:", start)
    print("Goal:", goal)

    if path:
        print("\nPath Found: YES")
        print("Path Length:", len(path))

        straight_dist = math.sqrt((goal[0]-start[0])**2 + (goal[1]-start[1])**2)
        print("Straight Distance:", round(straight_dist, 2))

        detour = len(path) - straight_dist
        print("Detour:", round(detour, 2))
    else:
        print("\nPath Found: NO")

    print("\nNodes Explored:", explored)
    print("Execution Time:", round(runtime, 2), "ms")
    print("==============================\n")


# Run simulation for one density
def run_simulation(density):
    print("\nRunning simulation with density:", density)

    grid = generate_grid(density)

    start = (0, 0)
    goal = (69, 69)

    # Ensure start and goal are free
    grid[start[0]][start[1]] = FREE
    grid[goal[0]][goal[1]] = FREE

    path, explored, runtime = astar(grid, start, goal)

    performance_report(grid, path, explored, runtime, start, goal, density)


# Compare different densities
def compare_densities():
    densities = [0.1, 0.25, 0.4]   # Low, Medium, High

    for d in densities:
        run_simulation(d)


# ---- MAIN ----
print("\nUGV Navigation (Static Obstacles - 70x70 Grid)")

compare_densities()