#!/usr/bin/env python3
"""项目分析脚手架：第 0 步。输出 _workbench/project.md 草稿（背景/业务目标/用户/功能/约束）。
用法：python scripts/project.py "项目一句话" --users "目标用户" -o _workbench/project.md
只用标准库。
"""
import argparse, os, sys

TEMPLATE = """# project.md · {title}

## 项目背景
{goal}

## 业务目标（可衡量的 1-3 条）
- （填1：如 提升团购核销率）
-

## 用户分析
### 目标用户群（关键特征 3-5 条）
- {users}
-
### 核心使用场景（2-3 个）
- （何时、何地、为何打开）
-
### 关键用户旅程（主流程 3-5 步）
1.
2.
3.

## 功能分析
### 功能清单（先列全）
-
### 优先级（P0 必有 / P1 重要 / P2 可砍，P0 不超过 7 个）
-
### 信息架构（页面地图）
- （Tab/页面/层级，一句话写清每页职责）

## 约束
- 技术栈：（填）
- 品牌 VI：（填）
- 项目级不做清单：
  -
"""

def main():
    ap = argparse.ArgumentParser(description='生成 project.md 草稿')
    ap.add_argument('goal', help='项目一句话，如"本地餐饮商家的 AI 营销视频工具"')
    ap.add_argument('--users', default='（待填）', help='目标用户')
    ap.add_argument('-o', '--output', default='_workbench/project.md')
    a = ap.parse_args()
    out = a.output
    if os.path.exists(out):
        print(f'已存在，不覆盖：{out}', file=sys.stderr)
        sys.exit(1)
    os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
    open(out, 'w', encoding='utf8').write(TEMPLATE.format(title=a.goal[:20], goal=a.goal, users=a.users))
    print(f'project 草稿已生成：{out}')
    print('下一步：填业务目标/用户旅程/功能清单，然后进第 1 步逐页出 spec。')

if __name__ == '__main__':
    main()
