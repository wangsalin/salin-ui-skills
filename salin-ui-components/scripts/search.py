#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
salin-ui-components 组件检索（标准库 only，无第三方依赖）

用法：
  python search.py "<查询>" [--top 3] [--full]
  --full：输出完整规格（变体/尺寸/状态/App/Web/无障碍/红线），默认只输出摘要
"""
import argparse, csv, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE, "..", "data", "components.csv")

def load():
    with open(CSV_PATH, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def tokenize(q):
    raw = [t for t in re.findall(r"[\u4e00-\u9fff]+|[a-zA-Z]+", q.lower()) if t]
    tokens = list(raw)
    for t in raw:
        if re.fullmatch(r"[\u4e00-\u9fff]{3,}", t or ""):
            tokens += [t[i:i+2] for i in range(len(t) - 1)]
    return tokens

def score(c, tokens):
    hay = " ".join([c["NameCN"], c["NameEN"], c["Keywords"], c["Variants"]]).lower()
    s = sum(2 for t in tokens if t in hay)
    s += sum(1 for t in tokens if t in c["NameEN"].lower())
    return s

def search(query, top=3):
    comps = load()
    tokens = tokenize(query)
    ranked = sorted(comps, key=lambda c: score(c, tokens), reverse=True)
    return ranked[:top]

def brief(c):
    return (f"[{c['No']}] {c['NameCN']} ({c['NameEN']})\n"
            f"    变体：{c['Variants'][:90]}...\n"
            f"    尺寸：{c['Sizes'][:70]}")

def full(c):
    return (f"[{c['No']}] {c['NameCN']} ({c['NameEN']})\n"
            f"  变体：{c['Variants']}\n"
            f"  尺寸：{c['Sizes']}\n"
            f"  状态：{c['States']}\n"
            f"  App：{c['AppNote']}\n"
            f"  Web：{c['WebNote']}\n"
            f"  无障碍：{c['A11y']}\n"
            f"  红线：{c['DoNot']}\n"
            f"  AI提示词：{c['AIPrompt']}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--top", type=int, default=3)
    ap.add_argument("--full", action="store_true")
    args = ap.parse_args()
    fmt = full if args.full else brief
    print(f"查询：{args.query}\n")
    for c in search(args.query, args.top):
        print(fmt(c) + "\n")

if __name__ == "__main__":
    main()
