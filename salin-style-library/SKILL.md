---
name: "salin-style-library"
description: "Salin UI 风格库 / 试衣间：6 套精调风格（石墨青柠/工业深蓝/霓虹暗夜/荧光柠檬/明黄市集/深色画廊），关键词检索 + 三旋钮（variance/motion/density）+ MASTER.md 项目级设计记忆持久化。用于新项目定视觉方向、多方向小样二选一。风格选定后由 salin-app-ui / salin-web-ui 按 MASTER.md 执行。"
---

# Salin Style Library · 风格库

## Purpose
解决"每次做 UI 都从零想风格"的问题：6 套精调风格可检索，三旋钮定调，选定后落盘为项目级 `MASTER.md`，后续所有 builder 按同一份设计记忆执行，不再各做各的。

## Workflow
1. 用一句话描述产品（行业/用户/调性），跑检索：
   `python scripts/search.py "<产品描述>" --top 3`
2. 给用户看 Top 3（每套一句话卖点 + 主色），让用户二选一或三选一。**不替用户定风格。**
3. 定旋钮：variance（1 保守–10 出挑）、motion（1 静谧–10 动感）、density（1 疏朗–10 紧凑）。默认 5/5/5；用户有明确倾向再调。
4. 落盘：`--persist -p "<项目名>" --output-dir <项目根目录>` 生成 `design-system/<slug>/MASTER.md`。
5. 把 MASTER.md 路径交给 builder（salin-app-ui / salin-web-ui），它们按此执行；动效需求按 MASTER.md 的 motion 旋钮路由到 salin-ui-motion 或 motion-gsap。

## Query Contract
- 查询词 2–5 个有意义的词：行业 + 用户 + 调性，如"美容会所 预约""工业设备 ToB""奶茶店 点单"。
- 零命中时自动回退默认风格（暖纸青墨），并明确告诉用户是回退。
- 风格的"不适用"字段是红线：命中了不适用场景必须换，不许硬套。

## MASTER.md 契约
- 一份 MASTER.md 只对应一个项目；已存在不覆盖（防丢已有决策），要换风格先删再跑。
- builder 必须完整读取 MASTER.md 后再动手；跨页面保持一致，有冲突以 MASTER.md 为准。
- 页面级微调走 `design-system/<slug>/pages/` 下的 override 文件，不改 MASTER.md。

## Operating Rules
1. 风格二选一必须用户拍板，不许代选；旋钮可以给推荐值。
2. 检索脚本只用标准库，不许加第三方依赖。
3. 加新风格 = 在 `data/styles.csv` 加一行（字段对齐表头），不许改脚本结构。
4. 风格描述必须写"不适用"场景；没有不适用场景的风格不许入库。
5. 需要更深层的风格/配色/字体依据时，查 `ui-ux-pro-max`（79 风格库）；本库只做"我们调过的 6 套"。
