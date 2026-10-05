# CLAUDE.md — salin-ui-skills

本仓库是 UI 设计类 skills 的独立家园。**所有 UI 设计类 skills 只在这里维护，不在 `salin-skills` 主仓重复。**

## 硬性约定

1. **一个 skill 一个文件夹**：每制作一个 skill，必须在本目录下创建对应的独立子文件夹，skill 的全部文件都放在自己的文件夹内。
2. **命名必须包含 Salin**：所有 skill 的名字（文件夹名和 SKILL.md 中的 name）必须包含 `salin`，使用 kebab-case，例如 `salin-app-ui`。
3. **App 与 Web 分开**：移动端 App/小程序界面与桌面端网页界面必须是两个独立 skill，不许合并（2026-10-05 用户拍板）。
4. **总控 + 专项**：新增 UI 能力先判断是走 `salin-ui-director` 路由，还是新增专项 skill；专项之间不许职责重叠，边界写进 description。
5. **退役不断链**：退役 skill 保留目录并在 SKILL.md 头部 + description 标注 DEPRECATED 与替代者，不直接删除。
6. **出品三件套**：新 skill 必须带 `SKILL.md` + `evals/evals.json`（断言式用例）+ 打包好的 `.skill` 文件（一键安装包，zip 格式，根目录为 skill 文件夹）。

## 目录结构示例

```text
salin-ui-skills/
├── CLAUDE.md
├── README.md
├── llms.txt
├── salin-xxx/              # 一个 skill 一个文件夹
│   ├── SKILL.md
│   ├── evals/evals.json
│   └── references/
└── salin-xxx.skill         # 一键安装包
```
