import tkinter as tk
from tkinter import messagebox

# --- Lógica do Jogo ---
jogador_atual = "🐱"  # Gatinho inicial
tabuleiro = [["" for _ in range(3)] for _ in range(3)]

def verificar_vitoria(tab, jogador):
    for i in range(3):
        if all([celula == jogador for celula in tab[i]]):
            return True
    for i in range(3):
        if all([tab[j][i] == jogador for j in range(3)]):
            return True
    if all([tab[i][i] == jogador for i in range(3)]):
        return True
    if all([tab[i][2-i] == jogador for i in range(3)]):
        return True
    return False

def verificar_empate():
    for linha in tabuleiro:
        if "" in linha:
            return False
    return True

# --- Funções da Interface ---
def clique_botao(linha, coluna):
    global jogador_atual
    if tabuleiro[linha][coluna] == "":
        tabuleiro[linha][coluna] = jogador_atual
        botoes[linha][coluna]["text"] = jogador_atual
        
        if verificar_vitoria(tabuleiro, jogador_atual):
            messagebox.showinfo("Fim de Jogo", f"Parabéns! {jogador_atual} venceu!")
            desabilitar_botoes()
            return
        
        if verificar_empate():
            messagebox.showinfo("Fim de Jogo", "Empate!")
            return

        jogador_atual = "😺" if jogador_atual == "🐱" else "🐱"
        rotulo_status["text"] = f"Vez do jogador: {jogador_atual}"

def reiniciar_jogo():
    global jogador_atual
    jogador_atual = "🐱"
    rotulo_status["text"] = f"Vez do jogador: {jogador_atual}"
    for i in range(3):
        for j in range(3):
            tabuleiro[i][j] = ""
            botoes[i][j]["text"] = ""
            botoes[i][j]["state"] = "normal"

def desabilitar_botoes():
    for i in range(3):
        for j in range(3):
            botoes[i][j]["state"] = "disabled"

# --- Configuração da Janela ---
janela = tk.Tk()
janela.title("Jogo da Velha dos Gatinhos")
janela.configure(bg="#FFF9C4")  # Amarelo bebê

rotulo_status = tk.Label(janela, text=f"Vez do jogador: {jogador_atual}", font=("Arial", 16), bg="#FFF9C4")
rotulo_status.grid(row=0, column=0, columnspan=3, pady=10)

botoes = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        botao = tk.Button(janela, text="", font=("Arial", 30), width=5, height=2,
                          command=lambda i=i, j=j: clique_botao(i, j), bg="#FFFDE7")
        botao.grid(row=i+1, column=j, padx=5, pady=5)
        botoes[i][j] = botao

botao_reiniciar = tk.Button(janela, text="Reiniciar Jogo", font=("Arial", 12), command=reiniciar_jogo, bg="#FFF176")
botao_reiniciar.grid(row=4, column=0, columnspan=3, pady=10)

janela.mainloop()
