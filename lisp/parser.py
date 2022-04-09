import shlex

from lisp.types import Symbol

def parse(source):
    return parseTokens(tokenize(source))

def tokenize(source):
    return shlex.split(source.replace('(', ' ( ').replace(')', ' ) '), posix=False)

def readAtom(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token if isString(token) else Symbol(token)

def parseTokens(tokens):
    if len(tokens) == 0:
        raise SyntaxError('Fim do arquivo')
    token = tokens.pop(0)
    if token == ')':
        raise SyntaxError("Token ')' não esperado")
    elif token == '(':
        l = []
        while tokens[0] != ')':
            l.append(parseTokens(tokens))
        tokens.pop(0)
        return l
    else:
        return readAtom(token)

def isString(token):
    return token[0] == "'" and token[-1] == "'"