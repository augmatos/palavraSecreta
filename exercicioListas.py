print('O objetivo desse jogo é descobrir qual a palavra secreta, digite uma letra por vez e boa sorte.')

palavra = 'microcomputador'
digitadas = []
chances = (len(palavra)) // 2

while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')
    print()

    if len(letra) > 1:
        print('Você digitou mais de uma letra.')
        print()
        continue

    digitadas.append(letra)

    if letra in palavra:
        print(f'Parabens, a letra "{letra}" existe na palavra secreta.')
        print()
    else:
        print(f'A letra {letra} nao existe na palavra secreta.')
        print()
        chances -= 1
        print(f'Voce ainda tem {chances} chances.')
        print()
        digitadas.pop()

    secreta_temp = ''
    for letra_secreta in palavra:
        if letra_secreta in digitadas:
            secreta_temp += letra_secreta
        else:
            secreta_temp += '*'

    if secreta_temp == palavra:
        print(f'Parabens, voce acertou. A palavra secreta era "{palavra}" ')
        break
    else:
        print(secreta_temp)
        print('-----------------------------------------------------------------')
