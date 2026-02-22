import tkinter as tk
from comandos import interpretar_comando # type: ignore

# Criar janela
janela = tk.Tk()
janela.title("Assistente IA")
janela.geometry("700x400")
janela.resizable(False, False)

# Carregar imagem
fundo_img = tk.PhotoImage(file="fundo.png")

# Label com imagem
label_fundo = tk.Label(janela, image=fundo_img)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

# Caixa de texto
entrada = tk.Entry(janela, font=("Arial", 14))
entrada.place(x=120, y=300, width=360)

# Função do botão
def executar():
    comando = entrada.get()
    interpretar_comando(comando)
    entrada.delete(0, tk.END)

# Botão
botao = tk.Button(janela, text="Executar", command=executar)
botao.place(x=260, y=340)

# Iniciar app
janela.mainloop()