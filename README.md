# Analisador-Lexico-Compiler

Este projeto implementa um analisador léxico (ou lexer) em Python, desenvolvido para realizar a leitura e análise de arquivos de código fonte escritos na linguagem C. Utilizando a biblioteca PLY (Python Lex-Yacc), o projeto realiza a tokenização do código C, identificando e categorizando os diversos elementos sintáticos da linguagem, como operadores, identificadores, palavras reservadas, números, tipos de dados, strings, comentários e diretivas de pré-processamento.

Funcionalidades:

- Tokenização Completa: O lexer identifica e classifica todos os tokens presentes no código-fonte, incluindo operadores, palavras reservadas, identificadores, números, strings, comentários, e diretivas de pré-processamento (como #include).
- Tabela de Símbolos: Ao longo da análise, o lexer cria uma tabela de símbolos, onde são registrados os identificadores encontrados, com seu tipo, escopo e um ID único para cada um.
- Reconhecimento de Comentários: O lexer também é capaz de identificar e ignorar tanto os comentários de linha (//) quanto os de múltiplas linhas (/* */).
- Exibição de Tokens: A ferramenta permite visualizar os tokens identificados de forma detalhada, com informações como tipo, valor, linha e posição no código-fonte.
- Função de Debug: O projeto inclui uma função de debugging que exibe informações detalhadas sobre os tokens encontrados, facilitando o acompanhamento e a correção de erros durante o processo de tokenização.
- Geração de Tabelas: O código gera tabelas organizadas dos tokens identificados e da tabela de símbolos, com informações claras sobre os identificadores e seus respectivos atributos.

Tecnologias Utilizadas:

- Python: Linguagem de programação utilizada para a implementação do analisador léxico.
- PLY (Python Lex-Yacc): Biblioteca Python usada para construir o lexer e realizar a análise léxica.
- PrettyTable: Biblioteca utilizada para gerar tabelas formatadas, exibindo os tokens e os identificadores na tabela de símbolos de forma legível.

Como Usar
1. Instale as dependências
Certifique-se de ter o Python instalado e depois instale as bibliotecas necessárias utilizando o pip:

bash
pip install ply prettytable

2. Prepare o código fonte
Crie um arquivo com o código fonte em C que deseja analisar (por exemplo, arquivofonte.txt).

3. Execute o analisador
Execute o script Python para iniciar a análise léxica do arquivo de código fonte:

bash
python analisador_lexico.py

4. Resultados
O script exibirá os tokens identificados no código.
As tabelas de símbolos e identificadores serão apresentadas no terminal.
Se você ativar o modo de depuração, o processo de tokenização será exibido detalhadamente.

Estrutura do Projeto

analisador_lexico.py: Script principal contendo a implementação do lexer.
arquivofonte.txt: Exemplo de arquivo de código fonte em C para análise.
README.md: Este arquivo de documentação.

Contribuições
Contribuições são bem-vindas! Se você encontrar algum problema ou quiser adicionar novas funcionalidades, sinta-se à vontade para abrir uma issue ou enviar um pull request.
