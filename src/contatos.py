import os

contatos_arquivo = os.getenv('CONTATOS_ARQUIVO', '../data/contatos.txt')

CONTATOS_ARQUIVO = os.path.join(os.path.dirname(__file__), contatos_arquivo)

def ler_contatos():
    if not os.path.exists(CONTATOS_ARQUIVO):
        return[]
    
    with open(CONTATOS_ARQUIVO, "r") as file:
        return [linha.strip().split(";") for linha in file.readlines() if linha.strip()]
    
def adicionar_contato(numero, nome):
    if len(numero) != 11 or not numero.isdigit():
        return "Número inválido! Deve ter 11 dígitos (DDD + 9 dígitos)"

    if " " in nome:
        return "O nome não pode conter espaços!"
    
    with open(CONTATOS_ARQUIVO, "a") as file:
        file.write(f"+55{numero};{nome}\n")
    return "Contato adicionado com sucesso!"

def listar_contatos():
    contatos = ler_contatos()
    return [f"{nome}: {numero}" for numero, nome in contatos]

def editar_contato(numero_antigo, novo_numero, novo_nome):
    contatos = ler_contatos()
    contato_encontrado = False

    with open(CONTATOS_ARQUIVO, "w") as file:
        for numero, nome in contatos:
            numero_com_ddd = f"+55{numero_antigo}"

            if numero_com_ddd == numero:  
                file.write(f"+55{novo_numero};{novo_nome}\n") 
                contato_encontrado = True
            else:
                file.write(f"{numero};{nome}\n")
    
    if contato_encontrado:
        return "Contato editado com sucesso!"
    else:
        return "Contato não encontrado!"