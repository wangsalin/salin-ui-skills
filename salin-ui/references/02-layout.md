# 03 · 布局（layout）

回答"这个页面骨架怎么搭"：24 种布局模式的分区、栅格、红线（`data/layouts.csv`），统一空间系统（`data/spacing.md`）。

布局清单（24 种）：feed 信息流 / tab-home 底部Tab首页 / masonry 卡片瀑布流 / form-wizard 表单向导 / profile 我的页 / detail 详情页 / marketing-site 营销官网 / workspace 三栏工作台 / dashboard 仪表盘 / docs 文档站 / campaign 落地页长页 / shop-list 电商列表 / auth 登录认证 / empty 空状态 / bento-grid Bento网格 / h-scroll 横滑画廊 / search-results 搜索结果页 / chat 聊天会话页 / settings 设置页 / creator-profile 创作者主页 / onboarding 引导页 / notification-center 通知中心 / split-screen 分屏页 / leaderboard 排行榜

## 定骨架流程
1. 先定端（App/Web）与页面类型。
2. 查 `data/layouts.csv` 找模式，读分区与栅格；无命中用"X+Y 混合"描述，不硬套。
3. 先骨架后组件：本阶段只讨论分区与层级，**不讨论颜色字号**（线框确认前谈视觉即错）。
4. 间距/断点/容器一律查 `data/spacing.md`，不许凭感觉定数值。
5. 对照该模式的红线自查一遍，命中的当场改。
6. **减法**：每个分区必须对应 spec 里一个用户问题，对应不上的删。好页面比差页面少 30% 元素。

## 响应式降级
- Web→平板（≤1024）：多列→2列；三栏工作台右栏变抽屉；Bento 大卡片降级为全宽横卡。
- 平板→手机（≤768）：全部单列；侧边栏→底部Tab 或抽屉；分屏页上下堆叠；数据表→卡片列表。
- 触控：App 目标 ≥44px，Web ≥32px；悬停态只做增强，不承载唯一操作。

## 输出契约（Layout Spec，每页必备）
- 模式：命中的布局模式（或 X+Y 混合）
- 分区：自上而下/由外而内，带占比或顺序
- 栅格：列数/边距/间距/圆角（数值引用 spacing.md）
- 断点：768 / 1024 下的降级方式
- 状态：空/加载/错误/超长内容如何处理

## 看图拆布局（九段式，分析现有页面时用）
模式命名 → 分区拆解 → 栅格间距 → 信息层级 → 导航模式 → 视线动线（F型/Z型/layer-cake） → 密度分级（疏/中/密） → 触控审计 → 评价（可借鉴点+问题点对照红线）
