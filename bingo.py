import random
import time

print('Feito por João Gabriel')

def gerar_cartela(modo, jogador):
    if modo == 'rápido':

        linhas, colunas, max_num = 2, 3, 30
    else:
        linhas, colunas, max_num = 3, 4, 40
    
    cartela = []
    for col in range(colunas):
        intervalo = range(col * 10 + 1, (col + 1) * 10 + 1)
        coluna = random.sample(intervalo, linhas)
        cartela.append(coluna)
    
    return {
        'jogador': jogador,
        'cartela': [list(row) for row in zip(*cartela)],
        'marcacoes': [[False] * colunas for _ in range(linhas)]
    }

def exibir_cartela(cartela):
    print(f"Cartela de {cartela['jogador']}:")
    for i, linha in enumerate(cartela['cartela']):
        print(' '.join(f"[{num}]" if cartela['marcacoes'][i][j] else f" {num} " for j, num in enumerate(linha)))
    print()

def verificar_vitoria(cartela):
    return all(all(marcado for marcado in linha) for linha in cartela['marcacoes'])

def sortear_dezena(sorteadas, max_num):
    while True:
        dezena = random.randint(1, max_num)
        if dezena not in sorteadas:
            return dezena

def marcar_cartela(cartela, dezena):
    for i, linha in enumerate(cartela['cartela']):
        for j, num in enumerate(linha):
            if num == dezena:
                cartela['marcacoes'][i][j] = True

def jogar_bingo():
    print("Bem-vindo ao Simulador de Bingo!")
    modo = input("Escolha o modo de jogo ('rápido' ou 'demorado'): ").strip().lower()
    while modo not in ('rápido', 'demorado'):
        modo = input("Opção inválida. Escolha 'rápido' ou 'demorado': ").strip().lower()
    
    jogadores = ['Jogador 1', 'Jogador 2'] if modo == 'rápido' else ['Jogador 1', 'Jogador 2', 'Jogador 3', 'Jogador 4']
    cartelas = [gerar_cartela(modo, jogador) for jogador in jogadores]
    
    max_num = 30 if modo == 'rápido' else 40
    sorteadas = []
    ganhadores = []
    
    while not ganhadores:
        time.sleep(1)
        dezena = sortear_dezena(sorteadas, max_num)
        sorteadas.append(dezena)
        sorteadas.sort()
        
        print(f"\nDezena sorteada: {dezena}")
        print(f"Dezenas sorteadas até agora: {sorteadas}")
        
        for cartela in cartelas:
            marcar_cartela(cartela, dezena)
            exibir_cartela(cartela)
            
            if verificar_vitoria(cartela) and cartela['jogador'] not in ganhadores:
                ganhadores.append(cartela['jogador'])
    
    print(f"\nBingo! Os ganhadores são: {', '.join(ganhadores)}")

if __name__ == "__main__":
    jogar_bingo()
