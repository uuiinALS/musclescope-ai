import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from exercises.week01_tasks import add, distance, maximum


class DayOneExerciseTests(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 1), -1)

    def test_maximum_supports_negative_numbers(self) -> None:
        self.assertEqual(maximum([-4, -2, -7]), -2)

    def test_maximum_rejects_empty_list(self) -> None:
        with self.assertRaises(ValueError):
            maximum([])

    def test_distance(self) -> None:
        self.assertEqual(distance(0, 0, 3, 4), 5.0)
        self.assertEqual(distance(1, 1, 1, 1), 0.0)


if __name__ == "__main__":
    unittest.main()
