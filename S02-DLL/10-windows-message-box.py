# -*- encoding: utf-8 -*-
# https://docs.microsoft.com/en-us/windows/desktop/LearnWin32/working-with-strings
# https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-messageboxw
import ctypes
import ctypes.wintypes

MB_ICONWARNING = 0x30
MB_CANCELTRYCONTINUE = 0x06
MB_DEFBUTTON2 = 0x100


def basic_invocation():
    user32 = ctypes.windll.user32
    # print(user32)
    # print(user32.MessageBoxW)
    ret = user32.MessageBoxW(
        None,
        ctypes.wintypes.LPCWSTR("用户信息未找到\n是否重试?"),
        ctypes.wintypes.LPCWSTR("Account Details"),
        # "Account Details",
        ctypes.wintypes.UINT(MB_ICONWARNING | MB_CANCELTRYCONTINUE | MB_DEFBUTTON2)
    )
    print(ret)


basic_invocation()
