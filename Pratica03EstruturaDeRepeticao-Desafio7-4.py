numero_secreto = 7
palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Tente adivinhar o número secreto: "))

    if palpite > numero_secreto:
        print("Tente um número menor!")
    elif palpite < numero_secreto:
        print("Tente um número maior!")
    else:
        print("Parabéns! Você acertou o número secreto!")