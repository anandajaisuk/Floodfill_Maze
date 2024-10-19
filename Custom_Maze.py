import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from walls_list import walls

# Define the size of the maze (16x16)
maze_size = 16

# Define the start and goal points
start = (15, 0)  # Bottom-left corner
goal = (maze_size // 2, maze_size // 2)  # Middle

# Create an empty maze (0 = path, 1 = wall)
maze = np.zeros((maze_size, maze_size))



# Directions: North, East, South, West (dy, dx)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
directions_map = ['top', 'right', 'bottom', 'left']

# Floodfill function to fill the maze with distances from the goal
def floodfill(maze, goal):
    rows, cols = maze.shape
    flood = np.full((rows, cols), np.inf)  # Initialize flood values with infinity
    flood[goal] = 0  # Set goal distance to 0

    queue = [goal]
    while queue:
        current = queue.pop(0)
        current_value = flood[current]

        # Explore all four directions
        for i, direction in enumerate(directions):
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            # Check if the neighbor is within the maze boundaries and is not a wall
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor] == 0:
                if not is_wall_blocking(current, neighbor, walls):  # Check if a wall is blocking
                    if flood[neighbor] > current_value + 1:
                        flood[neighbor] = current_value + 1
                        queue.append(neighbor)
    
    return flood

# Function to check if a wall is blocking the direction
def is_wall_blocking(current, neighbor, walls):
    cy, cx = current
    ny, nx = neighbor
    for wall in walls:
        wy, wx, left, right, top, bottom = wall
        if (cy, cx) == (wy, wx):
            if cy == ny and cx < nx and right == 1:  # Going right
                return True
            if cy == ny and cx > nx and left == 1:  # Going left
                return True
            if cx == nx and cy < ny and bottom == 1:  # Going down
                return True
            if cx == nx and cy > ny and top == 1:  # Going up
                return True
        if (ny, nx) == (wy, wx):
            if ny == cy and nx < cx and right == 1:  # Returning from right
                return True
            if ny == cy and nx > cx and left == 1:  # Returning from left
                return True
            if nx == cx and ny < cy and bottom == 1:  # Returning from down
                return True
            if nx == cx and ny > cy and top == 1:  # Returning from up
                return True
    return False

# Function to find a path from the start to the goal
def find_path(flood_map, start, goal, walls):
    path = [start]
    current = start
    while current != goal:
        neighbors = [(current[0] + dy, current[1] + dx) for dy, dx in directions]
        valid_neighbors = [(y, x) for y, x in neighbors if 0 <= y < maze_size and 0 <= x < maze_size and maze[y, x] == 0]
        # Check if the direction is not blocked by a wall
        valid_neighbors = [pos for pos in valid_neighbors if not is_wall_blocking(current, pos, walls)]
        current = min(valid_neighbors, key=lambda pos: flood_map[pos])
        path.append(current)
    return path

# Function to draw walls as thick lines for specified directions
def draw_walls_custom(maze, ax, walls):
    for (y, x, left, right, top, bottom) in walls:
        if top == 1:
            ax.plot([x, x+1], [y, y], color='black', linewidth=4)
        if bottom == 1:
            ax.plot([x, x+1], [y+1, y+1], color='black', linewidth=4)
        if left == 1:
            ax.plot([x, x], [y, y+1], color='black', linewidth=4)
        if right == 1:
            ax.plot([x+1, x+1], [y, y+1], color='black', linewidth=4)

# Perform Floodfill on the maze
flood_map = floodfill(maze, goal)

# Find a path from the start to the goal
path = find_path(flood_map, start, goal, walls)

# Plot the Floodfill result
fig, ax = plt.subplots(figsize=(12, 12))
ax.set_aspect('equal')

# Draw the Floodfill values
for y in range(maze_size):
    for x in range(maze_size):
        if maze[y, x] == 0:  # Show only non-wall cells
            ax.text(x + 0.5, y + 0.5, f"{int(flood_map[y, x])}", va='center', ha='center')

# Create a grid for the maze
for x in range(maze_size + 1):
    ax.axhline(x, lw=1, color='black')
    ax.axvline(x, lw=1, color='black')

# Highlight the start and goal points
start_rect = patches.Rectangle((start[1], start[0]), 1, 1, linewidth=0, edgecolor=None, facecolor='lightgreen', alpha=0.5)
goal_rect = patches.Rectangle((goal[1], goal[0]), 1, 1, linewidth=0, edgecolor=None, facecolor='lightcoral', alpha=0.5)
ax.add_patch(start_rect)
ax.add_patch(goal_rect)

# Draw walls using the draw_walls_custom function
draw_walls_custom(maze, ax, walls)

# Draw the green path as a straight line between nodes from the center of each cell
for i in range(len(path) - 1):
    current = path[i]
    next_node = path[i + 1]
    # Use the center of each cell (+0.5) to draw the lines
    ax.plot([current[1] + 0.5, next_node[1] + 0.5], [current[0] + 0.5, next_node[0] + 0.5], 
            color='green', linewidth=3, zorder=10)

ax.set_xlim(0, maze_size)
ax.set_ylim(maze_size, 0)  # Reverse the y-axis without using invert_yaxis()

# Remove axis ticks
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()
plt.show()
