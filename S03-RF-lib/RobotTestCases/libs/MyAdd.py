# encoding: utf-8
ROBOT_LIBRARY_VERSION = '1.0'


def to_num(n):
    return float(n) if '.' in str(n) else int(n)

def add(n1, n2=1):
    return to_num(n1) + to_num(n2)
