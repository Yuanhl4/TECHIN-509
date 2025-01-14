board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

def flood_fill(input_board, old, new, x, y):
    a, b = len(input_board), len(input_board[0])
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()
        if (
            0 <= x < a
            and 0 <= y < b
            and input_board[x][y] == old
        ):
            input_board[x] = input_board[x][:y] + new + input_board[x][y + 1:]
            stack.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])

    return input_board

#Example
result_board = flood_fill(board, old = ".", new = "~", x=5, y=11)

for row in result_board:
    print(row)

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

def flood_fill(input_board, old, new, x, y):
    a, b = len(input_board), len(input_board[0])
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()
        if (
            0 <= x < a
            and 0 <= y < b
            and input_board[x][y] == old
        ):
            input_board[x] = input_board[x][:y] + new + input_board[x][y + 1:]
            stack.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])

    return input_board

#Example
result_board = flood_fill(board, old = ".", new = "~", x=1, y=1)

for row in result_board:
    print(row)
