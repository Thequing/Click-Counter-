import tkinter as tk
from tkinter import messagebox

class ClickCounterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contador de Cliques")
        self.geometry("300x200")
        self.resizable(False, False)

        # Variáveis Tkinter
        self.contador = tk.IntVar(value=0)
        self.status_var = tk.StringVar()

        # Configurar menu
        self._setup_menu()

        # Configurar interface
        self._setup_ui()

        # Configurar atalhos
        self._setup_bindings()

        # Inicializar status
        self.atualizar_status()

    def _setup_menu(self):
        menu_bar = tk.Menu(self)

        menu_arquivo = tk.Menu(menu_bar, tearoff=0)
        menu_arquivo.add_command(label="Resetar", command=self.resetar)
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label="Sair", command=self.sair)

        menu_ajuda = tk.Menu(menu_bar, tearoff=0)
        menu_ajuda.add_command(label="Sobre", command=self.sobre)

        menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)
        menu_bar.add_cascade(label="Ajuda", menu=menu_ajuda)

        self.config(menu=menu_bar)

    def _setup_ui(self):
        # Corpo principal UI
        frame = tk.Frame(self, padx=20, pady=20)
        frame.pack(expand=True)

        # Contador
        self.label = tk.Label(
            frame,
            textvariable=self.contador,
            font=("Arial", 32)
        )
        self.label.pack(pady=10)

        # Botões
        self.btn_click = tk.Button(
            frame,
            text="Clique aqui",
            command=self.clicar,
            width=15
        )
        self.btn_click.pack(pady=5)

        self.btn_reset = tk.Button(
            frame,
            text="Resetar",
            command=self.resetar
        )
        self.btn_reset.pack()

        # Cliques feitos
        status = tk.Label(
            self,
            textvariable=self.status_var,
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        status.pack(side=tk.BOTTOM, fill=tk.X)

    def _setup_bindings(self):
        self.bind("<space>", lambda e: self.clicar())
        self.bind("<r>", lambda e: self.resetar())
        self.bind("<Escape>", lambda e: self.sair())

    def clicar(self):
        self.contador.set(self.contador.get() + 1)
        self.atualizar_status()
        self._flash_button()

    def resetar(self):
        if messagebox.askyesno("Resetar", "Quer zerar o contador?"):
            self.contador.set(0)
            self.atualizar_status()

    def sair(self):
        if messagebox.askokcancel("Sair", "Quer sair do programa?"):
            self.destroy()

    def atualizar_status(self):
        self.status_var.set(f"Cliques: {self.contador.get()}")

    def sobre(self):
        messagebox.showinfo(
            "Sobre",
            "Contador de Cliques\nDemonstração usando Tkinter"
        )

    def _flash_button(self):
        # Butão pisca de outra cor
        original_color = self.btn_click.cget("bg")
        self.btn_click.config(bg="lightblue")
        self.after(100, lambda: self.btn_click.config(bg=original_color))

if __name__ == "__main__":
    app = ClickCounterApp()
    app.mainloop()