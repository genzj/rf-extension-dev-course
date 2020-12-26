import ctypes

c = ctypes.cdll.msvcrt

# const char * strchr ( const char * str, int character );
c.strchr.restype = ctypes.c_char_p

subs = c.strchr(b'abcdefg', ctypes.c_char(b'c'))
print(f'{subs=}')

# Pitfall #1: bytes/str are always mapped to pointer types (char*/wchar*)
subs = c.strchr(b'abcdefg', b'c')
print(f'{subs=}')

# Pitfall #2: Python uses dynamic length ints while DLL uses fixed length ones
big_int = 1024**4
print(f'{big_int=}')
print(f'{ctypes.c_long(big_int)=}')
