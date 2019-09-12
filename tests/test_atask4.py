import unittest

from atasks.atask4.atask4 import winning_player_index, Move


class TestATask3(unittest.TestCase):
    def test_atask4_win_vertical(self):
        board = [
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
        ]

        result = winning_player_index(board, Move(0, 4, 3))
        self.assertEqual(0, result)

        board = [
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, -1, -1],
        ]

        result = winning_player_index(board, Move(0, 4, 4))
        self.assertEqual(0, result)

        board = [
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
        ]

        result = winning_player_index(board, Move(0, 4, 2))
        self.assertEqual(0, result)

        board = [
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, 0, -1],
        ]

        result = winning_player_index(board, Move(0, 4, 2))
        self.assertEqual(-1, result)

    def test_atask4_win_horizontal(self):
        board = [
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
            [1, 1, 1, 1, 0, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
        ]

        result = winning_player_index(board, Move(1, 0, 3))
        self.assertEqual(1, result)

        board = [
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
            [0, 1, 1, 1, 1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
        ]

        result = winning_player_index(board, Move(1, 4, 3))
        self.assertEqual(1, result)

        board = [
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
            [1, -1, 1, 1, 1, 1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
        ]

        result = winning_player_index(board, Move(1, 5, 3))
        self.assertEqual(1, result)

        board = [
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
            [1, 1, 0, 0, 0, 1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
        ]

        result = winning_player_index(board, Move(1, 5, 3))
        self.assertEqual(-1, result)

    def test_atask4_win_forward_slash(self):
        board = [
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, 2, 0, -1],
            [1, 1, 2, 1, 0, -1],
            [-1, 2, -1, -1, -1, -1],
            [2, -1, -1, -1, -1, -1],
        ]

        result = winning_player_index(board, Move(2, 0, 5))
        self.assertEqual(2, result)

        board = [
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, -1, -1, 2, -1],
            [-1, -1, -1, 2, 0, -1],
            [1, 1, 2, 1, 0, -1],
            [-1, 2, -1, -1, -1, -1],
            [1, -1, -1, -1, -1, -1],
        ]

        result = winning_player_index(board, Move(2, 3, 2))
        self.assertEqual(2, result)

        board = [
            [-1, -1, -1, -1, 2, -1],
            [-1, -1, -1, 2, 0, -1],
            [-1, -1, 2, -1, 0, -1],
            [1, 2, 1, 1, 0, -1],
            [-1, 1, -1, -1, -1, -1],
            [2, -1, -1, -1, -1, -1],
        ]

        result = winning_player_index(board, Move(2, 0, 4))
        self.assertEqual(2, result)

        board = [
            [-1, -1, -1, -1, 2, -1],
            [-1, -1, -1, -1, 0, -1],
            [-1, -1, 2, -1, 0, -1],
            [1, 1, -1, 1, 0, -1],
            [-1, 2, -1, -1, -1, -1],
            [2, -1, -1, -1, -1, -1],
        ]

        result = winning_player_index(board, Move(2, 0, 4))
        self.assertEqual(-1, result)

    def test_atask4_win_backward_slash(self):
        board = [
            [3, -1, -1, -1, 0, -1],
            [-1, 3, -1, -1, 0, -1],
            [-1, -1, 3, -1, 0, -1],
            [1, 1, 2, 3, 0, -1],
            [-1, 2, -1, -1, -1, -1],
            [2, -1, -1, -1, -1, -1],
        ]

        result = winning_player_index(board, Move(3, 0, 0))
        self.assertEqual(3, result)

        board = [
            [-1, -1, -1, -1, 0, -1],
            [-1, 3, -1, -1, 0, -1],
            [-1, -1, 3, -1, 0, -1],
            [1, 1, 2, 3, 0, -1],
            [-1, 2, -1, -1, 3, -1],
            [2, -1, -1, -1, -1, -1],
        ]

        result = winning_player_index(board, Move(3, 3, 3))
        self.assertEqual(3, result)

        board = [
            [3, -1, -1, -1, 0, -1],
            [-1, 0, -1, -1, 0, -1],
            [-1, -1, 3, -1, 0, -1],
            [1, 1, 2, 3, 0, -1],
            [-1, 2, -1, -1, 3, -1],
            [2, -1, -1, -1, -1, 3],
        ]

        result = winning_player_index(board, Move(3, 5, 5))
        self.assertEqual(3, result)

        board = [
            [3, -1, -1, -1, 0, -1],
            [-1, 3, -1, -1, 0, -1],
            [-1, -1, -1, -1, 0, -1],
            [1, 1, 2, 3, 0, -1],
            [-1, 2, -1, -1, -1, -1],
            [2, -1, -1, -1, -1, 3],
        ]

        result = winning_player_index(board, Move(3, 3, 3))
        self.assertEqual(-1, result)
