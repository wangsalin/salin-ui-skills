# Salin UI Skills

> UI 设计的 Claude Skills 独立仓库 · 总控 + 专项架构 · 每个 skill 独立文件夹，开箱即用

![Claude Skill](https://img.shields.io/badge/Claude-Skill-d97706) ![Language](https://img.shields.io/badge/%E4%B8%AD%E6%96%87-zh--CN-blue) [![LLMs.txt](https://img.shields.io/badge/LLMs.txt-supported-brightgreen.svg)](llms.txt)

从 `wangsalin/salin-skills` 独立出来的 UI 设计 skill 家族。`salin-skills` 保留非 UI skills（如短视频营销），**所有 UI 设计类 skills 只在这个仓库维护**。

---

## 家族全景

```
salin-ui-director（总控：判型 → 分工 → 统一验收）
├── salin-ui-brief          需求定义：一句话需求 → spec.md，区块与用户问题 1:1
├── salin-app-ui            移动端 App / 小程序界面设计与实现
├── salin-web-ui            桌面端网页界面设计与实现
├── salin-style-library     风格库 / 试衣间：风格检索 + 三旋钮 + MASTER.md
├── salin-ui-components     组件设计规范：12 高频组件变体/尺寸/状态/双端差异/红线
├── salin-ui-layout         页面/App 布局：14 种布局模式 + 六段式拆布局分析
├── salin-ui-motion         组件级微交互动效（55 种模式）
├── salin-ui-term           效果术语翻译：大白话 → 设计术语 → 可执行指令
├── salin-dashboard-builder Dashboard / 数据看板专项
├── salin-shadcn-ui         shadcn 组件工程
└── salin-ui-quality-audit  审查验收、反模板化、WCAG 硬门
```

| skill | 一句话 | 安装包 |
|---|---|---|
| salin-ui-director | UI 总控：确定目标、分工边界、执行顺序与统一验收 | [salin-ui-director.skill](salin-ui-director.skill) |
| salin-ui-brief | 需求定义：一句话需求 → _workbench/spec.md，区块与用户问题 1:1 | [salin-ui-brief.skill](salin-ui-brief.skill) |
| salin-app-ui | 移动端 App/小程序：首页/列表/表单向导/结果成就/我的设置 | [salin-app-ui.skill](salin-app-ui.skill) |
| salin-web-ui | 桌面端网页：官网/营销页、SaaS 工作台与后台 | [salin-web-ui.skill](salin-web-ui.skill) |
| salin-style-library | 风格库/试衣间：6 套精调风格检索 + 三旋钮 + MASTER.md 设计记忆 | [salin-style-library.skill](salin-style-library.skill) |
| salin-ui-components | 组件设计规范：按钮/输入框/卡片/弹窗/Tabs/导航/表格/徽标/Toast/下拉/开关/进度条，变体+尺寸+状态+红线 | [salin-ui-components.skill](salin-ui-components.skill) |
| salin-ui-layout | 页面/App 布局：信息流/Tab首页/瀑布流/营销官网/三栏工作台/仪表盘等 14 种 + 拆布局分析 | [salin-ui-layout.skill](salin-ui-layout.skill) |
| salin-ui-motion | 55 种组件微交互（十一大场景分组） | [salin-ui-motion.skill](salin-ui-motion.skill) |
| salin-ui-term | 大白话 → 设计术语（中英对照）→ 可执行指令，45 条术语词典 | [salin-ui-term.skill](salin-ui-term.skill) |
| salin-dashboard-builder | Dashboard 页面架构、指标、交互图表、筛选联动 | [salin-dashboard-builder.skill](salin-dashboard-builder.skill) |
| salin-shadcn-ui | shadcn 初始化、组件源码、主题 tokens、变体 | [salin-shadcn-ui.skill](salin-shadcn-ui.skill) |
| salin-ui-quality-audit | UI 审查、反模板化、打磨、WCAG 5 条硬门、上线验收 | [salin-ui-quality-audit.skill](salin-ui-quality-audit.skill) |

> `salin-product-ui-builder` 已退役（拆分为 salin-app-ui + salin-web-ui），保留目录仅作过渡，不再维护。

## 用法

**不知道用哪个？** 直接调 `salin-ui-director`：描述你的目标，它会判型、分工、定验收标准，只用一个主 skill 负责到底。

**目标明确？** 直接用对应的专项 skill，单一任务不要经过总控。

## 📦 安装

任选其一：

**方式一 · Claude 桌面版 / 网页版**：下载上表中的 `.skill` 文件，在 Claude 对话中打开该文件，点 **Save skill**。

**方式二 · Claude Code**：

```bash
git clone https://github.com/wangsalin/salin-ui-skills.git
cp -r salin-ui-skills/<skill-name> ~/.claude/skills/
```

新会话自动生效（Windows 目录为 `C:\Users\<你>\.claude\skills\`）。

## 📁 仓库结构

```text
salin-ui-skills/
├── salin-ui-director/        # 总控 skill
│   ├── SKILL.md
│   ├── agents/               # agent 配置
│   ├── evals/                # 评测用例
│   └── references/           # 总控参考（视觉方向/项目类型/qa 清单…）
├── salin-app-ui/             # 专项 skill
│   ├── SKILL.md
│   ├── evals/
│   └── references/           # design-tokens / patterns
├── ...
└── *.skill                   # 每个 skill 的一键安装包（zip）
```

## 设计语言

自建 skills 默认使用「暖纸青墨」视觉语言（#F5F3EE + #2E5B4F，强调色陶土橙 #C96F2B），深色只给结果页（暖黑 + 暖金）。禁用大面积渐变、玻璃拟态、紫蓝科技风、中文 900 字重。更深层的风格/配色/字体依据可查 `ui-ux-pro-max`。

## 退役说明

- `salin-product-ui-builder`：2026-10-05 起 DEPRECATED，已拆分为 `salin-app-ui` + `salin-web-ui`。SKILL.md 头部与 description 已标注，请使用拆分后的 skill。
