from lisp.types import Number, Symbol
from lisp.environment import Env

class Func():
    def __init__(self, params, body, env):
        self.params = params
        self.body = body
        self.env = env

    def __call__(self, *args):
        return evaluate(self.body, Env(self.params, args, self.env))

def evaluate(expr, env):
    if isinstance(expr, Symbol):
        return env.findEnv(expr)[expr]
    elif isinstance(expr, Number) or type(expr) is str:
        return expr
    
    op, *args = expr

    if op == 'if':
        test, conseq, alternative = args
        return evaluate(conseq if evaluate(test, env) else alternative, env)
    elif op == '=':
        symbol, expression = args
        env[symbol] = evaluate(expression, env)
        return
    elif op == 'quote':
        return args[0]
    elif op == 'set!':
        (symbol, expression) = args
        env.findEnv(symbol)[symbol] = evaluate(expression, env)
        return
    elif op == '->':
        (params, body) = args
        return Func(params, body, env)
    else:
        fn = evaluate(op, env)
        evaluatedArgs = [evaluate(arg, env) for arg in expr[1:]]
        return fn(*evaluatedArgs)