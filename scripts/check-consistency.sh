#!/bin/bash
# 一致性检查：skill 源文件与 README/director/包之间的数字是否同步
# 用法：bash scripts/check-consistency.sh（在仓库根目录运行）
set -u
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

[ $FAIL = 0 ] && echo "ALL PASS" || echo "有不一致项，见上"
exit $FAIL
