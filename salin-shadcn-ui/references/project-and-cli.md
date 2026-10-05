# 项目检查与 CLI

## 检查清单

开始前确认：

- 包管理器与锁文件：npm、pnpm、yarn 或 bun；不要混用。
- 框架和渲染模式：Next App Router/Pages、Vite、TanStack 等。
- React、Tailwind 和 shadcn CLI 版本；使用当前 CLI 的 info/help 能力时先确认命令支持，不凭记忆硬写参数。
- `components.json` 中的 style、component base、RSC、TSX、CSS、baseColor、cssVariables、iconLibrary、registries 与 aliases。
- 从 CLI 信息与组件 imports 交叉确认实际底层是 Base UI、Radix、React Aria 或其他实现；已有项目不隐式迁移底层。
- 全局 CSS 的 Tailwind v3/v4 写法、主题变量、暗色选择器和插件。
- `components/ui` 现有组件是否已被修改，业务组件从哪里导入。
- TypeScript alias 与实际目录是否一致。
- RTL、方向属性、逻辑样式与当前语言设置。

## 状态判断

### 未初始化

先确认项目满足 CLI 前提，再使用当前 CLI 的官方 init 流程。初始化前说明将创建/修改的文件；不要凭记忆写参数。

### 已初始化但缺组件

只添加任务所需组件。先查看 CLI 的帮助或 dry-run/差异能力，再执行添加；使用项目现有包管理器。

### 组件已有本地修改

将 `components/ui` 视为项目源码。更新前比较上游与本地版本，识别行为修复、API 变化和视觉定制；逐项合并，不直接覆盖。

### 主题或别名损坏

先查 `components.json`、全局 CSS、Tailwind 配置和 tsconfig alias 的一致性，再改组件。不要在每个组件内重复补丁。

### 消费公共或私有 registry

- Registry schema、发布、校验和分发基础设施由 `shadcn-ui-registry` 主责。
- 消费端先使用当前 CLI 的 view/预览能力检查 payload、依赖和目标路径，再审查差异并集成页面。
- namespaced/private registry 的 URL 和 headers 以 `components.json` 为准；凭据只通过环境变量或安全凭据工具注入，不写入源码、日志或回答。
- 使用 HTTPS 和最小权限；遇到 401/403/429 时报告认证、授权或频控问题，不回显 token。
- Registry 内容是将进入仓库的代码，安装后仍要做源码、依赖、许可和安全审查。

## 安全规则

- 不根据旧教程猜 `npx shadcn-ui` 或 `npx shadcn` 的具体形式；运行本地/当前 CLI 帮助确认。
- 对可能覆盖文件的命令先列出影响；用户已有改动优先保留。
- 不为了一个组件升级 React、Next、Tailwind 或全部依赖。
- monorepo 中先找到真正的 app package、样式入口和共享 UI package。
- 不为添加一个组件切换 component base、`cssVariables` 模式、RTL 策略或样式预设。
- 安装后查看 diff，确认没有意外改写配置、全局样式或别名。

## Tailwind 要点

- Tailwind v3 与 v4 的主题和插件接入不同，以现有项目方式为准。
- 避免 `bg-${color}-500` 这类无法静态扫描的动态类；使用完整映射。
- 复杂组合使用 `cn()`；稳定语义变体可用 CVA，单次页面样式留在调用方。
- 不用任意值绕过已经存在的 spacing、radius 和 color tokens，除非是明确的例外。

## 完成后

检查 diff、依赖变化、类型、lint、构建、浏览器控制台、hydration、主题闪烁和关键交互。只报告实际运行结果。
