# 🤖 Automatização de Mensagens para Clientes via WhatsApp

## 📋 Descrição

Este é um script Python que automatiza o envio de mensagens via WhatsApp, utilizando uma planilha Excel com dados dos clientes (nome, telefone, data de vencimento). O programa envia mensagens personalizadas para lembrar os clientes do vencimento do serviço e fornece links para pagamento.

## ⚙️ Tecnologias Utilizadas

- 📊 `openpyxl`: Para ler dados da planilha Excel.
- ⏱️ `time`: Para adicionar pausas entre as ações.
- 🌐 `webbrowser`: Para abrir o WhatsApp Web.
- 🖱️ `pyautogui`: Para automatizar interações na interface do WhatsApp Web.
- 🔐 `urllib.parse`: Para codificar mensagens para URLs seguras.
- 📜 `logging`: Para registrar erros durante a execução.
- ⌨️ `pynput`: Para monitorar teclas pressionadas.

## 🚀 Como Usar

### 1. Instalação das Dependências

Instale as bibliotecas necessárias executando o seguinte comando:

```bash
pip install openpyxl pyautogui pynput webbrowser
```

### 2. Preparando a Planilha

Crie uma planilha Excel com as seguintes informações dos clientes:

- Nome
- Número de telefone
- Data de vencimento do serviço

Salve a planilha com o nome clientes.xlsx no mesmo diretório do script.

### 3. Executando o Programa

Execute o script com o comando:

```bash
python nome_do_programa.py
```

### 4. Enviando as Mensagens

Para iniciar o envio das mensagens, pressione a combinação de teclas Ctrl + Alt + F12. O WhatsApp Web será aberto e as mensagens serão enviadas automaticamente.

## 🔧 Funcionamento

- Pressione Ctrl + Alt + F12: O WhatsApp Web será aberto.
- Leitura da Planilha: O programa lê os dados da planilha Excel.
- Envio das Mensagens: O programa envia mensagens personalizadas para cada cliente, incluindo o vencimento do serviço e o link para pagamento.
- Fechamento do WhatsApp Web: Após o envio das mensagens, o WhatsApp Web será fechado.
- Logs de Erros: Qualquer erro durante a execução será registrado no arquivo erros.log.

## 🔍 Contribuição

Sinta-se à vontade para fazer contribuições! Para isso, basta seguir os seguintes passos:

- Faça um fork deste repositório.
- Crie uma branch para sua modificação.
- Faça o commit das suas alterações.
- Abra um pull request.

## 📄 Licença
Este projeto está licenciado sob a MIT License. O arquivo 'LICENSE' ainda será disponibilizado.
