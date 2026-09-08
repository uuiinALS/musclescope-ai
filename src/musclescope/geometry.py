from dataclasses import dataclass
from math import acos, degrees, hypot


@dataclass(frozen=True)
class Point2D:
    x: float
    y: float


def joint_angle(first: Point2D, vertex: Point2D, third: Point2D) -> float:
    """计算 first-vertex-third 形成的较小夹角，单位为度。"""
    vector_a = (first.x - vertex.x, first.y - vertex.y)
    vector_b = (third.x - vertex.x, third.y - vertex.y)
    denominator = hypot(*vector_a) * hypot(*vector_b)
    if denominator == 0:
        raise ValueError("关键点重合，无法计算角度")

    cosine = (vector_a[0] * vector_b[0] + vector_a[1] * vector_b[1]) / denominator
    cosine = max(-1.0, min(1.0, cosine))
    return round(degrees(acos(cosine)), 1)
