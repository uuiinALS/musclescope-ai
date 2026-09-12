# MuscleScope AI

面向力量训练的可解释动作分析、肌肉负荷估计与受控教练Agent。

长期证据链：

```text
视频观测 → 2D/3D运动学 → 个体化肌骨模型 → 肌肉激活/肌肉力估计
                                      ↘ 结构化结果 → 教练Agent解释与工具调用
```

> 必须区分视频观测、模型估计和传感器测量。普通视频不能直接看见深层肌肉；本项目不提供医疗诊断。

## 当前里程碑：M0

先完成纯Python“关节角度分析器”：

- 读取JSON中的三个二维关键点
- 计算夹角
- 处理非法输入
- 输出结果JSON
- 使用自动测试验证边界

M0不使用AI模型、FastAPI、Spring Boot、NumPy或OpenCV。目的是先建立以后所有模块依赖的编程能力。

## 关键文档

- [项目战略与技术边界](docs/PROJECT_STRATEGY.md)
- [简历量化证据账本](docs/INTERVIEW_EVIDENCE.md)
- [16周学习路线](docs/ROADMAP.md)
- [第1周逐日计划](docs/WEEK_01.md)
- [跨对话学习上下文](docs/LEARNING_CONTEXT.md)
- [隐含情感回应Agent候选想法](ideas/emotion-aware-response-agent.md)

## 仓库结构

```text
docs/        路线、决策、指标和学习上下文
ideas/       尚未立项的候选产品
src/         正式可复用代码
exercises/   学习者亲手完成的练习
examples/    小型匿名示例
tests/       自动测试
```

## 第一周运行方式

```powershell
python -m unittest discover -s tests -v
python -m src.musclescope.cli examples/angle_input.json result.json
```

## 学习和真实性规则

- 每看课最多30分钟，随后必须编码。
- 先做`exercises`，卡住20分钟后再查资料。
- Codex优先解释、提示和审查，不代写整周作业。
- 每天做小提交并记录错误。
- 简历只写已经存在的代码、部署和实验；规划功能不得包装成已完成。
- 所有量化结果必须能指向脚本、数据版本或日志。

## 存储范围

仓库只保存源码、文档和小型匿名示例，不保存用户视频、隐私数据、虚拟环境、数据集或模型权重。