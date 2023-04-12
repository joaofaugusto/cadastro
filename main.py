import tkinter as tk
import ttkbootstrap as ttk

def entrar():
    login = entry_int.get()
    login_senha = entry_senha.get()
    if login == 123 and login_senha == 'teste':
        saida_string.set('Login Efetuado com sucesso')



window = ttk.Window(themename='minty')

window.title('Teste')
titulo_label = ttk.Label(
    master= window,
    text= 'Cadastro',
    font= 'Calibri 24 bold'
)

input_frame = ttk.Frame(
    master = window
)

entry_int = tk.IntVar()
entry_string = tk.StringVar()
entry_email = ttk.Entry(
    master = window,
    textvariable=  entry_int 
)
entry_senha = ttk.Entry(
    master = window,
    textvariable= entry_string
)

button_login = ttk.Button(
    master = window,
    text= 'Entrar',
    command= entrar
)
titulo_label.pack(side=tk.TOP)
entry_email.pack(side=tk.TOP)
entry_senha.pack(side=tk.TOP)
button_login.pack(side=tk.TOP)
input_frame.pack(pady= 10)
saida_string = tk.StringVar()
saida_label = ttk.Label(
    master = window,
    text='Saida',
    font = 'Calibri 12 bold',
    textvariable=saida_string
)

saida_label.pack()

window.mainloop()