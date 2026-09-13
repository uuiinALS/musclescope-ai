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
    """检查一个点；D8辅导修正检查顺序，非法坐标向调用者抛出ValueError。"""
    if not isinstance(data, dict):
        raise ValueError("点必须是字典")

    try:
        x = data["x"]
        y = data["y"]
    except KeyError as e:
        raise ValueError(f"缺少坐标：{e}") from e

    if x is None or y is None:
        raise ValueError("坐标不能为空")

    if type(x) not in (int, float) or type(y) not in (int, float):
        raise ValueError("坐标类型不正确：x 和 y 必须是整数或浮点数")

    x = float(x)
    y = float(y)
    if not math.isfinite(x) or not math.isfinite(y):
        raise ValueError("转换后坐标必须是有限数值")

    return x, y


def calculate_angle(first: tuple[float, float], vertex: tuple[float, float], third: tuple[float, float]) -> float:
    """返回两向量之间的较小夹角（度）；重合端点抛出 ValueError。"""
    # 保留学习者写法：两个向量同时反向，不改变夹角。
    x1 = vertex[0] - first[0]
    y1 = vertex[1] - first[1]
    x2 = vertex[0] - third[0]
    y2 = vertex[1] - third[1]
    uv = x1 * x2 + y1 * y2
    u = math.sqrt(x1 ** 2 + y1 ** 2)
    v = math.sqrt(x2 ** 2 + y2 ** 2)

    if u == 0 or v == 0:
        raise ValueError("顶点与端点重合，无法计算夹角")

    cosine = uv / (u * v)
    cosine = max(-1.0, min(1.0, cosine))
    radians = math.acos(cosine)
    angle = math.degrees(radians)
    return angle


def analyze_angle(data: dict[str, object]) -> dict[str, float]:
    """D9辅导修正版：分析一组三点，不修改输入，不执行文件读写。"""
    if not isinstance(data, dict):
        raise ValueError("输入数据必须是字典")

    try:
        first = data["first"]
        vertex = data["vertex"]
        third = data["third"]
    except KeyError as e:
        raise ValueError(f"缺少关节点：{e}") from e

    first1 = parse_point(first)
    vertex1 = parse_point(vertex)
    third1 = parse_point(third)
    result = calculate_angle(first1, vertex1, third1)
    return {"angle_degrees": result}


if __name__ == "__main__":
    # 辅导补充：原题要求的三次调用，预期依次输出 5、-2、5.0。
    print(add(2, 3))
    print(maximum([-4, -2, -7]))
    print(distance(0, 0, 3, 4))
