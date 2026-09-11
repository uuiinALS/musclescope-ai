"""D6：学习者测试的修正版；补充0度、120度及交换/缩放性质。"""
import unittest

from exercises.week01_tasks import calculate_angle


class TestAngle(unittest.TestCase):
    def test_180_degrees(self):
        self.assertAlmostEqual(calculate_angle((-1, 0), (0, 0), (1, 0)), 180)

    def test_45_degrees(self):
        self.assertAlmostEqual(calculate_angle((1, 0), (0, 0), (1, 1)), 45)

    def test_first(self):
        with self.assertRaises(ValueError):
            calculate_angle((0, 0), (0, 0), (1, 0))

    def test_third(self):
        with self.assertRaises(ValueError):
            calculate_angle((0, 0), (1, 0), (1, 0))

    def test_move(self):
        self.assertAlmostEqual(calculate_angle((11, 10), (10, 10), (10, 11)), 90)

    def test_90_degrees(self):
        self.assertAlmostEqual(calculate_angle((1, 0), (0, 0), (0, 1)), 90)

    def test_zero_degrees(self):
        self.assertAlmostEqual(calculate_angle((1, 0), (0, 0), (2, 0)), 0)

    def test_obtuse_angle(self):
        self.assertAlmostEqual(calculate_angle((1, 0), (0, 0), (-1, 3 ** 0.5)), 120)

    def test_swapping_endpoints_preserves_angle(self):
        first, vertex, third = (2, 3), (-1, 1), (4, -2)
        self.assertAlmostEqual(
            calculate_angle(first, vertex, third),
            calculate_angle(third, vertex, first),
        )

    def test_scaling_preserves_angle(self):
        self.assertAlmostEqual(
            calculate_angle((1, 0), (0, 0), (1, 1)),
            calculate_angle((3, 0), (0, 0), (3, 3)),
        )


if __name__ == "__main__":
    unittest.main()
