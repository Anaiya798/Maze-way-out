import numpy as np
import unittest
from src.main import*

class BfsTest(unittest.TestCase):
    def test_matrix_2_3(self):
        maze = np.array([
            [0, 1, 0],
            [0, 0, 1]
        ])
        start_point = (1, 0)
        self.assertEqual(bfs(maze, 2, 3, start_point[0], start_point[1]), 0)

    def test_matrix_4_4(self):
        maze = np.array([
            [1, 1, 1, 0],
            [1, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 1]
        ])
        start_point = (1, 1)
        self.assertEqual(bfs(maze, 4, 4, start_point[0], start_point[1]), 2)

    def test_matrix_5_3(self):
        maze = np.array([
            [1, 1, 1, 0],
            [1, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 1]
        ])
        start_point = (1, 1)
        self.assertEqual(bfs(maze, 4, 4, start_point[0], start_point[1]), 2)

    def test_matrix_7_7(self):
        maze = np.array([
            [0, 0, 1, 1, 1, 0, 0],
            [0, 1, 0, 0, 0, 1, 1],
            [1, 0, 1, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 0, 1],
            [0, 0, 0, 1, 1, 0, 1]
        ])
        start_point = (3, 3)
        self.assertEqual(bfs(maze, 7, 7, start_point[0], start_point[1]), 5)
        start_point = (1, 2)
        self.assertEqual(bfs(maze, 7, 7, start_point[0], start_point[1]), NO_WAY_MARK)

    def test_matrix_9_12(self):
        maze = np.array([
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
            [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
            [0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0],
            [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
            [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0]
        ])
        start_point = (2, 6)
        self.assertEqual(bfs(maze, 9, 12, start_point[0], start_point[1]), 3)
        start_point = (5, 4)
        self.assertEqual(bfs(maze, 9, 12, start_point[0], start_point[1]), NO_WAY_MARK)




if __name__ == '__main__':
    unittest.main()
