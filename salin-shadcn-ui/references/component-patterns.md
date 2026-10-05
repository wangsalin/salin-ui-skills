# 组件组合模式

## 表单

- 使用真实 `label`、说明、错误和 `aria-describedby`；placeholder 不是标签。
- schema、表单状态和服务端错误保持一套字段语义；失败时保留输入。
- 验证通常在 blur 或提交时发生，密码强度等即时反馈例外。
- Submit 按钮有 pending，阻止重复提交；错误聚焦或摘要可帮助键盘用户定位。

常见组合：Form/Field + Input/Select/Checkbox/Radio + Button + Toast/Alert。不要为了使用组件而制造多余嵌套。

## Dialog、Sheet 与浮层

- 短、明确、需要阻断当前任务的内容使用 Dialog；保留上下文的辅助编辑可用 Sheet；复杂长流程使用独立页面。
- Trigger 保持语义和可访问名称；打开后焦点进入，Escape 关闭，关闭后返回触发器。
- DropdownMenu、Popover、Tooltip 不放在会裁切的 overflow 容器里；使用项目当前 headless primitive 的 Portal/top-layer 与定位行为，不混用其他底座 API。
- Tooltip 只补充说明，不能承载唯一操作或关键信息。

## 数据表

- 先确定用户要扫描、比较还是批量处理，再选列和密度。
- 工具栏包含搜索、筛选、排序、列显隐与批量操作中真正需要的部分。
- 定义加载、首次空、筛选无结果、错误、无权限、分页和长单元格。
- 移动端优先减少列、改详情抽屉或保留横向滚动提示，不把表格粗暴变成几十张卡。

## 应用壳

- Header、Sidebar、Breadcrumb、Command/Search 和内容区共享路由与权限来源。
- 当前项不能只靠颜色；收起侧栏的图标有 tooltip 和可访问名称。
- 移动端侧栏通常变 Sheet/Drawer，并处理打开时焦点与滚动锁定。
- 完整 Dashboard 的页面结构、侧栏和图表联动交给 `salin-dashboard-builder`。

## 反馈与状态

- Alert 用于页面内持续信息，Toast 用于短暂结果；不能用 Toast 替代字段错误。
- Skeleton 应接近内容形状并预留尺寸，避免布局跳动。
- Empty state 区分“从未有数据”和“筛选后无结果”，给出对应下一步。
- destructive 操作优先可撤销；真正不可逆、高成本或批量操作再确认。

## 通用与业务分层

```text
components/ui/        # shadcn 基础组件与通用 variants
components/patterns/  # 跨功能复用的表单、表格、页面壳组合
features/<domain>/    # 业务语义、数据获取、权限和页面组合
```

沿用项目已有结构，不为符合示例强制搬目录。
