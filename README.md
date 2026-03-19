# AI Assignment 3 – Search Algorithms and UGV Navigation

## Author

Name: Poonuri Hansika Reddy
Roll No: SE24UCSE237

## Overview

This assignment focuses on implementing search algorithms for pathfinding problems.

It consists of three parts:

1. Dijkstra’s Algorithm on Indian cities
2. UGV Navigation with Static Obstacles
3. UGV Navigation with Dynamic Obstacles

---

## Part 1: Dijkstra’s Algorithm

Dijkstra’s algorithm (Uniform Cost Search) is used to find the shortest path between cities based on road distances.

### Features:

* Graph representation of Indian cities with distances
* Priority queue implementation using heapq
* Computes shortest path from start city to goal city
* Outputs path and total distance

### Algorithm Used:

* Best-first search based on path cost

---

## Part 2: UGV Navigation (Static Obstacles)

A 70×70 grid represents a battlefield environment where obstacles are known beforehand.

### Features:

* Grid size: 70 × 70
* Obstacles generated randomly
* Three density levels:

  * Low (0.1)
  * Medium (0.25)
  * High (0.4)
* A* algorithm used for pathfinding

### Measures of Effectiveness:

* Path Length
* Nodes Explored
* Execution Time
* Obstacle Density

### Output:

* Determines whether a path exists
* Displays performance metrics

---

## Part 3: UGV Navigation (Dynamic Obstacles)

In this scenario, obstacles are dynamic and not known in advance.

### Approach:

* Obstacles are updated at each step
* A* algorithm is used repeatedly (replanning)
* UGV moves step-by-step toward the goal

### Features:

* Dynamic obstacle generation
* Continuous path replanning
* Real-time navigation

### Measures:

* Steps Taken
* Number of Replans
* Execution Time

---

## Technologies Used

* Python 3
* heapq
* random
* math
* time

---

## How to Run

Run each file separately:

```bash
python dijkstra_india.py
python ugv_static.py
python ugv_dynamic.py
```

---

## Conclusion

* Dijkstra’s algorithm finds optimal paths in weighted graphs.
* A* improves efficiency using heuristics.
* Static environments allow precomputed paths.
* Dynamic environments require continuous replanning.

---
