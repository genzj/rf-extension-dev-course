from ctypes import CFUNCTYPE, POINTER, c_int, c_int, cdll, sizeof

@CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
def py_cmp_func(a, b):
    print("py_cmp_func", a[0], b[0])
    return a[0] - b[0]


ia = (c_int * 5)(5, 1, 7, 33, 99)
print('before qsort:', list(ia))

cdll.msvcrt.qsort(ia, len(ia), sizeof(c_int), py_cmp_func)
print('after qsort:', list(ia))
