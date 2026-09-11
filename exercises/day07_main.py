"""D7第一轮：从仓库根目录运行 python exercises/day07_main.py。
主流程依据学习者原稿；main与异常分支为辅导补充。
输入错误时不打开输出文件，已有结果保持原样，不代表本次成功。
"""
import json

from week01_tasks import parse_point, calculate_angle


def main():
    try:
        with open("examples/angle_input.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        first = data["first"]
        vertex = data["vertex"]
        third = data["third"]

        first1 = parse_point(first)
        vertex1 = parse_point(vertex)
        third1 = parse_point(third)

        result = calculate_angle(first1, vertex1, third1)
    except FileNotFoundError:
        print("输入文件不存在，请检查路径")
        return
    except json.JSONDecodeError:
        print("JSON格式错误，请检查逗号和引号")
        return
    except KeyError as e:
        print(f"缺少关节点：{e}")
        return
    except ValueError as e:
        print(f"坐标不合法：{e}")
        return

    output = {"angle_degrees": result}
    with open("exercises/day07_result.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
    print(result)


if __name__ == "__main__":
    main()
