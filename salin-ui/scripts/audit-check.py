#!/usr/bin/env python3
"""验收机械检查：第 8 步的"机器能查的部分"。人负责走查，本脚本负责硬门槛。
用法：python scripts/audit-check.py page.html
检查项（全部基于正文文本 heuristics，误报可能，人工复核）：
 1. focus-visible 是否存在（键盘焦点可见）
 2. prefers-reduced-motion 是否存在
 3. tabular-nums 是否使用（数字等宽）
 4. 可疑小触控目标：height/ min-height < 44px 的 button/.btn/.cta 类（移动端）
 5. outline:none 裸奔（无 focus-visible 配套）
 6. 玻璃拟态 backdrop-blur 使用提醒
只用标准库。退出码 0=全过，1=有未过项。
"""
import re, sys

def main():
    if len(sys.argv) < 2:
        print('用法：python scripts/audit-check.py page.html')
        sys.exit(2)
    h = open(sys.argv[1], encoding='utf8').read()
    fails = []
    def check(name, ok, hint=''):
        print(('  ✓ ' if ok else '  ✗ ') + name + ('' if ok else f' —— {hint}'))
        if not ok:
            fails.append(name)

    check('键盘焦点可见（:focus-visible）', ':focus-visible' in h, '加 button:focus-visible{outline:2px solid ...}')
    check('减少动态降级（prefers-reduced-motion）', 'prefers-reduced-motion' in h, '加 @media (prefers-reduced-motion:reduce){*{transition:none!important}}')
    check('数字等宽（tabular-nums）', 'tabular-nums' in h, '价格/积分/百分比用 font-variant-numeric:tabular-nums')
    # 小触控目标启发式
    small = []
    for m in re.finditer(r'\.(btn|cta|tab|cell|back)(?::[a-z-]+)?\{([^}]*)\}', h):
        mm = re.search(r'(?:min-)?height\s*:\s*(\d+)px', m.group(2))
        if mm and int(mm.group(1)) < 44 and 'tabbar' not in m.group(0):
            small.append(f".{m.group(1)}:{mm.group(1)}px")
    check('触控目标 ≥44px（启发式）', not small, f'偏小：{", ".join(small)}（人工确认）')
    naked = 'outline:none' in h.replace(' ', '') or 'outline: none' in h
    check('无 outline 裸奔', not (naked and ':focus-visible' not in h), 'outline:none 必须配 :focus-visible')
    check('无玻璃拟态', 'backdrop-blur' not in h and 'backdrop-filter' not in h, 'backdrop-blur 默认禁用（人工确认例外）')

    print(f'\n{len(fails)} 项未过' if fails else '\n机械检查全过（仍需人工走查关键路径）')
    sys.exit(1 if fails else 0)

if __name__ == '__main__':
    main()
