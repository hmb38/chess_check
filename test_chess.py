import unittest
from chess import parse_concise_board


class TestAssertions(unittest.TestCase):

    def test_equals(self):
        self.assertEqual(1 + 1,   2)

    def test_parse_concise_board(self):
        board = (
            "..k.....",
            "........",
            "........",
            "........",
            "........",
            "........",
            "........",
            "....K..."
        )

        self.assertEqual(parse_concise_board(board), [
            {"type": "King", "colour": "White", "pos": {"x": 3, "y": 1}},
            {'type': 'King', 'colour': 'Black', 'pos': {'x': 5, 'y': 8}}
        ])


if __name__ == '__main__':
    unittest.main()
