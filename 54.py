
from typing import List
from enum import Enum
import unittest

class Direction(Enum):
    RIGHT=0
    DOWN=1
    LEFT=2
    UP=3

DirectionToMoves = {
    Direction.RIGHT:(0,1), 
    Direction.DOWN:(1,0), 
    Direction.LEFT: (0,-1), 
    Direction.UP:(-1,0)
    }
    
class Solution:
    max_rows = 0
    max_columns = 0


    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix or not matrix[0]:
            return []
        
        self.max_rows = len(matrix)
        self.max_columns = len(matrix[0])
        
        visited = [[False for _ in range(self.max_columns)] for _ in range(self.max_rows)]
        answer = []

        current_dir = Direction.RIGHT
        obstacles = 0 
        current_row =0 
        current_column =0 
        visited[current_row][current_column] = True
        answer.append(matrix[current_row][current_column])
        while obstacles <= 1:
            move = DirectionToMoves[current_dir]
            next_row = current_row + move[0] 
            next_column = current_column + move[1]
            if self.is_wall(next_row, next_column) or visited[next_row][next_column]:
                obstacles += 1
                current_dir_int = (current_dir.value)
                current_dir_int = (current_dir_int + 1) % 4
                if current_dir_int == 0:
                    current_dir = Direction.RIGHT
                elif current_dir_int == 1:
                    current_dir = Direction.DOWN
                elif current_dir_int == 2:
                    current_dir = Direction.LEFT
                else:
                    current_dir = Direction.UP
            else:
                current_row = next_row
                current_column = next_column
                visited[current_row][current_column] = True            
                answer.append(matrix[current_row][current_column])
                obstacles = 0
        return answer
            
    
    def is_wall(self, row, column) -> bool:
        return (
            row >= self.max_rows 
            or row < 0 
            or column >= self.max_columns 
            or column <0
        )
# Testing class
class TestSpiralOrder(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_spiral_order_1(self):
        self.assertEqual(self.solution.spiral_order([[1]]), [1])

    def test_spiral_order_2(self):
        self.assertEqual(self.solution.spiral_order([[1, 2], [3, 4]]), [1, 2, 4, 3])

    def test_spiral_order_3(self):
        self.assertEqual(self.solution.spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_spiral_order_4(self):
        self.assertEqual(self.solution.spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])

    def test_spiral_order_empty(self):
        self.assertEqual(self.solution.spiral_order([]), [])

    def test_spiral_order_single_row(self):
        self.assertEqual(self.solution.spiral_order([[1, 2, 3]]), [1, 2, 3])

    def test_spiral_order_single_column(self):
        self.assertEqual(self.solution.spiral_order([[1], [2], [3]]), [1, 2, 3])
'''
def main():
    import sys
    # If run as a script, run the tests
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        unittest.main()
    sol = Solution()
    answer = sol.spiral_order([[0,2,3],[4,5,5]])
    print(answer)
'''



if __name__=="__main__":
    unittest.main()