import tkinter as tk
from tkinter import ttk, messagebox

def calcular(operacao):
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())

        if operacao == "soma":
            resultado.set(num1 + num2)
        elif operacao == "subtracao":
            resultado.set(num1 - num2)
        elif operacao == "multiplicacao":
            resultado.set(num1 * num2)
        elif operacao == "divisao":
            if num2 == 0:
                messagebox.showerror("Erro", "Divisão por zero não permitida!")
                return
            resultado.set(num1 / num2)
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos!")


root = tk.Tk()
root.title("Calculadora Bonita")
root.geometry("300x350")
root.configure(bg="#2c3e50")  


style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10, background="#3498db")

ttk.Label(root, text="Número 1:", background="#2c3e50", foreground="white", font=("Arial", 12)).grid(row=0, column=0, pady=10)
entrada1 = ttk.Entry(root, font=("Arial", 12))
entrada1.grid(row=0, column=1, pady=10)

ttk.Label(root, text="Número 2:", background="#2c3e50", foreground="white", font=("Arial", 12)).grid(row=1, column=0, pady=10)
entrada2 = ttk.Entry(root, font=("Arial", 12))
entrada2.grid(row=1, column=1, pady=10)

resultado = tk.DoubleVar()
ttk.Label(root, text="Resultado:", background="#2c3e50", foreground="white", font=("Arial", 12)).grid(row=2, column=0, pady=10)
ttk.Entry(root, textvariable=resultado, font=("Arial", 12), state="readonly").grid(row=2, column=1, pady=10)


frame_botoes = ttk.Frame(root)
frame_botoes.grid(row=3, column=0, columnspan=2, pady=20)


def criar_botao(texto, operacao, linha, coluna, cor):
    botao = ttk.Button(frame_botoes, text=texto, command=lambda: calcular(operacao), style="Botao.TButton")
    botao.grid(row=linha, column=coluna, padx=5, pady=5, ipadx=10, ipady=5)
    style.configure("Botao.TButton", font=("Arial", 14), padding=10, background=cor)

criar_botao("+", "soma", 0, 0, "#27ae60")
criar_botao("-", "subtracao", 0, 1, "#e74c3c")
criar_botao("*", "multiplicacao", 1, 0, "#f39c12")
criar_botao("/", "divisao", 1, 1, "#9b59b6")

root.mainloop()
