"""
O processo de parsing significa obter uma representação interna do interpretador
de um código fonte.

É divido em:
1. Analise léxica: Dado um código-fonte, separamos o código em tokens.
2. Analise sintática: Transforma a sequência de tokens numa AST.
"""

from lisp.types import Symbol

def parse(source):
    return parseTokens(tokenize(source))

def tokenize(source):
    """
    Converte uma string em uma sequência de tokens.
    """
    return source.replace('(', ' ( ').replace(')', ' ) ').split()

def readAtom(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)

def parseTokens(tokens):
    """
    Ler uma expressão a partir de uma sequência de tokens.
    """
    if len(tokens) == 0:
        raise SyntaxError('Fim do arquivo')
    
    token = tokens.pop(0)

    if token == ")":
        raise SyntaxError("Token ')' não esperado")
    elif token == "(":
        l = []
        while tokens[0] != ')':
            l.append(parseTokens(tokens))
        tokens.pop(0)
        return l
    else:
        return readAtom(token)