"""Day 3：学习者原稿的辅导修正版。
从仓库根目录运行：python exercises/day03_json.py
输出文件会被覆盖。删除、逐点输出和 KeyError 处理由辅导补充，需独立复写验收。
"""

import json

with open("examples/angle_input.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for name in ("first", "vertex", "third"):
    point = data[name]
    print(name, point["x"], point["y"])

result = {"angle_degrees": 90.0}
with open("exercises/day03_result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

# 只删除副本的顶层键，不修改原始 data。
data1 = data.copy()
del data1["vertex"]

with open("exercises/copy.json", "w", encoding="utf-8") as f:
    json.dump(data1, f, ensure_ascii=False, indent=4)

with open("exercises/copy.json", "r", encoding="utf-8") as f:
    copied_data = json.load(f)

try:
    print(copied_data["vertex"])
except KeyError as e:
    print(f"缺少必要的关节点：{e}")
