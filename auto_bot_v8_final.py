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
import logging
from pynput import keyboard
import sys
import os

# Se o código estiver sendo executado pelo PyInstaller, ajusta o caminho de trabalho para o diretório onde o executável está.
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

#Configurando o logger
logging.basicConfig(filename='erros.log', level=logging.ERROR, format='%(asctime)s - %(message)s')

#Criando função para envio de mensagem
def enviar_mensagem(telefone, mensagem):

    try:
        link_direto_wpp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        webbrowser.open(link_direto_wpp)
        time.sleep(20)
        #Localizando o ícone a ser clicado
        clicar_icone_enviar = pyautogui.locateCenterOnScreen('icone_enviar.png')
        time.sleep(1)
        #Passando a coordernada da imagem utilizada
        pyautogui.click(clicar_icone_enviar[0], clicar_icone_enviar[1])
        time.sleep(8)

        #Verificando se a página do WhatsApp Web está aberta antes de fechar a aba
        if "web.whatsapp.com" in pyautogui.getActiveWindow().title:
            #Combinando tecla para fechar a aba
            pyautogui.hotkey('ctrl', 'w')

    except Exception as error:
            print(f"OPS! Ocorreu um erro ao tentar enviar a mensagem para {nome}: {error}")
            logging.error(f"Não foi possível enviar a mensagem para {nome}: {error}")

# Função para pressionar as teclas
def on_press(key):
    # Se as teclas pressionadas forem Ctrl, Alt e F12
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.alt_l or key == keyboard.KeyCode.from_char('F12'):

        #Abrindo o WebWhatsApp
        webbrowser.open("https://web.whatsapp.com")
        time.sleep(30)

        #Abrindo a planilha // Variável declarada como global para poder ser utilizada fora da função
        global pag_plan_cliente
        plan_cliente = openpyxl.load_workbook("clientes.xlsx")
        pag_plan_cliente = plan_cliente["Pagina1"]

# Esta função é chamada quando uma tecla é solta. A variável key é necessária como parâmetro da função, mesmo que não seja usada explicitamente.
def on_release(key):
    pass

# A variável key na função on_release não precisa ser declarada como global
# O parâmetro "on_press" recebe a função "on_press" definida anteriormente, assim como "on_release"
# "as listener" é usado para atribuir o objeto listener a uma variável chamada listener, permitindo que o programa continue em execução para capturar teclas pressionadas e soltas.
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

#Iterando sobre cada linha
for linha in pag_plan_cliente.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value

    #Verifica se acabou os valores da planilha
    if not nome and not telefone and not vencimento:
        print("Fim da planilha!")
        break

    #Personalizade sua mensagem aqui!
    mensagem_personalizada = f"Olá {nome}, sua internet vence no dia {vencimento.strftime('%d/%m/%Y')}! Para evitar o bloqueio da linha, efetue o pagamento pelo link: https://www.pagarinternet.com.br"

    #Abrindo exceção de erros no bloco para enviar a mensagem para cada cliente
    try:
        #Verificando se a página do WhatsApp Web está aberta antes de fechar a aba
        if "web.whatsapp.com" in pyautogui.getActiveWindow().title:
            #Fechando a página inicial
            pyautogui.hotkey('ctrl', 'w')

        #Abrindo o convite de contato e colando a mensagem
        enviar_mensagem(telefone, mensagem_personalizada)
        
    #"Exception" para capturar todas as exceções que ocorrerem. // "as error" atribui o objeto de exceção à variável "error"
    except Exception as error:
        print(f"OPS! Ocorreu um erro ao tentar enviar a mensagem para {nome}: {error}\n.")
        time.sleep(1)
        print(f"Tentando novamente...")
        time.sleep(2)

        #Ele vai tentar executar o código novamente
        try:
            enviar_mensagem(telefone, mensagem_personalizada)
        except:
            print(f"OPS! Novamente ocorreu um erro ao tentar enviar a mensagem para {nome}: {error}\n")
            logging.error(f"Não foi possível enviar a mensagem para {nome}: {error}\n")