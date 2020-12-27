# encoding: utf-8


from robot.api.deco import library, keyword

@library(scope='GLOBAL', version='1.1')
class MyDecoClassAdd(object):
    def __init__(self, n=1):
        self._n = n
    

    def _to_num(self, n):
        return float(n) if '.' in str(n) else int(n)

    @keyword('Add as number')
    def add(self, n1, n2=None):
        if n2 is None:
            n2 = self._n

        return self._to_num(n1) + self._to_num(n2)

    @keyword('减法')
    def sub(self, n1, n2=None):
        if n2 is None:
            n2 = self._n

        return self._to_num(n1) - self._to_num(n2)
