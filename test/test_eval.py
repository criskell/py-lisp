from unittest import main, TestCase
from lisp.eval import evaluate
from lisp.parser import parse
from lisp.types import Env

class TestEval(TestCase):
    def test_if_evaluate(self):
        self.assertEqual(evaluate(parse('x'), Env(x=5)), 5)

        e = Env()
        evaluate(parse('(define x 10)'), e)
        self.assertEqual(e.get('x'), 10)

if __name__ == '__main__':
    main()