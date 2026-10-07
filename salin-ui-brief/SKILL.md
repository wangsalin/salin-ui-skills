---
name: "salin-ui-brief"
description: "UI 需求定义：把一句话需求拆成页面定义文件（_workbench/spec.md），每个区块对应解决一个具体的用户问题。适用于新页面/新项目开工前、AI 搭页面之前，先把'做什么'定死。后续的设计、实现、改版都基于这份 spec，不再回头问需求。"
---

# Salin UI Brief · 需求定义

## Purpose
AI 搭页面翻车，第一因不是审美，是"不知道这页要解决什么"——区块堆在一起，每个区块都不知道自己为什么存在。本 skill 把一句话需求翻译成页面定义文件 `_workbench/spec.md`：页面结构 + 内容关系，每个区块必须对应一个用户问题。spec 是后续所有工作的唯一需求源。

蒸馏自 @西瓜同学🍉《第18集 | 3个UI设计Skills工作流，让AI做出高级网页》的 /finesse-brief：需求一句话 → 输出 spec.md → 定方向、搭页面、改细节全基于这份定义往下做。

## Workflow
1. **收需求**：只收一句话——"做什么 + 给谁看"。不写细节、不聊风格。细节现在写了也是猜。
2. **拆问题**：把这句话翻译成用户带着哪几个问题来这个页面（参考：参加什么 / 有多难 / 到哪了 / 还差几步）。
3. **定区块**：每个问题对应一个区块，一一列出：区块名 → 回答的用户问题 → 内容要点 → 优先级（P0 必有 / P1 重要 / P2 可砍）。
4. **写 spec**：按 `references/spec-template.md` 输出 `_workbench/spec.md`，含"不做清单"（明确写出这次不解决什么）。
5. **过质量门**：用 Operating Rules 自查，说不出解决哪个问题的区块直接删。
6. **交付**：spec 经用户确认后落盘；后续设计（salin-style-library / salin-ui-layout）、实现（salin-app-ui / salin-web-ui）、动效（salin-ui-motion）都基于 spec 开工。需求变更先改 spec 再动手，不许私自加区块。

## Output Contract
- 文件：`_workbench/spec.md`（模板见 `references/spec-template.md`）
- 必备字段：页面一句话目标 / 目标用户 / 区块表（区块 | 用户问题 | 内容要点 | 优先级）/ 不做清单
- 一句话"页面定义摘要"（纯文本，给后续 skill 当输入用，不用翻文件）

## Operating Rules
1. 需求只收一句话；用户开始写细节时打住——细节是拆问题的事，不是现在定的事。
2. 区块与用户问题严格 1:1：一个区块回答两个问题就拆成两个；一个问题没人回答就补区块。
3. 说不出"它解决用户哪个问题"的区块，删。宁可页面短，不可区块空。
4. spec 落盘前必须经用户确认；确认后它是唯一需求源，设计实现阶段不许私自加区块、改问题。
5. 不做视觉判断、不定风格、不写交互细节——那是 salin-style-library / salin-ui-layout / salin-ui-motion 的活，本 skill 越界即错。
