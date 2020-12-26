import binascii
import ctypes


libc = ctypes.cdll.msvcrt
print(f'{libc.strlen(b"123")=}')
print(f'{libc.wcslen("中文")=}')

# Caution: bytes and str are mapped to different types!
print(f'{libc.strlen(b"123")=}')
print(f'{libc.strlen("123")=}')
x = ctypes.c_wchar_p("123")
p = ctypes.cast(x, ctypes.POINTER(ctypes.c_char * 8))
print(binascii.hexlify(p.contents.raw, ' ', 2))


kernel32 = ctypes.windll.kernel32
GetComputerNameA = kernel32.GetComputerNameA

hostname = ctypes.create_string_buffer(20)
size = ctypes.c_long(len(hostname))
ret = GetComputerNameA(hostname, ctypes.byref(size))
print(f'{ret=}, {hostname.value=}')



