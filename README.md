# Contador de Cliques com Tkinter

O contador de cliques serve seu propósito de demonstrar o uso da biblioteca Tkinter para uma aplicação desktop usando eventos de interface e componentes básicos de GUI.

# Descrição

Incremente um contador ao pressionar um botão ou utilizar atalhos no teclado.

A aplicação possui:

* Interface gráfica simples
* Menu superior
* Barra de status
* Confirmações por caixas de diálogo
* Atalhos de teclado
* Feedback visual ao clicar no botão

# Funcionalidades

### Contador de cliques

* Cada clique no botão **"Clique aqui"** incrementa o contador.
* O valor é exibido em destaque no centro da janela.

### Reset do contador

* O botão **Resetar** ou a opção no menu zera o contador.
* Uma janela de confirmação aparece antes da ação.

### Feedback visual

* Ao clicar no botão principal, ele **pisca em outra cor**, indicando que a ação foi registrada.

### Barra de status

* Na parte inferior da janela existe uma **barra de status** que mostra o número atual de cliques.

### Menu da aplicação

A aplicação possui um menu com duas seções:

**Arquivo**

* Resetar contador
* Sair da aplicação

**Ajuda**

* Informações sobre o programa

### Atalhos de teclado

| Tecla   | Ação                  |
| ------- | --------------------- |
| `Space` | Incrementa o contador |
| `R`     | Reseta o contador     |
| `Esc`   | Fecha a aplicação     |

# Tecnologias Utilizadas

* **Python 3**
* **Tkinter**

# Como Executar

### Clonar ou baixar o projeto

```bash
git clone https://github.com/seu-usuario/click-counter.git
```

ou simplesmente baixar os arquivos.

### Executar o programa

```bash
python main.py
```

A janela do contador será aberta automaticamente.

ou simplesmente executar "Contador_de_Cliques.exe" dentro da pasta dist.

# Conceitos Demonstrados

* Interfaces gráficas com Tkinter
* Programação Orientada a Objetos (POO)
* Uso de variáveis reativas (`IntVar`, `StringVar`)
* Manipulação de eventos
* Atalhos de teclado
* Menus em aplicações desktop
* Caixas de diálogo (`messagebox`)
* Atualização dinâmica da interface
