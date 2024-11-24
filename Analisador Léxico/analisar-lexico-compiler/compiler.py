import ply.lex as lex
from prettytable import PrettyTable

# Abrir o arquivo em txt ou modo leitura ('r')
with open('arquivofonte.txt', 'r') as arquivo:
    conteudo = arquivo.read()

# Listagem de palavras reservadas
palavrasReservadas = {
    'if': 'IF', 'then': 'THEN', 'else': 'ELSE', 'while': 'WHILE', 
    'auto': 'AUTO', 'break': 'BREAK', 'case': 'CASE', 'include': 'INCLUDE',
    'char': 'CHAR', 'const': 'CONST', 'continue': 'CONTINUE', 'default': 'DEFAULT',
    'do': 'DO', 'double': 'DOUBLE', 'enum': 'ENUM', 'extern': 'EXTERN', 'float': 'FLOAT',
    'for': 'FOR', 'goto': 'GOTO', 'inline': 'INLINE', 'int': 'INT', 'long': 'LONG',
    'register': 'REGISTER', 'restrict': 'RESTRICT', 'return': 'RETURN', 'short': 'SHORT',
    'signed': 'SIGNED', 'sizeof': 'SIZEOF', 'static': 'STATIC', 'struct': 'STRUCT',
    'switch': 'SWITCH', 'typedef': 'TYPEDEF', 'union': 'UNION', 'unsigned': 'UNSIGNED',
    'void': 'VOID', 'volatile': 'VOLATILE', '_Alignas': '_ALIGNAS', '_Alignof': '_ALIGNOF',
    '_Atomic': '_ATOMIC', '_Bool': '_BOOL', '_Complex': '_COMPLEX', '_Generic': '_GENERIC',
    '_Imaginary': '_IMAGINARY', '_Noreturn': '_NORETURN', '_Static_assert': '_STATIC_ASSERT',
    '_Thread_local': '_THREAD_LOCAL'
}

# Listagem de tokens
tokens = [
    'ADICAO', 'SUBTRACAO', 'MULTIPLICACAO', 'DIVIDE', 'ATRIBUICAO',
    'ADICAO_ATRIBUICAO', 'SUBTRACAO_ATRIBUICAO', 'EPARENT', 'DPARENT',
    'ID', 'UNDERLINE', 'MAIORQUE', 'MENORQUE', 'IGUAL', 'DIFERENTE',
    'MAIORIGUAL', 'MENORIGUAL', 'AND', 'OR', 'STRING', 'NUMERO', 'TIPO_DADO',
    'COMENTARIO_LINHA', 'COMENTARIO_MULTILINHA', 'INCLUDE'
] + list(palavrasReservadas.values())

# Tabela de símbolos
tabelaDeSimbolos = {}
id_counter = 1  # Contador para os IDs dos identificadores

# Definindo as expressões regulares para os tokens

# Operadores
t_ADICAO = r'\+'
t_SUBTRACAO = r'-'
t_MULTIPLICACAO = r'\*'
t_DIVIDE = r'/'
t_ATRIBUICAO = r'='
t_ADICAO_ATRIBUICAO = r'\+='
t_SUBTRACAO_ATRIBUICAO = r'-='

# Parênteses
t_EPARENT = r'\('
t_DPARENT = r'\)'

# Outros tokens simples
t_UNDERLINE = r'\_'
t_MAIORQUE = r'\<'
t_MENORQUE = r'\>'
t_IGUAL = r'\='
t_DIFERENTE = r'\!='
t_MAIORIGUAL = r'\>='
t_MENORIGUAL = r'\<='
t_AND = r'\&&'
t_OR = r'\|\|'

# Strings (sequências de caracteres entre aspas)
t_STRING = r'"([^"\\]*(\\.[^"\\]*)*)"'  

# Tipos de dados (int, float, char, etc.)
t_TIPO_DADO = r'int|float|char|double|short|long|void'

# Números (inteiros, flutuantes e notação científica)
t_NUMERO = r'(-?\d+(\.\d*)?([eE][-+]?\d+)?)'

# Comentários de linha e de múltiplas linhas
t_COMENTARIO_LINHA = r'//.*'  # Comentários de linha
t_COMENTARIO_MULTILINHA = r'/\*[\s\S]*?\*/'  # Comentários de múltiplas linhas

# Diretivas de Pré-processamento (como #include)
t_INCLUDE = r'\#\s*include'

# Espaços em branco e quebras de linha (para ignorar)
t_ignore  = ' \t'

# Identificadores (nomes de variáveis e funções)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = palavrasReservadas.get(t.value, 'ID')  # Verifica se é uma palavra reservada
    if t.type == 'ID':  # Se for identificador, trata como tal
        if t.value not in tabelaDeSimbolos:
            global id_counter
            tabelaDeSimbolos[t.value] = {'type': 'ID', 'scope': 'global', 'id': id_counter}
            id_counter += 1  # Incrementa o contador para o próximo ID
        else:
            # Caso o identificador já exista, reutiliza o ID atribuído anteriormente
            pass
    return t

# Define uma regra para monitorar qual o número da linha que o caractere está
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Função de erro (para caracteres não reconhecidos)
def t_error(t):
    print(f"Erro Lexical: Caractere '{t.value[0]}' na linha {t.lineno}, posicao {t.lexpos}")
    t.lexer.skip(1)

# Build do lexer
lexer = lex.lex()

# Função de Debugging - Exibe os tokens de forma organizada
def debug_tokens(verbose=False):
    """
    Função de Debug para exibir tokens identificados, com formatação organizada.
    
    Parâmetros:
    - verbose: se True, exibe mais detalhes sobre cada token (valor, tipo, posição e linha).
    """
    print("\n" + "="*50)
    print("Iniciando a Tokenizacao do Codigo")
    print("="*50 + "\n")
    
    lexer.input(conteudo)  # Alimenta o lexer com o conteúdo do arquivo
    
    token_count = 0
    while True:
        tok = lexer.token()
        if not tok:
            break
        token_count += 1
        
        # Exibição de informações de debug com formato simples
        if verbose:
            print(f"Token #{token_count}:")
            print(f"  Tipo: {tok.type}")
            print(f"  Valor: {tok.value}")
            print(f"  Linha: {tok.lineno}")
            print(f"  Posicao: {tok.lexpos}")
            print("-" * 50)  # Separador entre tokens
        else:
            print(f"Token #{token_count}: {tok.type} -> {tok.value}")
    
    print("="*50)
    print(f"Tokenizacao concluida. Total de tokens encontrados: {token_count}")
    print("="*50 + "\n")

# Alimenta o lexer com dados do arquivo
lexer.input(conteudo)

# Tokenização e exibição dos tokens
print("\nTokens identificados:")
while True:
    tok = lexer.token()
    if not tok: 
        break
    print(f"Valor: {tok.value}, Linha: {tok.lineno}, Posicao: {tok.lexpos}, Tipo: {tok.type}")

# Tabela de Símbolos com IDs
tabela_simbolos = PrettyTable(['ID', 'Nome', 'Tipo', 'Escopo'])
for chave, valor in tabelaDeSimbolos.items():
    tabela_simbolos.add_row([valor['id'], chave, valor['type'], valor['scope']])

tabela_simbolos.align['Nome'] = 'l'
print("\nTABELA DE SIMBOLOS (Com IDs)")
print(tabela_simbolos)

# Tabela dos identificadores encontrados (sem IDs, apenas nome, tipo e escopo)
tabela_identificadores = PrettyTable(['Nome', 'Tipo', 'Escopo'])
for chave, valor in tabelaDeSimbolos.items():
    tabela_identificadores.add_row([chave, valor['type'], valor['scope']])

tabela_identificadores.align['Nome'] = 'l'
print("\nTABELA DE IDENTIFICADORES")
print(tabela_identificadores)

# Ativando o debug com o parâmetro verbose (True)
debug_tokens(verbose=True)






