---
name: "salin-ui-components"
description: "Salin UI 组件设计规范库：12 个高频组件（按钮/输入框/卡片/弹窗/标签页/导航栏/表格/徽标标签/轻提示/下拉选择/开关复选/进度条），每个给变体、尺寸、状态、App/Web 双端差异、无障碍要求和用法红线，关键词检索。用于设计或评审单个组件；按规范实现时配合 salin-app-ui / salin-web-ui，动效查 salin-ui-motion，shadcn 工程实现走 salin-shadcn-ui。"
---

# Salin UI Components · 组件设计规范库

## Purpose
回答"这个组件该长什么样"：12 个最高频组件的设计规格——变体怎么选、尺寸多少、状态有哪些、App 和 Web 有什么不一样、红线在哪。用数据检索，不凭感觉。

## Workflow
1. 确定要设计/评审的组件（如"提交按钮""数据表"）。
2. 跑检索：`python scripts/search.py "<组件名/场景>" --full`，读完整规格。
3. 按规格选变体：先看"红线"排除错误用法，再按 App/Web 差异定尺寸。
4. 状态全覆盖：default / hover / active / disabled / loading / error，一个不少；缺的问用户补业务定义，不虚构。
5. 动效需求 → 查 `salin-ui-motion` 对应模式；视觉 token（颜色/字号）→ 查对应风格的 MASTER.md 或 `salin-style-library`。

## Query Contract
- 查询词 2–4 个：组件名 + 场景，如"提交按钮""表格 订单""开关 设置页"。
- 一次只查一个组件；页面级需求先走 salin-app-ui / salin-web-ui 定页面类型，再回来查组件。
- 检索无命中时直接说"库里没有这个组件"，不许编造规格。

## 组件清单（v1，12 个）
按钮 button / 输入框 input / 卡片 card / 弹窗 dialog / 标签页 tabs / 导航栏 navigation / 表格 table / 徽标标签 badge-tag / 轻提示 toast / 下拉选择 select / 开关复选 switch-checkbox / 进度条 progress

## Operating Rules
1. 变体选择必须给理由（"为什么用 Secondary 而不用 Ghost"），不许"看着顺眼"。
2. 尺寸必须写具体数值，App/Web 分开写，不许一套尺寸通吃两端。
3. 每个组件交付时必须列出：所用变体、尺寸、全部状态、无障碍检查结论、命中的红线（无则写"无"）。
4. 加新组件 = 在 `data/components.csv` 加一行（字段对齐表头），不许改脚本结构。
5. 组件规范与页面模式冲突时（如 card 在 dashboard 里的用法），以页面 skill 为准，组件库只给组件本体规范。
