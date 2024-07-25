from tkinter import Tk, ttk, Label, Button


def fui_clicado():
    print("fui clicado")
    botao.config(text="Fui Clicado")
    # botao.pack()


janela = Tk()
estilo = ttk.Style()

texto = Label(
    text="Olá Everson Mayer",
    font=("Helvetica", 44)
)
texto.pack()

botao = Button(
    text="Clica em mim",
    font=("Helvetica", 24),
    command=fui_clicado
)
botao.pack()

b2 = ttk.Button(text="botão TTK")
b2.pack()

janela.mainloop()
