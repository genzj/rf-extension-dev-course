import ctypes

libc = ctypes.cdll.msvcrt
sscanf = libc.sscanf


a, b, c, d = ctypes.c_int(), ctypes.c_int(), ctypes.c_int(), ctypes.c_int()
ret = sscanf(b'1.2.3.4', b'%d.%d.%d.%d', ctypes.byref(a), ctypes.byref(b), ctypes.byref(c), ctypes.byref(d))
print(f'{ret=}, {(a,b,c,d)=}')

