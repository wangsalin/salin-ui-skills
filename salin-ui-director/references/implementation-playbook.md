# 前端落地

实现时优先复用项目现有技术栈。不要为了美化引入不必要框架。

## 项目检查

修改前先看：

- `package.json`
- `README.md`
- `AGENTS.md` / `CLAUDE.md`
- 路由目录：`app/`、`pages/`、`src/routes/`
- 组件目录：`components/`、`components/ui/`
- 样式：`globals.css`、Tailwind config、CSS variables
- `components.json` 是否存在
- Git 状态

## shadcn 使用

适合 React/Next/Vite/Tailwind 项目：

- 已有 shadcn：优先复用 `components/ui/*`。
- 没有 shadcn：只有项目适合且用户需要时再初始化。
- 组件添加用 CLI，避免手抄不完整实现。
- `components/ui/*` 保持通用；业务组合组件放到业务目录。
- 使用语义 token：`bg-background`、`text-foreground`、`border-border`、`bg-muted`、`text-muted-foreground`。

## 常见页面组件

| 页面 | 组件组合 |
|---|---|
| Dashboard | sidebar、tabs、card、table、badge、select、chart、skeleton |
| 表单 | form、input、textarea、select、checkbox、radio、switch、sonner |
| 数据表 | table/data-table、pagination、dropdown-menu、badge、empty |
| AI 工具 | textarea/input、tabs、scroll-area、button、progress、skeleton、toast |
| 登录 | input、button、checkbox、separator、alert、sonner |
| 弹窗流程 | dialog、alert-dialog、drawer、popover、tooltip |

## 状态完整性

每个交互面都要考虑：

- loading
- empty
- error
- disabled
- hover/active
- focus
- validation
- permission denied
- mobile overflow

## 不做

- 不在业务组件里散落大量 hex 色值。
- 不把所有东西都包成卡片。
- 不创建只转发 props 的无意义 wrapper。
- 不用动画掩盖信息结构问题。
- 不显示技术错误给用户，如 raw JSON、stack trace、token、workflow_id。
