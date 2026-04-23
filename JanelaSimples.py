import PySimpleGUI as sg

# 1. Definir o layout (elementos da janela)
layout = [
    [sg.Text("Olá, Mundo!")],
    [sg.Input(key='-INPUT-')],
    [sg.Button("Ok"), sg.Button("Sair")]
]

# 2. Criar a janela
window = sg.Window("Minha Primeira Tela", layout)

# 3. Loop de eventos para ler o que acontece
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Sair":
        break
    print(f"Você digitou: {values['-INPUT-']}")

# 4. Fechar a janela
window.close()
