from utilidades import readLinesFile, writeInFile, appendInFile

import ply.lex as lex

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS' ]
reserved = {
    'suma' : 'PLUS',
    'resta' : 'MINUS',
    'multiplicacion' : 'TIMES',
    'division' : 'DIVIDE',
    
}
t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.lower() in reserved :
        t.type = reserved[ t.value.lower() ]
        t.value = switchValue (t.type)
    return t

def switchValue(x):
    return {
        'PLUS': '+',
        'MINUS': '-',
        'TIMES': '*',
        'DIVIDE': '/',
        'EQUALS' : '='
    }[x]

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer

data = ''
for exp in readLinesFile('expresiones.in'):
    data+=exp
lex.input(data)
#lex.input("x = 3 - 4 + 5 * 6")
while True:
    tok = lex.token()
    if not tok: break
    print(str(tok.value) + " - " + str(tok.type))
