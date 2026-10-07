#!/usr/bin/env python3
"""动效检索：第 7 步。关键词 → 匹配的 motion 模式（含编号/场景/参数/提示词模板）。
用法：python scripts/motion-search.py "按钮 按压 反馈" [--top 5]
先按场景分组过滤再按关键词排序，解决"60 条逐条扫"的问题。只用标准库。
"""
import argparse, csv, os

DATA = os.path.join(os.path.dirname(__file__), '..', 'data', 'motions.csv')

def main():
    ap = argparse.ArgumentParser(description='检索 60 种动效模式')
    ap.add_argument('query', help='关键词，如"按钮 按压"、"进度条"、"下拉刷新"')
    ap.add_argument('--top', type=int, default=5)
    a = ap.parse_args()
    import math
    rows = list(csv.DictReader(open(DATA, encoding='utf8')))
    terms = [t for t in a.query.replace('，', ' ').split() if t]
    hays = [' '.join([r['name'], r['name_cn'], r['scene'], r['spec'], r['usage']]) for r in rows]
    idf = {t: math.log(len(rows) / max(sum(1 for h in hays if t in h), 1)) for t in terms}
    scored = []
    for r, hay in zip(rows, hays):
        s = sum((3 if t in r['name_cn'] else (2 if t in r['scene'] else 1)) * idf[t]
                for t in terms if t in hay)
        if s:
            scored.append((s, r))
    scored.sort(key=lambda x: -x[0])
    if not scored:
        print('无命中，换关键词再试（如：按钮/进度/弹窗/列表/输入框/导航）。')
        return
    for s, r in scored[:a.top]:
        print(f"#{r['id']} {r['name']} · {r['name_cn']}（{r['scene']}）")
        print(f"   规格：{r['spec'][:90]}")
        if r['prompt_template']:
            print(f"   提示词：{r['prompt_template'][:90]}")
    print('\n铁律：一屏最多 2 种模式，核心流程只用 1 种；时长/缓动写具体数值。')

if __name__ == '__main__':
    main()
