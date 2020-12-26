import ctypes


kernel32 = ctypes.windll.kernel32
GetComputerNameA = kernel32.GetComputerNameA
print(f'{kernel32=}, {GetComputerNameA=}')


libc = ctypes.cdll.msvcrt
sscanf = libc.sscanf
print(f'{libc=}, {sscanf=}')


user32 = ctypes.windll.LoadLibrary(r'C:\Windows\system32\user32.dll')
print(f'{user32=}, {user32.MessageBoxW=}')
