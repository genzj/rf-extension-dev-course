# encoding: utf-8
ROBOT_LIBRARY_VERSION = '1.0'


class MyClassAdd(object):
    def __init__(self, n=1):
        self._n = n
    
    def to_num(self, n):
        return float(n) if '.' in str(n) else int(n)

    def add(self, n1, n2=None):
        if n2 is None:
            n2 = self._n

        return self.to_num(n1) + self.to_num(n2)

