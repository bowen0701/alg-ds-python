"""The maze search problem."""
from __future__ import print_function
import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze(object):
    def __init__(self, maze_filename):
        rows_in_maze = 0
        cols_in_maze = 0
        self.maze_list = []
        maze_file = open(maze_filename, 'r')
        rows_in_maze = 0

        for line in maze_file:
            row_list = []
            col = 0
            for ch in line[:-1]:
                row_list.append(ch)
                if ch == 'S':
                    self.start_row = rows_in_maze
                    self.start_col = col
                col += 1
            rows_in_maze += 1
            self.maze_list.append(row_list)
            cols_in_maze = len(row_list)

        self.rows_in_maze = rows_in_maze
        self.cols_in_maze = cols_in_maze
        self.x_translate = -cols_in_maze / 2
        self.y_translate = rows_in_maze / 2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(
            -(cols_in_maze - 1) / 2 - .5,
            -(rows_in_maze - 1) / 2 - .5,
            (cols_in_maze - 1) / 2 + .5,
            (rows_in_maze - 1) / 2 + .5)

    def draw_maze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rows_in_maze):
            for x in range(self.cols_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(
                        x + self.x_translate,
                        -y + self.y_translate,
                        'yellow')
        self.t.color('black')
        self.t.fillcolor('blue')
        self.wn.update()
        self.wn.tracer(1)

    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x - .5, y - .5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()

        for i in range(4):
            self.t.forward(1)
            self.t.right(90)

        self.t.end_fill()

    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(
            self.t.towards(x + self.x_translate,
                           -y + self.y_translate))
        self.t.goto(x + self.x_translate, 
                    -y + self.y_translate)

    def drop_breadcrumb(self, color):
        self.t.dot(10, color)

    def update_position(self, row, col, val=None):
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.drop_breadcrumb(color)

    def is_exit(self, row, col):
        return (row == 0 or
                row == self.rows_in_maze - 1 or
                col == 0 or
                col == self.cols_in_maze - 1)

    def __getitem__(self, idx):
        return self.maze_list[idx]


def dfs_from(maze, start_row, start_col):
    maze.update_position(start_row, start_col)
    # Check for base cases:
    # 1. We have run into an obstacle, return False.
    if maze[start_row][start_col] == OBSTACLE:
        return False
    # 2. We have found a square that has already been explored.
    if maze[start_row][start_col] == TRIED:
        return False
    # 3. Success, an outside edge not occupied by an obstacle.
    if maze.is_exit(start_row, start_col):
        maze.update_position(start_row, start_col, PART_OF_PATH)
        return True
    maze.update_position(start_row, start_col, TRIED)

    # Otherwise, use logical short circuiting to try each direction
    # in turn, if needed.
    found_bool = (
        dfs_from(maze, start_row - 1, start_col) or
        dfs_from(maze, start_row + 1, start_col) or
        dfs_from(maze, start_row, start_col - 1) or
        dfs_from(maze, start_row, start_col + 1))

    if found_bool:
        maze.update_position(start_row, start_col, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_col, DEAD_END)

    return found_bool

def main():
    maze = Maze('maze_file.txt')
    maze.draw_maze()
    maze.update_position(maze.start_row, maze.start_col)
    dfs_from(maze, maze.start_row, maze.start_col)


if __name__ == '__main__':
    main()
