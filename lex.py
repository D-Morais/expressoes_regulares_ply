import ply.lex as lex
# 1) Números de telefones celulares no Brasil (código de área + número do celular).
tokens = (
    'CNPJ',
    'CPF',
    'HTML',
    'ID',
    'NUMEROS_REAIS',
    'PALAVRAS',
    'PLACA',
    'TELEFONE',
    'URL',
)


#Números de telefones celulares no Brasil (código de área + número do celular).
#def t_TELEFONE(t):
#    r'(\+\d{2}\d{11})'
#    if len(t.lexer.lexdata) != 14:
#        t_error(t)
#    else:
#        return t

#2) Placas de Carros Brasileiros (Padrão antigo, aquele com 3 letras e 4 números na sequência).
#def t_PLACA(t):
#    r'(([a-z]{3}|[A-Z]{3})\-\d{4})'
#    return t


#3) CPF (aqui deve ser escolhido com ponto e traço ou apenas numérico).
#def t_CPF(t):
#    r'(\d{5}\-\d{3})'
#    return t


#4) Números reais.
#def t_NUMEROS_REAIS(t):
#    r'(\d{1,}\.\d*)'
#    return t

#5) Tags HTML (padrão).
def t_HTML(t):
    r'(\<\w*d*.*\>)'
    return t


#6) URL de páginas web.
#def t_URL(t):
#    r'((http|https)\:\//\w*d*[\S+?]*)'
#    return t


#7) Palavras da Língua Portuguesa (qualquer uma, com ou sem significado – não iremos analisar a semântica).
#def t_PALAVRAS(t):
#    r'[a-zA-Z][a-zA-Z]*'
#    return t


#8) CNPJ (aqui deve ser escolhido com ponto e traço ou apenas numérico).
#def t_CNPJ(t):
#    r'(\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2})'
#    return t


#Identificadores da Linguagem C.
#def t_ID(t):
#    r'[a-z_][a-zA-Z_0-9]*'
#    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

resultado_lexema = []
# Error handling rule
def t_error(t):
    for i in range(0, len(t.lexer.lexdata)):
        resultado_lexema.append(t.value[i])
        t.lexer.skip(1)
    print(f"Erro {''.join(resultado_lexema)}")

    # Test it out
lexer = lex.lex()

data = '''<TESTE = 2+"@>'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
     tok = lexer.token()
     if not tok:
         break      # No more input
     print(tok.type, tok.value, tok.lineno, tok.lexpos)
     print(tok)