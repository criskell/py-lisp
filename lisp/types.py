class Symbol(str):
    pass

Number        = (int, float)     
Atom          = (Symbol, Number) 
List          = list             
Expression    = (Atom, List)     
Env           = dict
String        = str