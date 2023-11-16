import unittest
import numpy as np
from twentyFourtyEight import slide, merge
# Your slide and merge functions here

class TestSlideAndMerge(unittest.TestCase):
    def test_move_up(self):
        arr = np.array([[0, 2, 2, 0], [0, 4, 0, 4], [2, 0, 4, 2], [0, 0, 2, 0]])
        expected_result = np.array([[2, 2, 2, 4], [0, 4, 4, 2], [0, 0, 2, 0], [0, 0, 0, 0]])

        for x in range(4):
            arr[:,x] = slide(arr[:,x])
            arr[:,x] = merge(arr[:,x])
            arr[:,x] = slide(arr[:,x])

        self.assertTrue(np.array_equal(arr, expected_result))

    def test_move_down(self):
        arr = np.array([[0, 2, 2, 0], [0, 4, 0, 4], [2, 0, 4, 2], [0, 0, 2, 0]])
        expected_result = np.array([[0, 0, 0, 0], [0, 0, 2, 0], [0, 2, 4, 4], [2, 4, 2, 2]])


        for x in range(4):
            arr[:,x] = np.flip(slide(np.flip(arr[:,x])))
            arr[:,x] = np.flip(merge(np.flip(arr[:,x])))
            arr[:,x] = np.flip(slide(np.flip(arr[:,x])))

        self.assertTrue(np.array_equal(arr, expected_result))

    def test_move_right(self):
        arr = np.array([[0, 2, 2, 0], [0, 4, 0, 4], [2, 0, 4, 2], [0, 0, 2, 0]])
        expected_result = np.array([[0, 0, 0, 4], [0, 0, 0, 8], [0, 2, 4, 2], [0, 0, 0, 2]])

        for x in range(4):
            arr[x, :] = np.flip(slide(np.flip(arr[x, :])))
            arr[x, :] = np.flip(merge(np.flip(arr[x, :])))
            arr[x, :] = np.flip(slide(np.flip(arr[x, :])))

        self.assertTrue(np.array_equal(arr, expected_result))
    
    def test_move_left(self):
        arr = np.array([[0, 2, 2, 0], [0, 4, 0, 4], [2, 0, 4, 2], [0, 0, 2, 0]])
        expected_result = np.array([[4, 0, 0, 0], [8, 0, 0, 0], [2, 4, 2, 0], [2, 0, 0, 0]])

        for x in range(4):
            arr[x, :] = slide(arr[x, :])
            arr[x, :] = merge(arr[x, :])
            arr[x, :] = slide(arr[x, :])

        self.assertTrue(np.array_equal(arr, expected_result))

if __name__ == '__main__':
    unittest.main()