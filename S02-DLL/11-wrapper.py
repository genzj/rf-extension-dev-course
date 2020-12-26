# -*- encoding: utf-8 -*-
# https://docs.microsoft.com/en-us/windows/desktop/LearnWin32/working-with-strings
# https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-messageboxw
import ctypes
import ctypes.wintypes

strchr = ctypes.cdll.msvcrt.strchr
strchr.restype = ctypes.c_char_p
strchr.argtypes=(ctypes.c_char_p, ctypes.c_char)
print(f"{strchr(b'abcdefg', b'd')=}")

# print(f"{strchr('abcdefg', 'd')=}")  # will raise WrongType - no str/bytes pitfall



MB_ICONWARNING = 0x30
MB_CANCELTRYCONTINUE = 0x06
MB_DEFBUTTON2 = 0x100


prototype = ctypes.WINFUNCTYPE(
    ctypes.c_int,
    ctypes.wintypes.HWND, ctypes.wintypes.LPCWSTR, ctypes.wintypes.LPCWSTR, ctypes.wintypes.UINT
)
paramflags = (
    (1, "hwnd", None),
    (1, "text", "Hi"),
    (1, "caption", "Hello from ctypes"),
    (1, "flags", MB_ICONWARNING | MB_CANCELTRYCONTINUE | MB_DEFBUTTON2)
)
MessageBox = prototype(("MessageBoxW", ctypes.windll.user32), paramflags)


MessageBox(text='中文提示', caption='调用windows函数')


