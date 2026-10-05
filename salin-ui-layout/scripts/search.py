#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
salin-ui-layout 布局模式检索（标准库 only，无第三方依赖）

用法：
  python search.py "<查询>" [--top 3] [--full]
  --full：输出完整规格（分区/栅格/适用/红线），默认只输出摘要
"""
import argparse, csv, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE, "..", "data", "layouts.csv")

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
    hay = " ".join([c["NameCN"], c["NameEN"], c["Keywords"], c["BestFor"]]).lower()
    s = sum(2 for t in tokens if t in hay)
    s += sum(1 for t in tokens if t in c["NameEN"].lower())
    return s

def search(query, top=3):
    comps = load()
    tokens = tokenize(query)
    return sorted(comps, key=lambda c: score(c, tokens), reverse=True)[:top]

def brief(c):
    return (f"[{c['No']}] {c['NameCN']} ({c['NameEN']}) [{c['Platform']}]\n"
            f"    分区：{c['Structure'][:80]}...")

def full(c):
    return (f"[{c['No']}] {c['NameCN']} ({c['NameEN']}) [{c['Platform']}]\n"
            f"  分区：{c['Structure']}\n"
            f"  栅格：{c['Grid']}\n"
            f"  适用：{c['BestFor']}\n"
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
