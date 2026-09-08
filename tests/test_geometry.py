import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from musclescope.geometry import Point2D, joint_angle


class JointAngleTests(unittest.TestCase):
    def test_right_angle(self) -> None:
        result = joint_angle(Point2D(1, 0), Point2D(0, 0), Point2D(0, 1))
        self.assertEqual(result, 90.0)

    def test_straight_angle(self) -> None:
        result = joint_angle(Point2D(-1, 0), Point2D(0, 0), Point2D(1, 0))
        self.assertEqual(result, 180.0)

    def test_overlapping_points_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            joint_angle(Point2D(0, 0), Point2D(0, 0), Point2D(1, 0))


if __name__ == "__main__":
    unittest.main()
