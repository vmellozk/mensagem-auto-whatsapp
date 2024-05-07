# Automatização de Mensagens para Clientes via WhatsApp

## O que é?

Este é um programa Python que automatiza o envio de mensagens para clientes via WhatsApp. 
Ele lê uma planilha Excel que contém informações dos clientes, como nome, número de telefone 
e data de vencimento do serviço. Com base nessas informações, o programa envia mensagens 
personalizadas para cada cliente, lembrando-os do vencimento do serviço e fornecendo um link 
para pagamento.

## Como foi feito?

O programa foi escrito em Python e utiliza as seguintes bibliotecas:

- `openpyxl`: Para ler os dados da planilha Excel.
- `time`: Para adicionar pausas entre as operações.
- `webbrowser`: Para abrir o WhatsApp Web.
- `pyautogui`: Para automatizar as interações com a interface do WhatsApp Web.
- `urllib.parse`: Para codificar a mensagem para uma URL segura.
- `logging`: Para registrar possíveis erros.
- `pynput`: Para monitorar as teclas pressionadas pelo usuário.

## Por que foram utilizadas essas bibliotecas?

- `openpyxl`: Para ler dados de uma planilha Excel.
- `time`: Para adicionar pausas entre as operações, garantindo que o programa não avance 
  antes que uma operação seja concluída.
- `webbrowser`: Para abrir o WhatsApp Web no navegador padrão.
- `pyautogui`: Para automatizar as interações com a interface do WhatsApp Web, como clicar 
  em botões e inserir texto.
- `urllib.parse`: Para codificar a mensagem para uma URL segura, garantindo que caracteres 
  especiais sejam tratados corretamente na mensagem.
- `logging`: Para registrar possíveis erros que ocorram durante a execução do programa.
- `pynput`: Para monitorar as teclas pressionadas pelo usuário e iniciar a execução do 
  programa quando a combinação de teclas específica é pressionada.

## Como utilizar o programa?

1. Instale as bibliotecas necessárias:
   
2. Ter uma planilha Excel com os dados dos clientes (pode ser personalizável):

PS: Salve a planilha com o nome `clientes.xlsx` e certifique-se de que ela está no mesmo 
diretório que o arquivo do programa.

3. Execute o programa utilizando o comando:

python "nome_do_programa".py

4. Quando quiser enviar as mensagens, pressione a combinação de teclas `Ctrl + Alt + F12`. 
Isso abrirá o WhatsApp Web e iniciará o envio das mensagens.



Dúvidas sobre o Código

## Por que abriu a planilha antes de mandar a mensagem?
A planilha é aberta antes do envio das mensagens para garantir que os dados dos clientes 
estejam atualizados no momento do envio.


## Por que iterou sobre cada linha da planilha antes de enviar a mensagem?
A iteração sobre cada linha da planilha permite que o programa envie mensagens personalizadas 
para cada cliente, informando o vencimento do serviço de forma individualizada.


## Funcionamento passo a passo do aplicativo

1. O usuário pressiona a combinação de teclas `Ctrl + Alt + F12`.

2. O programa abre o WhatsApp Web.

3. O programa lê os dados dos clientes a partir da planilha Excel.

4. Para cada cliente, o programa envia uma mensagem personalizada informando o vencimento 
do serviço e fornecendo um link para pagamento.

5. Após o envio das mensagens, o programa fecha o WhatsApp Web.

6. O programa registra quaisquer erros que ocorram durante a execução no arquivo `erros.log`.


## Explicações adicionais sobre o código

### `on_press`

`on_press` é uma função que é chamada quando uma tecla é pressionada.

### `on_release`

`on_release` é uma função que é chamada quando uma tecla é solta.

### `listener`

`listener` é um objeto que "escuta" as teclas e chama as funções `on_press` e `on_release`.

### `getattr(sys, 'frozen', False)`

`getattr(sys, 'frozen', False)` verifica se o script está sendo executado como um executável 
gerado pelo PyInstaller. Se o script estiver congelado, o caminho de trabalho é alterado 
para o diretório temporário onde os arquivos foram extraídos.

### `os.chdir(sys._MEIPASS)`

`os.chdir(sys._MEIPASS)` altera o diretório de trabalho para o diretório temporário onde 
os arquivos foram extra
