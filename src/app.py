import tkinter as tk
from tkinter import messagebox, scrolledtext
from contatos import adicionar_contato, editar_contato, listar_contatos
from mensagem import carregar_mensagem, salvar_mensagem
from envio import enviar_mensagem

def adicionar():
    numero = entry_numero.get()
    nome = entry_nome.get()
    resultado = adicionar_contato(numero, nome)
    messagebox.showinfo("Resultado", resultado)

def editar():
    numero_antigo = entry_numero_antigo.get()
    novo_numero = entry_novo_numero.get()
    novo_nome = entry_novo_nome.get()
    resultado = editar_contato(numero_antigo, novo_numero, novo_nome)
    messagebox.showinfo("Resultado", resultado)

def mostrar_contatos():
    contatos_texto.delete(1.0, tk.END)
    contatos = listar_contatos()
    contatos_texto.insert(tk.END, "\n".join(contatos))

def salvar_mensagem_edicao():
    nova_mensagem = mensagem_texto.get("1.0", tk.END).strip()
    salvar_mensagem(nova_mensagem)
    messagebox.showinfo("Sucesso", "Mensagem salva com sucesso!")

def enviar():
    enviar_mensagem()
    messagebox.showinfo("Envio", "Mensagens enviadas!")


# Configurações:
root = tk.Tk()
root.title("Bot Pizzaria Vó Nice")
root.geometry("1000x800")
root.configure(bg="#f0f0f0")
font_style = ("Arial", 12)

# Labels:
label_numero = tk.Label(root, text="Número (DDD + 9 dígitos):", font=font_style, bg="#f0f0f0")
label_numero.pack()
entry_numero = tk.Entry(root, font=font_style)
entry_numero.pack()

label_nome = tk.Label(root, text="Nome (sem espaços):", font=font_style, bg="#f0f0f0")
label_nome.pack()
entry_nome = tk.Entry(root, font=font_style)
entry_nome.pack()

btn_adicionar = tk.Button(root, text="Adicionar Contato", command=adicionar, font=font_style, bg="#4CAF50", fg="white")
btn_adicionar.pack()

label_numero_antigo = tk.Label(root, text="Número Antigo (DDD + 9 dígitos):", font=font_style, bg="#f0f0f0")
label_numero_antigo.pack()
entry_numero_antigo = tk.Entry(root, font=font_style)
entry_numero_antigo.pack()

label_novo_numero = tk.Label(root, text="Novo Número (DDD + 9 dígitos):", font=font_style, bg="#f0f0f0")
label_novo_numero.pack()
entry_novo_numero = tk.Entry(root, font=font_style)
entry_novo_numero.pack()

label_novo_nome = tk.Label(root, text="Novo Nome (sem espaços):", font=font_style, bg="#f0f0f0")
label_novo_nome.pack()
entry_novo_nome = tk.Entry(root, font=font_style)
entry_novo_nome.pack()

btn_editar = tk.Button(root, text="Editar Contato", command=editar, font=font_style, bg="#FF9800", fg="white")
btn_editar.pack()

btn_listar = tk.Button(root, text="Listar Contatos", command=mostrar_contatos, font=font_style, bg="#2196F3", fg="white")
btn_listar.pack()

contatos_texto = scrolledtext.ScrolledText(root, height=6, font=font_style)
contatos_texto.pack()

# Editor de mensagem
label_mensagem = tk.Label(root, text="Mensagem (use {nome} para personalizar):", font=font_style, bg="#f0f0f0")
label_mensagem.pack()

mensagem_texto = scrolledtext.ScrolledText(root, height=10, font=font_style)
mensagem_texto.pack()

mensagem_texto.insert(tk.END, carregar_mensagem())

btn_salvar_mensagem = tk.Button(root, text="Salvar Mensagem", command=salvar_mensagem_edicao, font=font_style, bg="#FFC107", fg="black")
btn_salvar_mensagem.pack()

btn_enviar = tk.Button(root, text="Enviar Mensagens", command=enviar, font=font_style, bg="#F44336", fg="white")
btn_enviar.pack()

root.mainloop()