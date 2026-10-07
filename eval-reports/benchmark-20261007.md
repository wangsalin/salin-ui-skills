# Benchmark 报告：带 skill vs 基线（2026-10-07）

## 方法
- 范围：6 个 skill（app-ui / web-ui / brief / term / components / layout），各 8 条 eval，共 48 条。
- 每条 eval 跑两轮：**基线轮**（不读 SKILL.md，模拟普通 AI）→ **带 skill 轮**（先读 SKILL.md + references/data），逐条 assertion 判定，全满足才算 pass。
- 执行：5 个 skill 由子代理并行完成；salin-ui-term 的子代理只做完基线轮即停，后半程由主代理亲自补完（基线答案 B0–B7 沿用子代理版本）。
- 判定诚实性要求：逐条引用原句作证据；不许压基线分。

## 总分

| skill | 基线 | 带 skill | 增益 |
|---|---|---|---|
| salin-app-ui | 0/8 | 8/8 | +8 |
| salin-web-ui | 1/8 | 8/8 | +7 |
| salin-ui-brief | 0/8 | 8/8 | +8 |
| salin-ui-term | 0/8 | 8/8 | +8 |
| salin-ui-components | 0/8 | 7/8 → 8/8* | +8 |
| salin-ui-layout | 0/8 | 8/8 | +8 |
| **合计** | **1/48 (2.1%)** | **48/48 (100%)** | **+47** |

\* components 原始 7/8：`danger-button-spec` 的断言与 skill 自身规范矛盾（危险按钮误要求 Primary 变体，规范要求 Danger），属 eval 写错而非 skill 问题。已修订 eval（Danger 变体 + 二次确认 + 双端尺寸 + 移动端状态），验证带 skill 通过，修正后计 8/8。commit 09a897d。

唯一基线通过的是 web-ui 的 `form-submit-cost-note`（提交按钮注明消耗），属通用常识。

## 增益来源分析
1. **边界路由类**：基线会直接开干错端任务（如用 44px/拇指热区套桌面官网），skill 正确拒单并路由到对口 skill（app-ui/web-ui 的 boundary 题）。
2. **硬性红线类**：基线凭直觉迎合用户（5 入口平铺、斑马纹、直角、紫蓝渐变），skill 明确引用红线拒绝并给替代方案。
3. **专有机制类**：brief 的 1:1 / 不做清单 / 确认门、term 的出处标注 / motion 编号联动 / "按这 N 条改"格式、layout 的九段式 / Layout Spec 五项——基线完全不会自发产出。
4. **精确数值类**：44px / 12px 表头 / 48px 行高 / 1200~1440 / 8pt 网格，基线凭感觉给不出。

基线并非答得差：在 layout 的 8 题里拿下 15/33 个 assertion 实质分，流程直觉多半正确。skill 的价值不在创意，在把"知道"变成"每次都做到"的检查清单。

## 局限性（诚实声明）
1. 基线非严格盲测：子代理与主代理共享上下文，可能无意带入 skill 知识 → 基线偏强，真实增益可能更大，差距被低估而非高估。
2. 判定者与执行者同一：虽有逐条引证要求，仍存主观性；建议抽查 `/tmp/eval-ab/`、`/tmp/eval_baseline.md` 等原始回答。
3. 48/48 满分说明题库偏向 skill 专有知识——这是设计意图（测增益），不代表真实用户场景全貌；下一轮应加入真实用户提问。
4. 本轮只覆盖 6 个新补 eval 的 skill；motion v4 / dashboard / quality-audit 等未重测。

## 结论
- 带 skill 通过率 **100%（48/48）**，基线 **2.1%（1/48）**，增益 +97.9 个百分点。对比第一轮 96.3%，本轮 skill 质量达标。
- 评测顺带抓出 1 条写错的 eval（danger-button-spec），已修复——说明"评测即质检"成立，建议每个 skill 大改后都跑一遍。
