import win32con
import win32gui


def clear_console():
    print(end="\033c")

def has_style(base_style: int, style: int):
    return int(base_style) & int(style) == int(style)

def get_window_styles(hwnd:int, gwl_style_or_exstyle:int, startstr:str):

    base_style = win32gui.GetWindowLong(hwnd, gwl_style_or_exstyle)
    print(f"original style: {base_style} ({hex(base_style)})")
    print()

    styles: list[tuple[str, int]] = []
    # x = name/key  |  v = value
    for x in dir(win32con):
        v = getattr(win32con, x)
        if callable(v):
            continue
        if not isinstance(v, int):
            continue
        if not x.startswith(startstr):
            continue
        if startstr == "WS_":
            if x.startswith("WS_EX_"):
                continue

        if has_style(base_style, v):
            styles.append((x, v))

    resolved_style = 0
    for (name, value) in styles:
        print(f"{name}: {value} ({hex(value)})")
        resolved_style += value

    print()
    print(f'resolved style: {resolved_style} ({hex(resolved_style)})')

hwnd = 0x000000000010102C # Replace this with the actual window handle you want to inspect

clear_console()

print("Window Styles:")
get_window_styles(hwnd, win32con.GWL_STYLE, "WS_")

print("-" * 50)

print("Extended Window Styles:")
get_window_styles(hwnd, win32con.GWL_EXSTYLE, "WS_EX_")

exit(0)