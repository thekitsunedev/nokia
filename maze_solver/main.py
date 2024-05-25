from dataclasses import dataclass

"""
This script uses the breadth-first-search algorithm to find the shortest path from start to finish.

Kis Vilmos Bendegúz - TheKitsuneDev @ 2024 nokia_hackathon
"""

@dataclass
class Tile:
    x: int
    y: int
    type: str
    direction: str
    parent: 'Tile' = None

    @property
    def xy(self) -> str:
        return str(self.x) + str(self.y)    


def get_neighbors(maze: list, x: int, y: int) -> list:
    """
    Returns with a list of the neighbors of the cell given by x and y.
    """
    DIRECTIONS: list = ['U', 'L', 'D', 'R']
    neighbors: list = []
    neighbor: Tile
    for i in range(2):
        for j in range(-1,2,2):
            neighbor = Tile(
                x = x + i * j,
                y = y + (1 - i) * j,
                type = maze[y + (1 - i) * j][x + i * j],
                direction = DIRECTIONS[i+1+j]
            )
            neighbors.append(neighbor)
    return neighbors


def solve_maze(maze: list) -> str:
    """
    Returns with the shortest path from start to finish
    "S # # ... G"
    S: Start
    U: Up
    D: Down
    L: Left
    R: Right
    """
    # Find starting cell
    startcell: Tile = None
    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            if col == "S":
                startcell: Tile = Tile(x, y, "S", "S")
                break
        if startcell:
            break
    
    checked: list = []
    tosearch: list = [startcell]
    while tosearch:
        selected: Tile = tosearch[0]
        checked.append(selected.xy)
        tosearch.pop(0)

        neighbor: Tile
        for neighbor in get_neighbors(maze, selected.x, selected.y):
            if neighbor.xy in checked:
                continue
            if neighbor.type == "#":
                checked.append(neighbor.xy)
                continue

            neighbor.parent = selected

            if neighbor.type == "G":
                selected = neighbor
                tosearch.clear()
                break

            tosearch.append(neighbor)
    
    result: str = "G"
    while selected.parent:
        result += f" {selected.direction}"
        selected = selected.parent
    result += " S"
    return result[::-1]


# Read mazes
with open('./input.txt', 'r') as f:
    rows: list = f.readlines()
    rows.append("\n")
    index: int = 0

    while index < len(rows):
        if rows[index].strip().isalpha():
            name: str = rows[index].strip()
            index += 1
            row: str = rows[index]
            maze: list = []
            while row != "\n":
                maze.append([field for field in row.strip().split(" ")])
                index += 1
                row = rows[index]
            print(name)
            print(solve_maze(maze))
        index += 1