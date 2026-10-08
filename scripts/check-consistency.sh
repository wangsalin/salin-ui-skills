#!/bin/bash
# 一致性检查：skill 源文件与 README/director/包之间的数字是否同步
# 用法：bash scripts/check-consistency.sh（可在任意目录运行，自动定位到仓库根目录）
set -u
cd "$(dirname "$0")/.."  # 固定到仓库根目录：相对路径检查 + 数字残留扫描都只扫本仓库，防止从别的 cwd 误跑出假失败
FAIL=0
say(){ if [ "$2" = "0" ]; then echo "  ✓ $1"; else echo "  ✗ $1"; FAIL=1; fi; }

echo "== motion 模式数 =="
N=$(grep -c "^### " salin-ui-motion/SKILL.md)
grep -q "组件交互动效：$N 种" salin-ui-motion/SKILL.md; say "motion description $N 种" $?
grep -q "## 交互模式（$N 种）" salin-ui-motion/SKILL.md; say "motion 模式标题 $N 种" $?
grep -q "从下面 $N 种模式里选" salin-ui-motion/SKILL.md; say "motion 内文 $N 种" $?
grep -q "$N 种组件微交互" README.md; say "README 表格 $N 种" $?
grep -q "组件级微交互动效：$N 种模式" salin-ui-director/SKILL.md; say "director 表格 $N 种" $?
grep -q "组件级微交互动效（$N 种模式" salin-ui-director/SKILL.md; say "director 内文 $N 种" $?
grep -q "的 $N 种模式联动" salin-ui-term/SKILL.md; say "term 联动 $N 种" $?

echo "== term 词典条数 =="
T=$(python3 -c "
t=open('salin-ui-term/references/term-dictionary.md',encoding='utf8').read()
print(len([l for l in t.split(chr(10)) if l.startswith('|') and '---' not in l and '大白话' not in l]))")
grep -q "$T 条术语词典" README.md; say "README 词典 $T 条" $?

echo "== .skill 包新鲜度 =="
for d in salin-*/; do
  n=$(basename "$d"); [ "$n" = "salin-product-ui-builder" ] && continue
  if [ ! -f "$n.skill" ]; then say "$n 缺 .skill 包" 1; continue; fi
  if [ "$d/SKILL.md" -nt "$n.skill" ]; then say "$n 包过期（SKILL.md 更新）" 1; else say "$n 包新鲜" 0; fi
done
[ -f salin-product-ui-builder.skill ] && say "退役包应已下架" 1 || say "退役包已下架" 0

echo "== 数字残留扫描 =="
grep -rn "55 种\|55种" --include="*.md" . | grep -v ".git/" | grep -v check-consistency && say "发现 55 种残留" 1 || say "无 55 种残留" 0

echo "== salin-ui 统一包 =="
M=$(($(wc -l < salin-ui/data/motions.csv) - 1))
[ "$M" = "60" ]; say "motions.csv 60 条" $?
T2=$(($(wc -l < salin-ui/data/terms.csv) - 1))
[ "$T2" = "53" ]; say "terms.csv 53 条" $?
E2=$(python3 -c "import json;print(len(json.load(open('salin-ui/evals/evals.json',encoding='utf8'))))")
[ "$E2" = "109" ]; say "evals 109 条" $?
grep -q "60 种" salin-ui/SKILL.md; say "SKILL.md 60 种" $?
[ -f salin-ui.skill ]; say "salin-ui.skill 包存在" $?
[ "salin-ui/SKILL.md" -nt "salin-ui.skill" ] && say "salin-ui 包过期" 1 || say "salin-ui 包新鲜" 0
for f in references/00-spec.md references/02-layout.md references/03-style.md references/04-implement-app.md references/05-implement-web.md references/06-dashboard.md references/07-shadcn.md references/08-audit.md references/09-routing.md; do
  [ -f "salin-ui/$f" ]; say "salin-ui/$f" $?
done

for sc in spec.py style-search.py motion-search.py audit-check.py; do
  [ -f "salin-ui/scripts/$sc" ]; say "salin-ui/scripts/$sc" $?
done
python3 -c "import ast;ast.parse(open('salin-ui/scripts/spec.py').read());ast.parse(open('salin-ui/scripts/style-search.py').read());ast.parse(open('salin-ui/scripts/motion-search.py').read());ast.parse(open('salin-ui/scripts/audit-check.py').read())" 2>/dev/null; say "4 脚本语法通过" $?

[ -f "salin-ui/references/10-tokens.md" ]; say "10-tokens.md" $?
[ -f "salin-ui/references/11-typography.md" ]; say "11-typography.md" $?
grep -q "11-typography" salin-ui/SKILL.md; say "SKILL.md 挂排版" $?
grep -q "10-tokens" salin-ui/SKILL.md; say "SKILL.md 挂 tokens" $?
grep -q "苹果风" salin-ui/references/03-style.md; say "03-style 苹果风" $?

[ -f "salin-ui/references/00-project.md" ]; say "00-project.md" $?
grep -q "7 步" salin-ui/SKILL.md; say "SKILL.md 7 步" $?
grep -q "任务分级" salin-ui/SKILL.md; say "任务分级" $?
grep -q "4 幕" salin-ui/SKILL.md; say "4 幕" $?
grep -q "北极星" salin-ui/SKILL.md; say "北极星" $?
grep -q "决策摘要" salin-ui/SKILL.md; say "决策摘要" $?
grep -q "结束本轮输出" salin-ui/SKILL.md; say "确认=结束本轮" $?
grep -q "动效编排" salin-ui/references/04-implement-app.md; say "动效编排子阶段" $?
[ -f "salin-ui/references/00-spec.md" ]; say "00-spec.md" $?
grep -q "术语统一表" salin-ui/scripts/spec.py; say "spec.py 术语统一表" $?
grep -q "边界防御" salin-ui/references/08-audit.md; say "audit 边界防御" $?
grep -q "单文件 HTML" salin-ui/references/04-implement-app.md; say "技术栈声明" $?
grep -q "RBAC" salin-ui/references/06-dashboard.md; say "dashboard RBAC" $?
[ -f "salin-ui/references/12-delivery.md" ]; say "12-delivery.md" $?
python3 -c "import ast;ast.parse(open('salin-ui/scripts/project.py').read())" 2>/dev/null; say "project.py 语法通过" $?

[ $FAIL = 0 ] && echo "ALL PASS" || echo "有不一致项，见上"
exit $FAIL
