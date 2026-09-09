"""Day 2：根据学习者原稿审查修正。

在当前工作目录创建或覆盖 exercise.txt。
分别在 exercise02.txt 不存在和存在时运行，观察异常分支。
"""

with open("exercise.txt", "w", encoding="utf-8") as f:
    f.write("shoulder\n")
    f.write("hip\n")
    f.write("knee\n")

with open("exercise.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip("\n"))

try:
    with open("exercise02.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError as e:
    print(e)
    print("文件不存在，请检查路径")
