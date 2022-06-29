''' 1) Constua um jogo da forca. '''

from ast import While

palavra = 'eletiva'
digitadas = []
chances = 3

print('JOGO DA FORCA - PYTHON (ELETIVA I)')

while True:
    letra = str(input("Digite uma letra: "))
    
    if len(letra) > 1:
        print('Apenas uma letra, por favor!')
        continue
    digitadas.append(letra)

    paralvra_temporaria = ''
    for letra_secreta in palavra:
        if letra_secreta in digitadas:
            paralvra_temporaria += letra_secreta
        else:
            paralvra_temporaria += '*'
    if paralvra_temporaria == palavra:
        print('Parabéns, você ganhou!')
        break
    else:
        print('Quase lá: ' + paralvra_temporaria)
    if letra not in palavra:
        chances -= 1
    if chances <= 0:
        print('Você perdeu!')
        break
    print('Chances restantes: ' + str(chances))
print()