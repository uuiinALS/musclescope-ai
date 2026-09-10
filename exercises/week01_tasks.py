"""第1周练习。先自己完成TODO，再查看src中的参考实现。"""

import math


def add(a: float, b: float) -> float:
    return a + b


def maximum(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("numbers 不能为空")

    j = numbers[0]
    for value in numbers:
        if j < value:
            j = value
    return j


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    x = x1 - x2
    y = y1 - y2
    a = x * x + y * y
    return math.sqrt(a)


def parse_point(data: dict[str, object]) -> tuple[float, float]:
    """检查一个点，返回浮点坐标；非法坐标抛出 ValueError。"""
    try:
        x = data["x"]
        y = data["y"]
    except KeyError as e:
        raise ValueError(f"缺少坐标：{e}") from e

    # 精确接受内置 int/float，因此不接受 bool 或数字字符串。
    if type(x) not in (int, float) or type(y) not in (int, float):
        raise ValueError("坐标类型不正确：x 和 y 必须是整数或浮点数")

    return float(x), float(y)


def calculate_angle(first: tuple[float, float], vertex: tuple[float, float], third: tuple[float, float]) -> float:
    # TODO(day5): 用点积公式实现，不调用src里的joint_angle
    raise NotImplementedError


if __name__ == "__main__":
    # 辅导补充：原题要求的三次调用，预期依次输出 5、-2、5.0。
    print(add(2, 3))
    print(maximum([-4, -2, -7]))
    print(distance(0, 0, 3, 4))
