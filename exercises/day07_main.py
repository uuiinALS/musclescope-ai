"""D7第二轮：命令行指定输入输出路径。

从仓库根目录运行：
python exercises/day07_main.py --input_path examples/angle_input.json --output_path exercises/day07_result.json

命令行参数由学习者提交；辅导者整理格式并运行测试。
输入错误时保留已有输出；退出码与更完整的输入校验留待D8。
"""
import argparse
import json

from week01_tasks import parse_point, calculate_angle


def main(input_path, output_path):
    try:
        with open(input_path, "r", encoding="utf-8") as f:
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
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
    print(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str, help="输入文件路径", required=True)
    parser.add_argument("--output_path", type=str, help="输出文件路径", required=True)
    args = parser.parse_args()
    main(args.input_path, args.output_path)
