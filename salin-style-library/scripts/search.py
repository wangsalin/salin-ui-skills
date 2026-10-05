#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
salin-style-library 风格检索 + 设计系统生成（标准库 only，无第三方依赖）

用法：
  python search.py "<查询>" [--top 3]
  python search.py "<查询>" --dials 6,4,7 --persist -p "项目名" [--output-dir <项目根目录>]

三旋钮（1-10）：variance（1=保守克制, 10=大胆出挑）, motion（1=静谧, 10=动感）, density（1=疏朗, 10=紧凑）
--persist：把选定风格 + 旋钮落盘为 design-system/<slug>/MASTER.md（项目级设计记忆）
"""
import argparse, csv, os, re, sys
from datetime import date

BASE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE, "..", "data", "styles.csv")

DIAL_GUIDE = {
    "variance": {1: "严格遵循风格基线，不做发挥", 5: "基线之上加一个记忆点", 10: "大胆重构视觉语言，保留风格基因"},
    "motion": {1: "几乎静态，只保留必要状态反馈", 5: "组件级微交互（走 salin-ui-motion）", 10: "页面级转场 + 复杂动效（走 motion-gsap）"},
    "density": {1: "极致留白，一屏一事", 5: "常规信息密度", 10: "高密度工作台，8pt 网格收紧"},
}

def load_styles():
    with open(CSV_PATH, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def tokenize(q):
    raw = [t for t in re.findall(r"[\u4e00-\u9fff]+|[a-zA-Z]+", q.lower()) if t]
    tokens = list(raw)
    # 中文长词加 bigram 回退："美容会所" → "美容","容会","会所"，提高召回
    for t in raw:
        if re.fullmatch(r"[\u4e00-\u9fff]{3,}", t or ""):
            tokens += [t[i:i+2] for i in range(len(t) - 1)]
    return tokens

def score(style, tokens):
    hay = " ".join([style["NameCN"], style["NameEN"], style["Keywords"],
                    style["BestFor"], style["DoNotUseFor"]]).lower()
    s = sum(2 for t in tokens if t in hay)
    # 英文名/关键词命中加权
    s += sum(1 for t in tokens if t in style["NameEN"].lower())
    return s

def search(query, top=3):
    styles = load_styles()
    tokens = tokenize(query)
    ranked = sorted(styles, key=lambda st: score(st, tokens), reverse=True)
    # 零命中时回退默认风格
    if ranked and score(ranked[0], tokens) == 0:
        ranked = sorted(styles, key=lambda st: st["No"] == "1", reverse=True)
    return ranked[:top]

def render_system(style, dials):
    v, m, d = dials
    def pick(dial_name, val):
        guide = DIAL_GUIDE[dial_name]
        key = min(guide, key=lambda k: abs(k - val))
        return guide[key]
    return f"""# 设计系统 MASTER（{style['NameCN']} / {style['NameEN']}）
> 生成日期：{date.today().isoformat()} · 风格库 salin-style-library · 旋钮 variance={v} motion={m} density={d}

## 风格基线
- 主色：{style['PrimaryColors']}
- 辅色：{style['SecondaryColors']}
- 字体：{style['Typography']}
- 圆角阴影：{style['RadiusShadow']}
- 动效倾向：{style['MotionTendency']}

## 旋钮决策
- variance={v}：{pick('variance', v)}
- motion={m}：{pick('motion', m)}
- density={d}：{pick('density', d)}

## AI 提示词（可直接用）
{style['AIPrompt']}

## 边界
- 适用：{style['BestFor']}
- 不适用：{style['DoNotUseFor']}
"""

def slugify(name):
    s = re.sub(r"[^\w\u4e00-\u9fff]+", "-", name).strip("-")
    return s or "project"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--top", type=int, default=3)
    ap.add_argument("--dials", default="5,5,5", help="variance,motion,density（1-10）")
    ap.add_argument("--persist", action="store_true")
    ap.add_argument("-p", "--project", default="")
    ap.add_argument("--output-dir", default=".")
    args = ap.parse_args()

    dials = tuple(max(1, min(10, int(x))) for x in args.dials.split(",")[:3])
    results = search(args.query, args.top)

    print(f"查询：{args.query}｜旋钮 variance={dials[0]} motion={dials[1]} density={dials[2]}\n")
    for i, st in enumerate(results, 1):
        print(f"[{i}] {st['NameCN']} ({st['NameEN']})")
        print(f"    主色：{st['PrimaryColors']}")
        print(f"    适用：{st['BestFor']}\n")

    if args.persist:
        style = results[0]
        slug = slugify(args.project or args.query[:12])
        outdir = os.path.join(args.output_dir, "design-system", slug)
        os.makedirs(outdir, exist_ok=True)
        path = os.path.join(outdir, "MASTER.md")
        if os.path.exists(path):
            print(f"MASTER.md 已存在，未覆盖（先删除再重跑可强制更新）：{path}")
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write(render_system(style, dials))
            print(f"已落盘：{path}")

if __name__ == "__main__":
    main()
