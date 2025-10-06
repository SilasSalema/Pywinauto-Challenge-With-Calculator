# Pywinauto-Challenge-With-Calculator

 
Projeto para realizar o desafio Pywinauto Challenge With Calculator com Python.
 
 
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=status&message=em%20desenvolvimento&color=GREEN&s…)
 
![Badge Python Version](http://img.shields.io/static/v1?label=python&message=3.11.5&color=blue&style=fill)
 
 
 
 
##                   BOAS PRÁTICAS UTILIZADAS DO SELENIUM                        
* [Confira aqui!](https://www.selenium.dev/pt-br/documentation/)
 
 
## Estrutura do projeto
```
 
    ├──helpers                                         # Representa todo o código que auxilia o serviço do robô.
    │   ├── tratar_erro_helper.py                                    # Código que realiza o tratamento de erros que podem ocorrer durante a execução do robô.
    │   ├── pywinauto_helper.py                                  # Código que realiza as ações genéricas na aplicação Desktop (clicar, definir valor, obter valor na aplicação Desktop).
    │   ├── excel_helper.py                                  # Código que realiza as ações em arquivo excel.
    │   ├── criar_arquivo_log_helper.py                                    # Código que realiza a criação do arquivo de log para o dia atual.
    │   ├── conter_por_extenso_helper.py                                  # Código que realiza as ações genéricas para conversão para string por extenso.
    ├── services                                       # Representa todo o código que realiza o serviço do robô.  
    │   ├── pywinauto_challenge_service.py                                   # Código que realiza o processo completo.
    │   ├── pywinauto_service.py                                  # Código que realiza as ações principais na aplicação Desktop (abrir e fechar conexão com aplicação Desktop, localizar janela).
    ├── main.py                                         # Código que realiza o inicio da execução do robô.
    ├── requirements.txt                                # Lista de dependências e suas respectivas versões.
    └── README.md                                       # Arquivo com orientações inicias do projeto e detalhes importantes.
```
## Configuração de Ambiente
- Realize o download e instação do [Python 3.12.3](https://www.python.org/downloads/release/python-3115/)
#### OBS.: Para evitar problemas de compatibilidade, desinstale qualquer versão anterior do python.
 
 
Para realizar a instalação do python na versão do projeto, acesse:
 
- B3Store
 
#
- Após a instalação, verifique se as variáveis de ambiente foram configuradas corretamente. Para isso, basta executar o comando abaixo no terminal para visualizar a versão do python:
```
python --version
```
- O resultado deve ser algo como:
```
Python 3.12.3
```
- Agora verifique se o pip, gerenciador de pacotes do Python, foi instalado corretamente:
```
pip --version
```
- O resultado deve ser algo como:
```
pip 23.2.1 from C:\Program Files\Python311\Lib\site-packages\pip (python 3.12)
```
 
```
pip install -r requirements.txt
```
##
## Editor de texto
Como editor de texto, a sugestão Visual Studio Code, porém você pode utilizar seu favorito.
Caso opte pelo Visual Studio Code, [clique aqui](https://code.visualstudio.com/download) e realize o downlaod e instalação pelo link.
- Para melhor utilização, recomenda-se a instalação das seguintes extensões:
 
| Extensão                   | Função       |
| ---------------            | -------------|
| Path Intellisense          | Auxilia no autocomplete ao inserir caminhos de arquivos e pastas no código.                     |
| Material Icon Theme        | Altera os ícones de arquivos de acordo com a extensão.                                          |
| Black Formatter                 | Auxilia na formatação dos arquivos Python de acordo com o [PEP8](https://peps.python.org/pep-0008/)    |
 
----
## Executando o robô
 Para realizar a execução do robô, utilize o comando:
```
python main.py
```
 
## Autores
 
- Silas da Silva Salema