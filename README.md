# MuscleScope AI

面向力量训练的可解释动作分析与肌肉负荷估计项目。

这个仓库同时承担两个目标：

1. 从几乎零工程基础开始，训练真正的编程、调试和测试能力。
2. 长期研究“视频姿态 → 3D运动学 → 肌骨模型 → 肌肉激活/肌肉力估计”。

> 项目必须区分视频观测、模型估计和传感器测量。普通视频不能直接看见深层肌肉，本项目不提供医疗诊断。

## 当前里程碑：M0

先完成一个纯 Python 的“关节角度分析器”：

- 读取 JSON 文件中的三个二维关键点。
- 计算夹角。
- 对非法输入给出可读错误。
- 把结果写到 JSON 文件。
- 用自动测试验证 90°、180°和异常情况。

M0 不使用 AI 模型，也不使用 FastAPI、Spring Boot、NumPy 或 OpenCV。目的是先掌握以后所有模块都需要的基础能力。

## 仓库结构

```text
musclescope-ai/
├─ README.md
├─ docs/
│  ├─ ROADMAP.md
│  └─ WEEK_01.md
├─ src/
│  └─ musclescope/
│     ├─ __init__.py
│     ├─ geometry.py
│     └─ cli.py
├─ exercises/
│  └─ week01_tasks.py
├─ examples/
│  └─ angle_input.json
└─ tests/
   └─ test_geometry.py
```

## 第一周完成后的运行方式

```powershell
python -m unittest discover -s tests -v
python -m src.musclescope.cli examples/angle_input.json result.json
```

## 学习规则

- 每次看课最多连续30分钟，随后必须自己写代码。
- 不复制参考实现；先做 `exercises`，卡住20分钟后再查资料。
- 每道练习写出输入、输出、边界情况和时间复杂度。
- Codex可以解释错误、审查和出提示，但不要直接让它完成整周作业。
- 每天结束做一次小提交，提交信息说明“做了什么”，不要写 `update`。

## 当前范围

本仓库只保存源代码、文档和小型匿名示例，不保存视频、用户数据、虚拟环境、数据集或模型权重。