import heapq
import random
import math
import time

ROWS = 70
COLS = 70

FREE = 0
OBSTACLE = 1


# Create empty grid
def create_grid():
    return [[FREE for _ in range(COLS)] for _ in range(ROWS)]


# Add dynamic obstacles
def update_obstacles(grid, prob):
    for i in range(ROWS):
        for j in range(COLS):
            if random.random() < prob:
                grid[i][j] = OBSTACLE


# Heuristic
def heuristic(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


# A* algorithm
def astar(grid, start, goal):
    pq = [(0, start)]
    cost = {start: 0}
    parent = {}
    visited = set()

    while pq:
        _, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            break

        x, y = current
        moves = [(-1,0), (1,0), (0,-1), (0,1)]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < ROWS and 0 <= ny < COLS:
                if grid[nx][ny] == FREE:
                    new_cost = cost[current] + 1

                    if (nx, ny) not in cost or new_cost < cost[(nx, ny)]:
                        cost[(nx, ny)] = new_cost
                        f = new_cost + heuristic((nx, ny), goal)
                        heapq.heappush(pq, (f, (nx, ny)))
                        parent[(nx, ny)] = current

    # reconstruct path
    path = []
    node = goal
    while node in parent or node == start:
        path.append(node)
        if node == start:
            break
        node = parent[node]

    path.reverse()
    return path


# Dynamic simulation
def run_dynamic():
    grid = create_grid()

    start = (0, 0)
    goal = (69, 69)

    current = start
    steps = 0
    replans = 0

    start_time = time.time()

    print("\nDynamic UGV Navigation Started...\n")

    while current != goal:
        # obstacles change every step
        update_obstacles(grid, 0.1)

        # ensure current & goal are free
        grid[current[0]][current[1]] = FREE
        grid[goal[0]][goal[1]] = FREE

        path = astar(grid, current, goal)

        if len(path) < 2:
            print("No path available due to dynamic obstacles!")
            break

        # move one step
        current = path[1]
        steps += 1
        replans += 1

    end_time = time.time()

    # ---- OUTPUT ----
    print("\n===== DYNAMIC ENVIRONMENT REPORT =====")
    print("Goal Reached:", "YES" if current == goal else "NO")
    print("Steps Taken:", steps)
    print("Replans:", replans)
    print("Execution Time:", round((end_time - start_time)*1000, 2), "ms")
    print("======================================\n")


# ---- MAIN ----
print("UGV Navigation with Dynamic Obstacles (70x70)")

run_dynamic()