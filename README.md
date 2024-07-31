# IITISoC-24-IVR-2-MICROMOUSE

## GOAL
To develop a maze solving micromouse with hardware integration using stimulation

People Involved : 

Mentors:
- [Ampady B R](https://github.com/ampady06)
- [Bhawna Chaudhary](https://github.com/WebWizard104)

Members:
<br>

- [K Bharath Varma](https://github.com/bharath2varma)
- [V Poorna sai reddy](https://github.com/poornareddy396)
- [N Srinivas Gopi Charan](https://github.com/Chandu-08)
- [Sathvika V](https://github.com/sathvika1128)


## MICROMOUSE

A Micromouse is a small robotic vehicle designed to navigate its way through an unknown maze. It is an autonomous, battery-operated, and self-contained robot that utilizes maze-solving algorithms to find the shortest route to the center of the maze.

## ALGORITHMS
There are different algorithms to solve the maze and those include wall following,depth first search,floodfill,A*.

The wall following algorithm is the simplest of the maze solving techniques. Basically, this algorithm makes mouse follow either the left or the right wall as a guide around the maze. If the mouse just follows the right/left walls, exploring only the perimeter of the maze without venturing into the middle section.

The depth first search is an intuitive method of searching a maze. Basically, the mouse simply starts moving. When it comes to an intersection in the maze, it randomly chooses one of the paths. If that path leads to a dead end, the mouse backtracks to the inter section and chooses another path. This forces the robot to explore every possible path within the maze. By exploring every cell within the maze the mouse will eventually find the centre. 

The flood-fill algorithm involves assigning values to each of the cells in the maze where these values represent the distance from any cell on the maze to the destination cell. The destination cell, therefore, is assigned a value of 0.
When it comes time to make a move, the robot must examine all adjacent cells which are not separated by walls and choose the one with the lowest distance value.
The flood-fill algorithm is a good way of finding the shortest (if not the fastest) path from the start cell to the destination cells.

We chose BFS with flood fill over DFS due to our clearer understanding of BFS and its straightforward implementation. Despite its higher memory usage, we believed it could be refined more effectively. Our decision was driven by familiarity and the potential for optimization.









