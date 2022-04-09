import math
import operator as op

from lisp.types import Env

class Env(dict):
    def __init__(self, params=(), args=(), outerEnv=None):
        self.update(zip(params, args))
        self.outerEnv = outerEnv

    def findEnv(self, name):
        return self if (name in self) else self.outerEnv.findEnv(name)


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
        '=': op.eq,
        'print': print,
        'sqrt': math.sqrt,
        'begin': lambda *x: x[-1],
    })

    return env

globalEnv = createStandardEnv()
globalEnv.update(globalEnv=globalEnv)