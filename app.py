import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
from datetime import datetime



webbrowser.open('https://web.whatsapp.com/')
sleep(30)

hoje = datetime.today().date()

workbook = openpyxl.load_workbook('nomes.xlsx')
pagina_nomes = workbook['Página1']

for linha in pagina_nomes.iter_rows(min_row=2):

    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value

    if vencimento.date() == hoje:
        print(f"Enviar mensagem para {nome}")

    mensagem = f"Olá {nome}, seu vencimento é {vencimento.strftime('%d/%m/%Y')}. Favor enviar para 222.222.222-22"

    try:


        link = f"https://api.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}"
        webbrowser.open(link)

        sleep(10)

        continuar = pyautogui.locateCenterOnScreen('continuar.png')

        sleep(10)

        pyautogui.click(continuar[0], continuar[1])

        sleep(10)

        pyautogui.press("enter")

        sleep(3)

        pyautogui.hotkey('ctrl', 'w')

        sleep(3)

    except:
        print(f"Não foi possível mandar mensagem para {nome}.")

        with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo_erros:
            arquivo_erros.write(f"{nome};{telefone}\n")
