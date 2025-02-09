import pywhatkit as kit
import time
from datetime import datetime
from contatos import ler_contatos
from mensagem import formatar_mensagem

def enviar_mensagem():
    contatos = ler_contatos()

    now = datetime.now()
    hora = now.hour
    minuto = now.minute+1

    if minuto >= 60:
        minuto -=60
        hora +=1

    for numero, nome in contatos:
        mensagem = formatar_mensagem(nome)
        kit.sendwhatmsg_instantly(numero, mensagem, 10, True, 2)
        time.sleep(4)