import os

mensagem_arquivo = os.getenv('MENSAGEM_ARQUIVO', '../data/mensagem.txt')

MENSAGEM_ARQUIVO = os.path.join(os.path.dirname(__file__), mensagem_arquivo)

def ler_mensagem():
    try:
        with open(MENSAGEM_ARQUIVO, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Arquivo de mensagem não encontrado!"
    except Exception as e:
        return f"Erro ao ler o arquivo: {e}"

MENSAGEM_PADRAO = ler_mensagem()

def carregar_mensagem():
    if not os.path.exists(MENSAGEM_ARQUIVO):
        salvar_mensagem(MENSAGEM_PADRAO)

    with open(MENSAGEM_ARQUIVO, "r", encoding="utf-8") as file:
        return file.read()
    
def salvar_mensagem(nova_mensagem):
    with open(MENSAGEM_ARQUIVO, "w", encoding="utf-8") as file:
        file.write(nova_mensagem)

def formatar_mensagem(nome):
    mensagem = carregar_mensagem()
    return mensagem.replace("{nome}", nome)