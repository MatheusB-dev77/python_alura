import os
def exibir_nome_do_programa():

    print ('🆂🅰🅱🅾🆁 🅴🆇🅿🆁🅴🆂🆂\n')

def exibir_opcoes():

    print('1.cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def finalizando_app():
    os.system('cls')
    print('Finaliznado o app')

def opcao_invalida():
    print('Opção invalida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()



def escolher_opcao():
    opcao_escolhida= int(input('Escolha uma Opção: '))

# opcao_escolhida = int(opcao_escolhida)

    if opcao_escolhida == 1:
        print ('cadastrar restaurantes')
    elif opcao_escolhida == 2:
        print('Listar restaurante') 
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    elif opcao_escolhida == 4:
        finalizando_app()

    else:
        opcao_invalida()


def main ():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__== '__main__':
    main()