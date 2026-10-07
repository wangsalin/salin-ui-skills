# 术语词典：大白话 → 设计术语

查法：按用户大白话里的关键词（如下滑、卡片、翻、吸住、抖）定位行。`motion` 列是 salin-ui-motion 里的模式编号（`—` 表示通用术语、无对应模式）。English term 标注 `视频原话` 的三条来自 @西瓜同学🍉 第18集原话，其余为推荐译法。

## 滚动与固定

| 大白话说法 | 中文术语 | English term | motion | 出处 |
|---|---|---|---|---|
| 往下滑的时候，卡片一张张往前翻 | 卡片连续向前翻转 | Card Flip | — | 视频原话 |
| 滚到某一屏，内容定住不动，背景继续走 | 滚动与固定内容区域 | Pinned Section | — | 视频原话 |
| 左边的字跟着右边的卡片一起换 | 左侧文案同步切换 | Synced Copy | — | 视频原话 |
| 往上滚顶栏藏起来，往下滑顶栏出来 | 顶栏随滚动收起 | Collapsing Header | — | 推荐译法 |
| 滚到顶了还能再拽一下，有橡皮筋 | 橡皮筋超拉 | Overscroll / Rubber Banding | 37 | 推荐译法 |
| 滚得越快越糊，停下来变清楚 | 速度动态模糊 | Motion Blur (scroll velocity) | 40 | 推荐译法 |
| 滚动多少动画走多少，能停在半路 | 滚动驱动动画 | Scroll-driven Animation (Scrub) | 39 | 推荐译法 |
| 滚到中间那一项自动放大 | 滚动聚焦 | Scroll Focus | 43 | 推荐译法 |
| 下拉的时候顶图跟着变大 | 下拉拉大顶图 | Pull to Zoom Header | 41 | 推荐译法 |

## 手势进行中

| 大白话说法 | 中文术语 | English term | motion | 出处 |
|---|---|---|---|---|
| 甩出去还能按住停下来 | 惯性刹停 | Fling Catch | 35 | 推荐译法 |
| 手指没松开就知道会停在哪 | 落点预测 | Landing Prediction | 36 | 推荐译法 |
| 滑到一半，甩得快就走完，慢就回来 | 手势速度决策 | Velocity-based Dismiss | 31 | 推荐译法 |
| 按住后手指滑出去就不算点了 | 按压逃逸取消 | Press Escape | 32 | 推荐译法 |
| 斜着滑只认横/竖一个方向 | 手势方向锁定 | Gesture Direction Lock | 34 | 推荐译法 |
| 整个页面跟着手指走，能取消能走完 | 手势驱动转场 | Interactive Transition | 55 | 推荐译法 |
| 拖拽时靠近线自动吸住 | 吸附对齐 | Snap to Guide | 44 | 推荐译法 |
| 长按拖起排序，邻居让位 | 拖拽排序 | Drag to Reorder | 52 | 推荐译法 |
| 双指捏合切换排版密度 | 语义缩放 | Semantic Zoom | 38 | 推荐译法 |

## 选择与反馈

| 大白话说法 | 中文术语 | English term | motion | 出处 |
|---|---|---|---|---|
| 点一下复制，图标翻成对勾 | 复制反馈 | Copy Feedback | 6 | 推荐译法 |
| 开关拨动泛起一圈水波 | 开关联动涟漪 | Toggle Ripple | 51 | 推荐译法 |
| 批量勾选一个一个打勾，有节奏 | 接力打勾 | Staggered Check | 53 | 推荐译法 |
| 选中的标签把旁边的挤开 | 标签挤开 | Chip Squeeze | 54 | 推荐译法 |
| 点选后其他的变灰退后 | 聚焦模式 | Focus Mode (Dim Others) | 30 | 推荐译法 |
| 数字变了只有变的那几位跳 | 数字差分更新 | Text Diff Update | 33 | 推荐译法 |
| 滑杆拖到刻度附近自动吸过去 | 滑杆吸附 | Slider Snap | 45 | 推荐译法 |
| 旋钮转到刻度有段落感 | 磁吸刻度 | Magnetic Detents | 28 | 推荐译法 |
| 按下去卡片跟着手指倾斜 | 按压倾斜 | Press Tilt | 13 | 推荐译法 |
| 卡片飞进收纳区 | 卡片吸入回收 | Card Collect | 29 | 推荐译法 |
| 头像叠在一起，点开散开 | 重叠展开 | Overlap Stack Expand | 15 | 推荐译法 |
| 步骤条走过去有弹性 | 步骤弹性 | Spring Stepper | 50 | 推荐译法 |

## 通用组件术语

| 大白话说法 | 中文术语 | English term | motion | 出处 |
|---|---|---|---|---|
| 先出灰框占位，内容来了再填 | 骨架屏 | Skeleton Screen | — | 推荐译法 |
| 下拉刷新 | 下拉刷新 | Pull to Refresh | — | 推荐译法 |
| 左滑出现删除按钮 | 滑动操作 | Swipe Actions | — | 推荐译法 |
| 底部弹出的半屏面板 | 底部弹窗 | Bottom Sheet | 2 | 推荐译法 |
| 点一下底部导航图标展开成文字 | 底部导航选中展开 | Expanding Tab Bar | 4 | 推荐译法 |
| 悬浮按钮随滚动收起 | 滚动收起悬浮钮 | Scroll-aware FAB | 5 | 推荐译法 |
| 表单填错了抖一下 | 表单校验反馈 | Form Error Shake | 7 | 推荐译法 |
| 输入框下面弹出联想 | 输入联想浮层 | Suggest Popover | 11 | 推荐译法 |
| 拨动刻度调字号 | 刻度盘调节 | Dial Control | 12 | 推荐译法 |
| 长按变成录音条 | 长按转录音 | Hold to Record | 14 | 推荐译法 |
| 图标跟着手指放大 | 跟手放大 | Magnify on Touch | 19 | 推荐译法 |
| 下拉展开摘要，拉过阈值进详情 | 下拉摘要 | Pull Summary | 20 | 推荐译法 |
| 点卡片展开全屏详情 | 卡片展开详情 | Card to Detail | 21 | 推荐译法 |
| 横着滑的筛选胶囊 | 筛选胶囊行 | Chip Row | 23 | 推荐译法 |
| 悬浮元素跟着背景换黑白 | 自动反色 | Auto Contrast | 46 | 推荐译法 |
| 果冻一样 duang 一下 | 液态形变 | Liquid Deform (Gooey) | 47 | 推荐译法 |
| 卡片随视角分层错动 | 3D 视差 | 3D Parallax | 48 | 推荐译法 |
| 换列数时沿弧线飞 | 弧线重排 | Arc Reflow | 42 | 推荐译法 |

## 查不到时怎么办
1. 用最接近的一条 + 一句话行为补述，标注"推荐译法"。
2. 行为补述模板："元素在 {触发} 时 {时长}ms {缓动} {做什么}，结束状态 {是什么}"。
3. 不许生造英文词；不确定就只给中文术语 + 行为描述。
