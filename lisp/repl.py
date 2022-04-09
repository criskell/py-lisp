from lisp.eval import evaluate
from lisp.parser import parse
from lisp.environment import globalEnv


def repl():
    while True:
        source = input('py-lisp> ')
        result = evaluate(parse(source), globalEnv)

        print(result)

if __name__ == '__main__':
    repl()