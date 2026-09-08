import json
import sys
from pathlib import Path

from .geometry import Point2D, joint_angle


def parse_point(value: object, name: str) -> Point2D:
    if not isinstance(value, dict):
        raise ValueError(f"{name} 必须是包含 x、y 的对象")
    try:
        x = float(value["x"])
        y = float(value["y"])
    except (KeyError, TypeError, ValueError) as error:
        raise ValueError(f"{name}.x 和 {name}.y 必须是数字") from error
    return Point2D(x, y)


def run(input_path: Path, output_path: Path) -> float:
    with input_path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise ValueError("JSON最外层必须是对象")

    angle = joint_angle(
        parse_point(data.get("first"), "first"),
        parse_point(data.get("vertex"), "vertex"),
        parse_point(data.get("third"), "third"),
    )
    result = {"angle_degrees": angle}
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=2)
    return angle


def main() -> int:
    if len(sys.argv) != 3:
        print("用法: python -m src.musclescope.cli 输入.json 输出.json")
        return 2
    try:
        angle = run(Path(sys.argv[1]), Path(sys.argv[2]))
    except FileNotFoundError:
        print("错误：输入文件不存在")
        return 1
    except json.JSONDecodeError:
        print("错误：输入文件不是合法JSON")
        return 1
    except ValueError as error:
        print(f"错误：{error}")
        return 1
    print(f"关节角度：{angle}°")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
