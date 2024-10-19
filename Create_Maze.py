import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Set the size of the maze (16x16)
maze_size = 16
walls = np.zeros((maze_size, maze_size, 4))  # 4 directions: left, right, top, bottom

# Define the start and goal points
# x, y
start = (0.5, 15.5)
goal = (8.5, 8.5)

# Function to handle click events
def on_click(event):
    if event.inaxes:
        x = int(event.xdata)
        y = int(event.ydata)

        # Check if the click is within the grid bounds
        if 0 <= x < maze_size and 0 <= y < maze_size:
            # Determine which side (left, right, top, bottom) was clicked based on the click location
            if abs(event.xdata - x) < 0.1:  # Click near the left side
                walls[y, x][0] = (walls[y, x][0] + 1) % 2
            elif abs(event.xdata - (x + 1)) < 0.1:  # Click near the right side
                walls[y, x][1] = (walls[y, x][1] + 1) % 2
            elif abs(event.ydata - y) < 0.1:  # Click near the top side
                walls[y, x][2] = (walls[y, x][2] + 1) % 2
            elif abs(event.ydata - (y + 1)) < 0.1:  # Click near the bottom side
                walls[y, x][3] = (walls[y, x][3] + 1) % 2
            draw_grid()

# Function to draw the grid and walls
def draw_grid():
    ax.clear()
    # Draw the grid
    for i in range(maze_size + 1):
        ax.axhline(i, lw=2, color='black')
        ax.axvline(i, lw=2, color='black')

    # Draw the walls
    for y in range(maze_size):
        for x in range(maze_size):
            if walls[y, x][0]:  # Left wall
                ax.plot([x, x], [y, y+1], color='red', linewidth=4)
            if walls[y, x][1]:  # Right wall
                ax.plot([x+1, x+1], [y, y+1], color='red', linewidth=4)
            if walls[y, x][2]:  # Top wall
                ax.plot([x, x+1], [y, y], color='red', linewidth=4)
            if walls[y, x][3]:  # Bottom wall
                ax.plot([x, x+1], [y+1, y+1], color='red', linewidth=4)

    # Add a red circle at the start position (0, 0)
    start_circle = patches.Circle(start, 0.2, color='red')  # Draw a circle at the start position
    ax.add_patch(start_circle)

    # Add a green circle at the goal position (15, 15)
    goal_circle = patches.Circle(goal, 0.2, color='green')  # Draw a circle at the goal position
    ax.add_patch(goal_circle)

    ax.invert_yaxis()  # Invert the y-axis to make (0, 0) the top-left corner
    plt.draw()

# Function to save the wall data to a file in list format
def save_to_file():
    with open('Walls_list.py', 'w') as f:
        f.write("walls = [\n")
        for y in range(maze_size):
            for x in range(maze_size):
                # Check if there is a wall in any direction
                if np.any(walls[y, x] == 1):  # If there are walls
                    f.write(f"    ({y}, {x}, {int(walls[y,x][0])}, {int(walls[y,x][1])}, {int(walls[y,x][2])}, {int(walls[y,x][3])}),\n")
        f.write("]\n")
    print("Walls saved to walls_list.py")

# Set up the UI
fig, ax = plt.subplots(figsize=(6, 6))
fig.canvas.mpl_connect('button_press_event', on_click)

# Save button
ax_save = plt.axes([0.7, 0.02, 0.1, 0.05])
btn_save = plt.Button(ax_save, 'Save Walls')
btn_save.on_clicked(lambda event: save_to_file())

draw_grid()
plt.show()
