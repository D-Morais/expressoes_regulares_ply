"""
 Nessa atividade foi seguido o exemplo de codificação da ferramenta,
onde se adotou a forma estruturada for métodos para a criação das expressões regulares.
 Criamos as regras seguindo a ordem do arquivo disponibilizado pela professora, e em cada método deixamos
um pequeno comentario sobre qual o padrão que a expressão regular vai procurar.
 A entrada de dados é por meio de uma variável dentro do código, onde se deve escrever nela as entradas antes de executar o código para testar,
importante lembrar que o conteúdo a ser testado, deve estar dentro das aspas(''' ''').
 Um ponto que vale ressaltar é que as expressões regulares(ER) para PALAVRAS e IDs se sobrepoem, ou seja, a ER para
PALAVRA tem preferencia sobre a ER de ID, quando temos apenas uma palavra como entrada, já quando temos mais palavras como entrada
a ordem se inverte e o ID passa a ter prioridade, então para testar o ID isoladamente é preciso comentar o método da ER de PALAVRAS e para testar
o ER de PALAVRA isoladamente é necessário comentar o ER de ID.
"""

import ply.lex as lex

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
"""
A forma como o grupo decidiu aceitar os números de 
telefone celulares é seguindo o seguinte padrão +5551999999999.
"""
def t_TELEFONE(token):
    r'(\+\d{2}\d{11})'
    return token


#2) Placas de Carros Brasileiros (Padrão antigo, aquele com 3 letras e 4 números na sequência).
"""
A forma como o grupo decidiu aceitar as placas de carros
é seguindo o seguinte padrão AAA-000 ou aaa-000.
"""
def t_PLACA(token):
    r'(^([a-z]{3}|[A-Z]{3})\-\d{4})'
    return token


#3) CPF (aqui deve ser escolhido com ponto e traço ou apenas numérico).
"""
A forma como o grupo decidiu para o CPF é seguindo o seguinte 
padrão 000000000-00.
"""
def t_CPF(token):
    r'(\d{9}\-\d{2})'
    return token


#4) Números reais.
"""
São aceitos todos os modos de números reais, seja 1.1, 11.1, 11.111, e assim sucessivamente.
"""
# 1.1 11.2 111.2
def t_NUMEROS_REAIS(token):
    r'(\d{1,}\.\d*)'
    return token


#5) Tags HTML (padrão).
"""
Nas Tags HTML são aceitos as tag que tenha <>, podendo haver
qualquer coisa dentro dela.
"""
def t_HTML(token):
    r'(\<\w*d*.*\>)'
    return token


#6) URL de páginas web.
"""
As URLs serão aceitas aquelas que seguirem o seguinte padrão:
http:// ou https://, sendo aceito qualquer coisa (menos espaços em branco) 
após.
"""
def t_URL(token):
    r'((http|https)\:\//\w*d*[\S+?]*)'
    return token


#7) Palavras da Língua Portuguesa (qualquer uma, com ou sem significado – não iremos analisar a semântica).
"""
As palavras podem conter qualquer sequência de letras,
tanto maiúsculas, quanto minúsculas.
"""
def t_PALAVRAS(token):
    r'^[a-zA-Zç]+$'
    return token


#8) CNPJ (aqui deve ser escolhido com ponto e traço ou apenas numérico).
"""
A forma como o grupo decidiu para o CPF é seguindo o seguinte 
padrão 11111111/0001-22.
"""
def t_CNPJ(token):
    r'(\d{2}\d{3}\d{3}\/\d{4}\-\d{2})'
    return token


#Identificadores da Linguagem C.
"""
O ID é baseado na linguagem C, logo pode começar com
letras minúsculas, maiúsculas ou _, e após podem ter letras
minúsculas ou maiúsculas, _ e/ou números.
"""
def t_ID(token):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return token


# Conta o número de linhas.
def t_newline(token):
    r'\n+'
    token.lexer.lineno += len(token.value)


# Ignora os caracteres de espaço e tabulação.
t_ignore = ' \t'

# Método para captura e apresentação de erros.
def t_error(token):
    print(f'LexToken ({token.type}, valor: {token.value[0]}, linha: {token.lineno}, posição: {token.lexpos})')
    token.lexer.skip(1)


lexer = lex.lex()

# Aqui é inserido os dados para teste da ferramenta.
dado = '''teste'''

# Os dados são colocados no lexer
lexer.input(dado)

# Tokenizar
while True:
    tok = lexer.token()
    if not tok:
        break  # Quando não há mais tokens
    print(f'LexToken ({tok.type}, valor: {tok.value}, linha: {tok.lineno}, posição: {tok.lexpos})')
