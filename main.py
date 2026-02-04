import heapq

def heuristic(a, b):
    """
    Manhattan distance heuristic
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal, allow_diagonal=False):
    """
    grid : 2D list (0 = free cell, 1 = obstacle)
    start, goal : tuples (x, y)
    allow_diagonal : allow diagonal movements
    """

    rows, cols = len(grid), len(grid[0])

    # Open set (priority queue)
    open_set = []
    heapq.heappush(open_set, (0, start))

    # Tracking
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    closed_set = set()

    # Movement directions
    if allow_diagonal:
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
    else:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        closed_set.add(current)
        x, y = current

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            neighbor = (nx, ny)

            if not (0 <= nx < rows and 0 <= ny < cols):
                continue
            if grid[nx][ny] == 1 or neighbor in closed_set:
                continue

            tentative_g = g_score[current] + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def print_grid(grid, path=None):
    visual = [["." for _ in row] for row in grid]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                visual[i][j] = "#"

    if path:
        for x, y in path:
            visual[x][y] = "*"

    for row in visual:
        print(" ".join(row))

def hello():
    print("Hello, A* Pathfinding!")

def main():
    grid = [
        [0, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

    start = (0, 0)
    goal = (4, 6)

    path = astar(grid, start, goal, allow_diagonal=False)

    if path:
        print("Path found:")
        print_grid(grid, path)
    else:
        print("No path found.")
    hello()