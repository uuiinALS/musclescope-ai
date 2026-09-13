"""D7第二轮：命令行指定输入输出路径。

从仓库根目录运行：
python exercises/day07_main.py --input_path examples/angle_input.json --output_path exercises/day07_result.json

命令行参数由学习者提交；辅导者整理格式并运行测试。
D9辅导修正：调用analyze_angle，直接写入结果字典；不代表独立验收通过。
"""
import argparse
import json

from week01_tasks import analyze_angle


def main(input_path, output_path):
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        output = analyze_angle(data)
    except FileNotFoundError:
        print("输入文件不存在，请检查路径")
        return 1
    except json.JSONDecodeError:
        print("JSON格式错误，请检查逗号和引号")
        return 1
    except ValueError as e:
        print(f"输入数据不合法：{e}")
        return 1

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
    print(output["angle_degrees"])
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str, help="输入文件路径", required=True)
    parser.add_argument("--output_path", type=str, help="输出文件路径", required=True)
    args = parser.parse_args()
    raise SystemExit(main(args.input_path, args.output_path))
