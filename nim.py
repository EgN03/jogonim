def computador_escolhe_jogada(n,m):
    venceJoga = n%(m+1)
    if n == m or venceJoga >= m:
        compJoga = m
    compJoga = venceJoga
    
    return compJoga
    
def usuario_escolhe_jogada(n,m):
    usuJoga = int(input('\nQuantas peças você vai tirar?\n'))
    while usuJoga > m or usuJoga <1:
        print('\nOops! Jogada inválida! Tente de novo.\n')
        usuJoga = int(input('\nQuantas peças você vai tirar?'))
        
    return usuJoga


def partida():
    n = int(input('Quantas peças?'))
    m = int(input('Limite de peças por jogada?'))
    computadorJoga = False
    if n%(m+1)==0:
        print('\nVocê começa!')
    else:
        print('\nComputador começa!')
        computadorJoga = True
    while n > 0:
        if computadorJoga:
            compJoga = computador_escolhe_jogada(n,m)#Armazena a função dentro uma variável para facilitar o uso.
            n -= compJoga
            if compJoga == 1:
                print('\nO computador tirou uma peça.')
            else:
                print('\nO computador tirou', compJoga,'peças.')
            computadorJoga = False
        else:
            usuJoga = usuario_escolhe_jogada(n,m)
            n -= usuJoga
            if usuJoga == 1:
                print('\nVocê tirou uma peça.')
            else:
                print('\n Você tirou,',usuJoga, 'peças.')
            computadorJoga = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.\n')
        else:
            if n !=0:
                print('Agora restam',n,'peças no tabuleiro.\n')
    print('Fim do jogo! O computador ganhou!')
            

def campeonato():
    nRodada = 1
    voce = 0
    comp = 0
    while nRodada <= 3:
        print('\n **** Rodada',nRodada,'****\n')
        partida()
        nRodada += 1
        comp += 1
    print('\n**** Final do Campeonato ****\n')
    print('Placar: Você',voce, 'X', comp,'Computador')
    

def main():
     print('Bem-vindo ao jogo do NIM! Escolha:\n')
     tipo = int(input('''1 - Para jogar uma partida isolada
2 - Para jogar um campeonato '''))
     while tipo != 1 and tipo !=2: #Se o usuário colocar qualquer número que não seja 1 ou 2, entra no 'while', até ele colocar 1 ou 2 que são as opções.
         k = int(input('''1 - Para jogar uma partida isolada
2 - Para jogar um campeonato '''))
     if tipo == 1:
         print('\nVocê escolheu uma partida isolada\n')
         partida()
     else:
         print('\nVocê escolheu um campeonato!\n')
         campeonato()
         
main()

