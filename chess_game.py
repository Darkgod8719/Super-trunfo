import random

# Cartas exemplo
cartas = [
    {"nome": "Dragão", "força": 9, "velocidade": 5, "magia": 7},
    {"nome": "Golem", "força": 8, "velocidade": 3, "magia": 2},
    {"nome": "Elfo", "força": 5, "velocidade": 9, "magia": 6},
    {"nome": "Mago", "força": 4, "velocidade": 6, "magia": 10},
    {"nome": "Cavaleiro", "força": 7, "velocidade": 6, "magia": 4}
]

def escolher_carta():
    return random.choice(cartas)

def mostrar_carta(carta):
    print(f"\nCarta: {carta['nome']}")
    for chave, valor in carta.items():
        if chave != "nome":
            print(f"{chave.capitalize()}: {valor}")

def jogar():
    print("🎴 Bem-vindo ao Super Trunfo!")

    carta_jogador = escolher_carta()
    carta_cpu = escolher_carta()
    
    print("\nSua carta é:")
    mostrar_carta(carta_jogador)

    atributo = input("\nEscolha um atributo (força, velocidade, magia): ").lower()

    if atributo not in carta_jogador:
        print("❌ Atributo inválido. Fim de jogo.")
        return

    print("\nCarta da CPU:")
    mostrar_carta(carta_cpu)

    valor_jogador = carta_jogador[atributo]
    valor_cpu = carta_cpu[atributo]

    print(f"\nVocê: {valor_jogador} x CPU: {valor_cpu}")

    if valor_jogador > valor_cpu:
        print("✅ Você venceu!")
    elif valor_jogador < valor_cpu:
        print("❌ Você perdeu!")
    else:
        print("⚖️ Empate!")

if __name__ == "__main__":
    jogar()
