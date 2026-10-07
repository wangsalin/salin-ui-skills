# 07 · shadcn 工程（shadcn）

仅在 React/Next.js/Vite + Tailwind 项目中、且已确定使用 shadcn 时启用。shadcn 是"把组件源码带进项目"，不是黑盒依赖。

## 核心流程
1. 检查项目：README、package、Tailwind 版本、`components.json`、全局 CSS、路径别名、现有 `components/ui`。不猜测。
2. 判断状态：未初始化 / 已初始化 / 组件缺失 / 本地已修改 / 主题漂移。
3. 先预览风险：添加/更新组件前看 CLI 差异；禁止无审查覆盖已定制源码。
4. 获取基础组件：用项目包管理器和 shadcn CLI；保持现有 style、base color、CSS variables、aliases。
5. 按现有主题模式工作：维护语义 tokens（background/foreground/primary/muted/destructive/border）亮暗配对。
6. 组合产品界面：通用原子留 `components/ui`；业务组合放功能目录。
7. 补全状态与响应式：键盘/焦点/触摸/加载/空/错误/禁用/长内容/窄屏/暗色。
8. 验证真实项目：类型/lint/测试/构建/浏览器关键流程。

## 强约束
- 不臆测 CLI 参数、组件路径、Tailwind 版本；以本地项目与 CLI 输出为准。
- 不自动执行覆盖式更新；先确认修改文件并保留本地定制。
- 不把产品特定样式塞进通用 Button/Input；只有多处复用且语义稳定才加 variant。
- 不硬编码颜色替代语义 token；不混用 HSL/RGB/OKLCH。
- 不用 div 伪造按钮/链接/对话框；保留 headless primitive 的语义、焦点、键盘行为。
- 只需要产品设计方向时不要初始化 shadcn。

## 完成前检查
- 沿用项目包管理器、别名、Tailwind 版本、`components.json`。
- 本地修改已保护；tokens 语义化、亮暗成对、对比度足够。
- 业务组合与通用 `components/ui` 分层正确。
- 真实浏览器验证主题、键盘、触摸、控制台。
