from lisp.types import Symbol

def parse(source):
    return parseTokens(tokenize(source))

def tokenize(source):
    return source.replace('(', ' ( ').replace(')', ' ) ').replace("'", " ' ").split()

def readAtom(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)

def parseTokens(tokens):
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
    elif token == "'":
        string = ""
        first = True
        while tokens[0] != "'":
            if first:
                sep = ''
                first = False
            else:
                sep = ' '
            string += sep + tokens.pop(0)
        tokens.pop(0)
        return string
    else:
        return readAtom(token)