"""
Cenários de teste: São cenários de teste de uma unidade do código.
Caso de teste: Conjunto de cenários de teste.
Asserções: Validar se algo ocorreu como esperado.
Mock: Imitamos um comportamento.
"""

from unittest import main, TestCase
from lisp.parser import tokenize, readAtom, parseTokens

class TestParser(TestCase):
    def test_if_tokenize(self):
        result = tokenize('(a (b c) c)')
        expected = ['(', 'a', '(', 'b', 'c', ')', 'c', ')']

        self.assertEqual(result, expected)

    def test_if_read_atom(self):
        self.assertEqual(readAtom('0'), 0)
        self.assertEqual(readAtom('0.5'), 0.5)
        self.assertEqual(readAtom('x'), 'x')

    def test_if_parse_tokens(self):
        self.assertRaises(SyntaxError, parseTokens, [])
        self.assertRaises(SyntaxError, parseTokens, [')', 'a'])
        self.assertEqual(parseTokens(['0']), 0)
        self.assertEqual(parseTokens(['0.5']), 0.5)
        self.assertEqual(parseTokens(['x']), 'x')
        self.assertEqual(parseTokens(tokenize("'este projeto eh muito simplessss'")), 'este projeto eh muito simplessss')

if __name__ == '__main__':
    main()