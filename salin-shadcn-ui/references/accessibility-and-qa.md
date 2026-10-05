# 响应式、无障碍与验收

## 交互状态

为适用的控件检查：default、hover、focus-visible、active、disabled、loading、error、success。Hover 不是触摸和键盘的替代路径。

## 无障碍

- 使用 Button、Link、Input、Dialog 等语义组件，不用带 click 的 div 伪造。
- 每个图标按钮有可访问名称；装饰图标从辅助技术隐藏。
- 不移除焦点环；焦点顺序与视觉顺序一致。
- Dialog/Sheet/Dropdown 的焦点、Escape、方向键和返回触发器行为可用。
- 文本、边界、focus 和状态对比度足够；错误不只靠红色。
- 动态反馈适当使用 live region；支持 `prefers-reduced-motion`。

## 响应式

- 先保证最窄支持宽度，再增强到 `sm/md/lg/xl`；断点以项目实际配置为准。
- 触摸目标通常至少 44×44px；移动端正文通常不低于约 14px。
- 表格、Tabs、Breadcrumb、Dialog 和 Sidebar 要定义窄屏替代，而非仅缩小。
- 长文本使用 `min-w-0`、wrap、truncate 或 line-clamp；浮层避免越界和裁切。
- 测试 200% 缩放、软键盘、安全区和横竖屏。

## 主题与内容

- 亮色、暗色、系统主题都检查；颜色切换不应产生不可读状态。
- 测试中文、英文长词、emoji、零值、空值、大数字和错误文案。
- Skeleton/图片预留尺寸，减少 CLS；图标和字体加载失败时界面仍可用。

## 工程验收

按项目可用能力运行：

1. 格式化和 lint。
2. TypeScript 类型检查。
3. 单元/组件/集成测试。
4. 生产构建。
5. 浏览器检查关键流程、控制台、hydration、主题、键盘、触摸和移动端。

无法运行的检查必须说明原因。编译通过不等于交互、视觉和无障碍通过。
