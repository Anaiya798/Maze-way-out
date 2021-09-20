import numpy as np

INF = 1e9
NO_WAY_MARK = -1


def generate_maze(n, m):
    maze = np.array([np.random.randint(0, 2, (n, m))]).reshape(n, m)
    while all(maze[i][j] for i, j in zip(range(maze.shape[0]), range(maze.shape[1]))):  # degenerate case
        maze = np.array([np.random.randint(0, 2, (n, m))]).reshape(n, m)
    return maze


def bfs(maze, n, m, start_row, start_col):
    dist = np.array([INF] * n * m).reshape(n, m)
    dist[start_row][start_col] = 0
    queue = [(start_row, start_col)]

    while len(queue) != 0:
        row = queue[0][0]
        col = queue[0][1]
        queue.pop(0)
        if row + 1 < dist.shape[0]:
            if maze[row + 1][col] == 0 and dist[row + 1][col] == INF:
                dist[row + 1][col] = dist[row][col] + 1
                queue.append((row + 1, col))
        if col + 1 < dist.shape[1]:
            if maze[row][col + 1] == 0 and dist[row][col + 1] == INF:
                dist[row][col + 1] = dist[row][col] + 1
                queue.append((row, col + 1))
        if row - 1 >= 0:
            if maze[row - 1][col] == 0 and dist[row - 1][col] == INF:
                dist[row - 1][col] = dist[row][col] + 1
                queue.append((row - 1, col))
        if col - 1 >= 0:
            if maze[row][col - 1] == 0 and dist[row][col - 1] == INF:
                dist[row][col - 1] = dist[row][col] + 1
                queue.append((row, col - 1))

    res1 = min(dist[0][j] for j in range(dist.shape[1]))
    res2 = min(dist[n - 1][j] for j in range(dist.shape[1]))
    res3 = min(dist[i][0] for i in range(dist.shape[0]))
    res4 = min(dist[i][n-1] for i in range(dist.shape[0]))

    result = min(res1, res2, res3, res4)
    if result == INF:
        print("No way out of maze from this start point")
        return NO_WAY_MARK
    else:
        return result


if __name__ == '__main__':
    n = int(input("Number of maze rows: "))
    m = int(input("Number of maze columns: "))
    maze = generate_maze(n, m)

    print("============")
    print("Here is the maze. Zeroes stands for free entries, ones stands for walls: \n", maze)
    print("============")

    start_row = int(input("Row of the start point: ")) - 1
    start_col = int(input("Column of the start point: ")) - 1

    if maze[start_row][start_col] == 1:
        raise ValueError("It's a wall! Be more attentive!")
    if start_row < 1 or start_row >= maze.shape[0] or start_col < 1 or start_col >= maze.shape[1]:
        raise ValueError("Point out of the maze!")

    print("Shortest way to exit: ", bfs(maze, n, m, start_row, start_col))
