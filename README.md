# list_window_styles

## Description

* List from a given handle its styles.

## Advantages

* Officially tested for styles and exstyles.
* Has a built in debugging that allows you to performs an in-depth analysis, in a human-readable format to understand what is happening within the code.

## Example Output
```
Window Styles:
original style: 365363200 (0x15c70000)

WS_BORDER: 8388608 (0x800000)
WS_CAPTION: 12582912 (0xc00000)
WS_CLIPSIBLINGS: 67108864 (0x4000000)
WS_DLGFRAME: 4194304 (0x400000)
WS_GROUP: 131072 (0x20000)
WS_MAXIMIZE: 16777216 (0x1000000)
WS_MAXIMIZEBOX: 65536 (0x10000)
WS_MINIMIZEBOX: 131072 (0x20000)
WS_OVERLAPPED: 0 (0x0)
WS_SIZEBOX: 262144 (0x40000)
WS_TABSTOP: 65536 (0x10000)
WS_THICKFRAME: 262144 (0x40000)
WS_TILED: 0 (0x0)
WS_VISIBLE: 268435456 (0x10000000)

resolved style: 365363200 (0x15c70000)
--------------------------------------------------
Extended Window Styles:
original style: 256 (0x100)

WS_EX_LEFT: 0 (0x0)
WS_EX_LTRREADING: 0 (0x0)
WS_EX_RIGHTSCROLLBAR: 0 (0x0)
WS_EX_WINDOWEDGE: 256 (0x100)

resolved style: 256 (0x100)
```
## Credits

* The method I uses to filter the styles has been inspired from:<br>
> https://github.com/Xpra-org/xpra/blob/9f892b77cfd0a0ad0dbe76387755b474bf9965f6/packaging/MSWindows/gen_win32con.py<br>
* Helpers from https://discord.gg/GSVrHag:<br>
> [@Grub4K](https://github.com/Grub4K) - Code refining and optimization.<br>
> [@mdev](https://github.com/mdev-new) - Helped me fixing an issue where I was using the "+" opeartor instead of the "|",<br>
which was causing an innacurate calculation of the 'resolved_style' variable.<br>
