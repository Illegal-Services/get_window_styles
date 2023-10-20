#!/usr/bin/env python3

#list_window_styles.py

# --------------------
# 🐍 Standard Python Libraries (Included by Default) 🐍
# These modules are part of the Python standard library and don't require additional installation.
# --------------------
import win32con
import win32gui


def clear_console():
    print(end="\033c")

def has_style(base_style: int, style: int):
    base_style = int(base_style)
    style = int(style)
    return base_style & style == style

def list_window_styles(hwnd: int, styles_type: int, constant_prefix: str, debug=False):

    base_style = win32gui.GetWindowLong(hwnd, styles_type)
    if debug:
        print(f"original style: {base_style} ({hex(base_style)})")
        print()

    styles_found: list[tuple[str, int]] = []
    for n in dir(win32con):      # n = constant name
        v = getattr(win32con, n) # v = constant value
        if not isinstance(v, int):
            continue
        if not n.startswith(constant_prefix):
            continue
        if constant_prefix == "WS_":
            if n.startswith("WS_EX_"):
                continue

        if has_style(base_style, v):
            styles_found.append((n, v))

    resolved_style = 0
    for (name, value) in styles_found:
        if debug:
            print(f"{name}: {value} ({hex(value)})")
        resolved_style |= value

    if debug:
        print()
        print(f'resolved style: {resolved_style} ({hex(resolved_style)})')

    return (resolved_style, styles_found)


hwnd = 0x0000000000081004 # Replace this with the actual window handle you want to inspect

clear_console()

print("Window Styles:")
list_window_styles(hwnd, styles_type=win32con.GWL_STYLE, constant_prefix="WS_", debug=True)

print("-" * 50)

print("Extended Window Styles:")
list_window_styles(hwnd, styles_type=win32con.GWL_EXSTYLE, constant_prefix="WS_EX_", debug=True)

exit(0)