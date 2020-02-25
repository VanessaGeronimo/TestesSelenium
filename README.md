# Automação de Cadastro

Automação de cadastro simples utilizando selenium e python.

## Como Utilizar

### Firefox

Como o projeto foi desenvolvido utilizando o navegador firefox, ele é necessário para executar o mesmo, caso esteja usando windows pode baixar [neste](https://www.mozilla.org/pt-BR/firefox/new/) link, caso esteja usando linux, pode instalar utilizando o comando `apt install firefox` ou similar.

### Python

Esse projeto foi desenvolvido utilizando python 3, para faze-lo funcionar abra o terminal e verifique se você tem o python instalado digitando `python3`, caso o prompt do python apareça, aperte `ctrl + d` para sair, caso você não tenha instalado, acesse: [python](https://www.python.org/), faça o download do executavel e instale seguindo os guias disponiveis [aqui](https://wiki.python.org/moin/BeginnersGuide/Download) em ingles e  [aqui](https://python.org.br/instalacao-windows/) em português.


### Pip

O pip é um gerenciador de dependências do python, é necessário instalar o Pip para que se instale todas as dependências e bibliotecas necessárias para o projeto funcionar.
**No Linux**, rodar o comando `sudo - apt install python3-pip`
**No Windows**, Baixe o arquivo [get-pip.py](https://bootstrap.pypa.io/get-pip.py) em seguida execute, e dependendo de onde baixou use o `cd` para navegar, seguindo o exemplo abaixo:

```
cd C:\Users\[Nome do seu usuário padrão]\Downloads
python get-pip.py
```

### Selenium
 Selenium é uma ferramenta para automação de testes.

 Para instalar o Selenium no Linux e no Windows, é necessário rodar o seguinte comando:
 `sudo pip install selenium`


### GeckoDriver
É um driver que é necessário ser utilizado para as novas versões do Firefox, auxiliando na automação de testes. Ele já esta no repositório, mas como esse projeto foi desenvolvido em um ambiente Linux, caso seja necessário executar no Windows, baixar o [GeckoDriver.exe](https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win64.zip), 
no código é necessário fazer uma alteração 
```python
webdriver.Firefox(executable_path='geckodriver.exe') 
# Alterar o nome do arquivo para o nome correspondente
```
### Executando
* Após instalar todas as dependências necessárias, deve- se executar o comando `python3 main.py`





