#!/usr/bin/env python3
"""风格检索：第 2 步。产品描述 → Top 3 风格。
用法：python scripts/style-search.py "奶茶店 点单 年轻人" [--top 3]
只用标准库。零命中时回退默认风格（暖纸青墨）并明示。
"""
import argparse, csv, os, sys

DATA = os.path.join(os.path.dirname(__file__), '..', 'data', 'styles.csv')

def main():
    ap = argparse.ArgumentParser(description='检索风格库 Top N')
    ap.add_argument('query', help='2-5 个词：行业+用户+调性')
    ap.add_argument('--top', type=int, default=3)
    a = ap.parse_args()
    rows = list(csv.DictReader(open(DATA, encoding='utf-8-sig')))
    terms = [t for t in a.query.replace('，', ' ').split() if t]
    scored = []
    for r in rows:
        hay = ' '.join([r.get('NameCN',''), r.get('NameEN',''), r.get('Keywords',''), r.get('BestFor','')])
        s = sum(2 if t in hay else 1 for t in terms for _ in [0] if t in hay or any(t[i:i+2] in hay for i in range(len(t)-1))) if False else sum((2 if t in hay else (1 if any(t[i:i+2] in hay for i in range(max(len(t)-1,1))) else 0)) for t in terms)
        scored.append((s, r))
    scored.sort(key=lambda x: -x[0])
    top = [r for s, r in scored[:a.top] if s > 0]
    if not top:
        print('零命中，回退默认风格：暖纸青墨（请明确告诉用户这是回退）')
        return
    for i, r in enumerate(top, 1):
        print(f"[{i}] {r['NameCN']}（{r['NameEN']}）")
        print(f"    主色：{r['PrimaryColors'][:60]}")
        print(f"    适合：{r['BestFor'][:50]}")
        print(f"    不适用：{r['DoNotUseFor'][:50]}")
    print('\n下一步：给用户看 Top 3，由用户二选一/三选一（不许代选），再定三旋钮。')

if __name__ == '__main__':
    main()
