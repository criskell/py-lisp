import sys

from lisp.eval import evaluate
from lisp.parser import parse
from lisp.environment import globalEnv

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        evaluate(parse(f.read()), globalEnv)