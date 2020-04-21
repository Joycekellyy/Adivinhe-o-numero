from random import randint
computador = randint(1, 50)
n = 1
print('\033[1;35mEstou pensando em um número entre 1 e 50')
print('\033[1;35mVocê escolhe seu número de tentativas :)')
tent = int(input('Seu número de tentativas: '))
if tent >= 10:
    print('\033[1;31mSão muitas tentativas, não aceitamos isso aqui.')
else:
    print(f'\033[1;32mVOCÊ TEM \033[1;31m{tent}\033[1;32m TENTATIVAS, BOA SORTE!')
    while n != computador and tent != 0:
        n = int(input(f'\033[1;32mDigite seu palpite: \033[m'))
        tent += -1
        if tent == 0:
            print('\033[1;31mVocê esgotou suas tentativas, tente novamente.\033[m')
        else:
            if n > computador:
                print(f'\033[1;31mMuito alto!\033[m\nSuas tentativas: \033[1;33m{tent}\033[m')
            elif n < computador:
                print(f'\033[1;31mMuito baixo!\033[m\nSuas tentativas: \033[1;33m{tent}\033[m')
            else:
                print('\033[1;32mParabéns! você acertou o número no qual eu pensava!')