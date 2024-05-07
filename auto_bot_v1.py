'''
DEMANDA:
PRECISO AUTOMATIZAR MINHAS MENSAGENS P/ MEUS CLIENTES, GOSTARIA DE SABER VALORES, E GOSTARIA QUE ENTRASSEM EM CONTATO COMIGO P/ EXPLICAR MELHOR, 
QUERO PODER MANDAR MENSAGENS DE COBRANÇA EM DETERMINADO DIA COM CLIENTES COM VENCIMENTO DIFERENTE
'''

#Instalando bibliotecas essenciais para o funcionamento do código.
import openpyxl
import time
import webbrowser
import pyautogui
from urllib.parse import quote

#Abrindo o WebWhatsApp
webbrowser.open("https://web.whatsapp.com")
time.sleep(30)

#Abrindo a planilha
plan_cliente = openpyxl.load_workbook("clientes.xlsx")
pag_plan_cliente = plan_cliente["Pagina1"]

#Iterando sobre cada linha
for linha in pag_plan_cliente.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value

    #Personalizade sua mensagem!
    mensagem_personalizada = f'Olá {nome}, sua internet vence no dia {vencimento.strftime('%d/%m/%Y')}! Para evitar o bloqueio da linha, efetue o pagamento pelo link: https://www.pagarinternet.com.br'
