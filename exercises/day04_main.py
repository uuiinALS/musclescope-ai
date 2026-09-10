"""Day 4 调用示例（辅导补充）。
从仓库根目录运行：python exercises/day04_main.py
"""

from week01_tasks import parse_point


if __name__ == "__main__":
    cases = [
        {"x": 1, "y": 2},
        {"x": -2.5, "y": 3},
        {"x": 1},
        {"x": "1", "y": 2},
        {"x": True, "y": 0},
        {"x": 1, "y": 2, "name": "hip"},
    ]
    for data in cases:
        try:
            print(parse_point(data))
        except ValueError as e:
            print(e)
