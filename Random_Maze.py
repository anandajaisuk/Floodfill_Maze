import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

maze_size = 16

start = (0, 0)  # Top left
goal = (maze_size - 1, maze_size - 1)  # Bottom right

# Initialize an empty maze (0 = path, 1 = wall)
maze = np.zeros((maze_size, maze_size))

# Function to randomly generate walls
def generate_random_walls(num_walls, maze_size):
    walls = []
    directions = ['top', 'right', 'bottom', 'left']
    
    for _ in range(num_walls):
        y = random.randint(0, maze_size - 1)
        x = random.randint(0, maze_size - 1)
        direction = random.choice(directions)
        walls.append((y, x, direction))
    
    return walls

# Random walls
num_walls = 70
walls = generate_random_walls(num_walls, maze_size)

# Directions: North, East, South, West (dy, dx)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
directions_map = ['top', 'right', 'bottom', 'left']

# Floodfill function to populate the maze with distances from the goal
def floodfill(maze, goal):
    rows, cols = maze.shape
    flood = np.full((rows, cols), np.inf)  # Start flood values with infinity
    flood[goal] = 0  # Set goal as distance 0

    queue = [goal]
    while queue:
        current = queue.pop(0)
        current_value = flood[current]

        # Explore all four directions
        for i, direction in enumerate(directions):
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            # Check if the neighbor is within the maze bounds and not a wall
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor] == 0:
                if not is_wall_blocking(current, neighbor, walls):  # Check if there's a wall
                    if flood[neighbor] > current_value + 1:
                        flood[neighbor] = current_value + 1
                        queue.append(neighbor)
    
    return flood

# Function to check if a wall is blocking the direction
def is_wall_blocking(current, neighbor, walls):
    cy, cx = current
    ny, nx = neighbor
    if cy == ny and cx < nx:  # Moving right
        return (cy, cx, 'right') in walls or (ny, nx, 'left') in walls
    elif cy == ny and cx > nx:  # Moving left
        return (cy, cx, 'left') in walls or (ny, nx, 'right') in walls
    elif cx == nx and cy < ny:  # Moving down
        return (cy, cx, 'bottom') in walls or (ny, nx, 'top') in walls
    elif cx == nx and cy > ny:  # Moving up
        return (cy, cx, 'top') in walls or (ny, nx, 'bottom') in walls
    return False

# Function to find a path from the start to the goal
def find_path(flood_map, start, goal, walls):
    path = [start]
    current = start
    while current != goal:
        neighbors = [(current[0] + dy, current[1] + dx) for dy, dx in directions]
        valid_neighbors = [(y, x) for y, x in neighbors if 0 <= y < maze_size and 0 <= x < maze_size and maze[y, x] == 0]
        # Check that there is no wall blocking the direction
        valid_neighbors = [pos for pos in valid_neighbors if not is_wall_blocking(current, pos, walls)]
        current = min(valid_neighbors, key=lambda pos: flood_map[pos])
        path.append(current)
    return path

# Function to draw the walls with thick lines in the specified direction
def draw_walls_custom(maze, ax, walls):
    for (y, x, side) in walls:
        if side == 'top':
            ax.plot([x, x+1], [y, y], color='black', linewidth=4)
        if side == 'bottom':
            ax.plot([x, x+1], [y+1, y+1], color='black', linewidth=4)
        if side == 'left':
            ax.plot([x, x], [y, y+1], color='black', linewidth=4)
        if side == 'right':
            ax.plot([x+1, x+1], [y, y+1], color='black', linewidth=4)

# Run floodfill on the maze
flood_map = floodfill(maze, goal)

# Find the path from start to goal
path = find_path(flood_map, start, goal, walls)

# Plot the floodfill results
fig, ax = plt.subplots(figsize=(12, 12))
ax.set_aspect('equal')

# Plot floodfill values
for y in range(maze_size):
    for x in range(maze_size):
        if maze[y, x] == 0:  # Show only cells that are not walls
            ax.text(x + 0.5, y + 0.5, f"{int(flood_map[y, x])}", va='center', ha='center')

# Draw the grid for the maze
for x in range(maze_size + 1):
    ax.axhline(x, lw=1, color='black')
    ax.axvline(x, lw=1, color='black')

# Highlight the start and goal points
start_rect = patches.Rectangle((start[1], start[0]), 1, 1, linewidth=0, edgecolor=None, facecolor='lightgreen', alpha=0.5)
goal_rect = patches.Rectangle((goal[1], goal[0]), 1, 1, linewidth=0, edgecolor=None, facecolor='lightcoral', alpha=0.5)
ax.add_patch(start_rect)
ax.add_patch(goal_rect)

# Draw walls using the custom draw function with the specified directions
draw_walls_custom(maze, ax, walls)

# Draw the green path between nodes, from the center of each cell
for i in range(len(path) - 1):
    current = path[i]
    next_node = path[i + 1]
    # Draw lines from the center of each cell (+0.5) to the next
    ax.plot([current[1] + 0.5, next_node[1] + 0.5], [current[0] + 0.5, next_node[0] + 0.5], 
            color='green', linewidth=3, zorder=10)

ax.set_xlim(0, maze_size)
ax.set_ylim(maze_size, 0)  # Invert y-axis without using invert_yaxis()

# Remove axis markers
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()
plt.show()
