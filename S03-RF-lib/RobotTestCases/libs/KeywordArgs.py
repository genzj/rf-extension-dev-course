# encoding: utf-8
from robot.api.deco import library, keyword


def to_num(n):
    return float(n) if '.' in str(n) else int(n)


@library(scope='GLOBAL', version='1.1')
class KeywordArgs(object):
    def __init__(self, n=1):
        self._n = n

    @keyword('Add as number', types={'n1': int, 'n2': int})
    def add(self, n1, n2=None):
        if n2 is None:
            n2 = self._n

        return n1 + n2

    @keyword('减法', types=[int, int])
    def sub(self, n1, n2=None):
        if n2 is None:
            n2 = self._n

        return n1 - n2
    
    @keyword('Multiply')
    def mul(self, n1:float, n2:float=None):
        if n2 is None:
            n2 = self._n
        return n1 * n2

    @keyword('Add Many')
    def add_many(self, *n):
        return sum(map(to_num, n))

    @keyword('Add or sub')
    def add_or_sub(self, **kwargs):
        ans = 0
        for k, v in kwargs.items():
            if k.lower().startswith('add'):
                ans += to_num(v)
            elif k.lower().startswith('sub'):
                ans -= to_num(v)
        return ans

