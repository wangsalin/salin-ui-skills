#!/usr/bin/env python3
"""spec 脚手架：第 1 步需求定义的格式保证器。
用法：python scripts/spec.py "一句话需求" --users "目标用户" -o _workbench/spec.md
输出带必填字段的 spec.md 草稿（区块表/不做清单/页面定义摘要），内容由人填，脚本保证不漏项。
只用标准库。
"""
import argparse, os, sys

TEMPLATE = """# spec.md · {title}

## 页面一句话目标
{goal}

## 北极星（≤5 行，硬约束）
- 业务指标：（1 条，可衡量）
- 核心用户任务：（1 条）
> 铁律：后文每个区块必须能回指北极星，回指不上的删。不许写"提升用户体验"类套话。

## 目标用户
{users}

## 区块表（区块 | 用户问题 | 内容要点 | 优先级）

| 区块 | 用户问题 | 内容要点 | 优先级 |
|---|---|---|---|
| （填区块1） | （用户带着什么问题来） | （放什么内容） | P0 |
| （填区块2） | | | P0 |
| （填区块3） | | | P1 |

> 铁律：一个区块只回答一个用户问题；说不出解决哪个问题的区块直接删。

## 术语统一表（名称 | 大白话含义 | 出处/约定）

| 名称 | 大白话含义 | 出处/约定 |
|---|---|---|
| （填名称1） | （用户理解的说法） | （沿用现有/新定） |
| （填名称2） | | |

> 铁律：命名一旦确定，后续步骤不许另起名字。

## 不做清单（这次明确不解决什么）
- （填1）
- （填2）

## 页面定义摘要（一句话，给后续步骤当输入）
{goal}，{users}。
"""

def main():
    ap = argparse.ArgumentParser(description='生成 spec.md 草稿')
    ap.add_argument('goal', help='一句话需求，如"社区咖啡店今日特调营销页"')
    ap.add_argument('--users', default='（待填）', help='目标用户')
    ap.add_argument('-o', '--output', default='_workbench/spec.md', help='输出路径')
    a = ap.parse_args()
    out = a.output
    if os.path.exists(out):
        print(f'已存在，不覆盖：{out}', file=sys.stderr)
        sys.exit(1)
    os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
    title = a.goal[:20]
    open(out, 'w', encoding='utf8').write(TEMPLATE.format(title=title, goal=a.goal, users=a.users))
    print(f'spec 草稿已生成：{out}')
    print('下一步：填区块表（每区块对应一个用户问题），然后请用户确认。')

if __name__ == '__main__':
    main()
