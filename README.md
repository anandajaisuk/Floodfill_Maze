# Maze Solver using Flood Fill Algorithm

This project implements a maze-solving algorithm using the **flood fill method** to find the shortest path from a start point to a goal in a 16x16 grid. The maze is defined by walls, and the solution involves checking for obstacles and visualizing the optimal path using Python's `matplotlib` for graphical representation.

## Features

- **Flood Fill Algorithm**: Calculates the distance from the goal to all other points in the maze.
- **Wall Detection**: Identifies walls in the maze and ensures that the algorithm navigates around them.
- **Pathfinding**: Finds and highlights the shortest path from the start to the goal.
- **Visualization**: Visualizes the maze, walls, and the optimal path using `matplotlib`.

## Requirements
You can install these dependencies using the provided `requirements.txt` file:
```bash
pip install -r requirements.txt
```
## Demonstration
![1_aeauHcJPbJnghjSNWO2RLA](https://github.com/user-attachments/assets/5ce2104e-6203-4105-b528-bf046d2f57fd)
<br>
https://medium.com/@minikiraniamayadharmasiri/micromouse-from-scratch-algorithm-maze-traversal-shortest-path-floodfill-741242e8510
This maze image is from the article Micromouse from Scratch: Algorithm, Maze Traversal, Shortest Path, and Floodfill, which I referenced to create an example for this project. Thank you so much!

## Steps
1. Create a Maze: Click on the nodes where you want to place walls and save the maze configuration.
```bash
python Create_Maze.py
```

![messageImage_1729377754172](https://github.com/user-attachments/assets/f86a9a17-35f6-4a39-9aed-581967510183)

2. Run the Maze Solver: Execute the custom maze solver to see the result.
```bash
python Custom_Maze.py
```
![messageImage_1729377806043](https://github.com/user-attachments/assets/061ff5b9-9178-41e5-ba90-b55ea6068799)
