import math
import operator as op

from lisp.types import Env

class Env(dict):
    def __init__(self, params=(), args=(), outerEnv=None):
        self.update(zip(params, args))
        self.outerEnv = outerEnv

    def findEnv(self, name):
        if name in self:
            return self
        elif self.outerEnv:
            return self.outerEnv.findEnv(name)
        else:
            raise NameError(f"Nome '{name}' não encontrado.")


def createStandardEnv():
    env = Env()

    env.update({
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
        '/': op.truediv,
        '>': op.gt,
        '<': op.lt,
        '>=': op.ge,
        '<=': op.le,
        '==': op.eq,
        'int': int,
        'float': float,
        'str': str,
        'print': print,
        'sqrt': math.sqrt,
        '>>>': lambda *x: x[-1],
    })

    return env

globalEnv = createStandardEnv()
globalEnv.update(globalEnv=globalEnv)