---
name: salin-ui
description: UI 设计一站式：从一句话需求到可交付页面的完整工作流。只读这一个 SKILL.md 就能开工，8 步自动编排（需求→风格→布局→组件→术语→实现→动效→验收），移动端 App/小程序、桌面端网页、数据看板全覆盖。蒸馏自 @西瓜同学🍉、@叨叨AI 等抖音 UI 博主方法论，经 109 条 evals 与 48/48 benchmark 验证。
---

# Salin UI · 一套 UI 设计

## 一句话开工
用户说"做个 X 页面 / 改版 Y / 加个动效 / 审查 Z" → **直接走下面的 8 步工作流，不要问、不要分 skill**。开工前先花 30 秒读 `references/09-routing.md` 确认启用哪些模块，再进第 1 步。唯一停下来问用户的时机：第 1 步 spec 确认、第 2 步风格二选一。

## 工作流（8 步，顺序执行，不许跳步）

| 步 | 做什么 | 读什么 | 产出 |
|---|---|---|---|
| 1 需求 | 一句话→用户问题→区块表→不做清单 | `references/01-brief.md`（脚手架：`scripts/spec.py`） | `_workbench/spec.md` + 用户确认 |
| 2 风格 | 检索风格→三旋钮→用户二选一 | `references/02-style.md` + `data/styles.csv`（检索：`scripts/style-search.py`） | `MASTER.md`（项目设计记忆） |
| 3 布局 | 查 24 种布局定骨架 | `references/03-layout.md` + `data/layouts.csv` | Layout Spec（模式/分区/栅格/断点/状态） |
| 4 组件 | 查 12 高频组件规范 | `data/components.csv` | 组件清单（变体/尺寸/状态） |
| 5 术语 | 大白话→设计术语（标出处） | `data/terms.csv`（53 条） | 术语统一表 |
| 6 实现 | 按端实现真实页面 | `references/04-implement-app.md` 或 `05-implement-web.md`；看板用 `06-dashboard.md`；shadcn 工程用 `07-shadcn.md` | 页面代码（含全部状态） |
| 7 动效 | 查 60 种模式落参数 | `data/motions.csv`（检索：`scripts/motion-search.py`） | 动效实现（一屏最多 2 种） |
| 8 验收 | WCAG 5 硬门 + 关键路径走查 | `references/08-audit.md`（机械检查：`scripts/audit-check.py`，人工走查不可省） | 验收结论（P0–P3） |

路由细节与"只做单步"的情况见 `references/09-routing.md`。

## 铁律（不读 reference 也必须遵守）
- 移动端触控目标 ≥ 44px，主操作放拇指热区；桌面端 8pt 网格、内容宽 1200–1440px、可点击 ≥ 32px 且有悬停态。
- 组件一律圆角（App 卡片 16px / 按钮 12px）；禁用紫蓝渐变、玻璃拟态、大面积渐变背景。
- 术语必须标出处（视频原话 / 推荐译法），**不编造英文术语**；查不到就用中文 + 行为描述。
- 动效时长写具体数值（150–200 / 200–300 / 300–400ms 三档），尊重 `prefers-reduced-motion`。
- 数字、积分、百分比一律 tabular-nums 等宽。
- 一屏一主角；空状态不留白（给 3 张建议卡或快捷入口）。
- 有品牌 VI 的项目，品牌优先于默认风格。

## 交付契约
每次交付必须附**调用清单**（用户会抽查）：
- 走了哪几步、每步读了哪个文件
- 用的哪条规则/哪个模式编号（如 motion #50）
- 哪几步跳过、为什么跳过

## 输入输出
- 输入：用户的一句话需求。细节缺失可标明假设后继续，不许为凑完整反复追问。
- 输出：可运行的页面/代码 + 调用清单 + 验收结论。只给方案不给实现时明确说明。
- `evals/` 是 skill 自身的质量回归题库（开发者跑分用），日常使用者不用读。
