import os

def show_help():
    print("\nINSTRUÇÕES DO SISTEMA DE NOTAS:")
    print("1. Digite seu nome para começar.")
    print("2. Insira suas duas notas quando solicitado.")
    print("3. Veja a média das notas.")
    print("4. Digite 'X' para sair do sistema.")

def mensagem_final():
    terminal_width = os.get_terminal_size().columns
    mensagem_final = "OBRIGADO POR UTILIZAR NOSSO SISTEMA!"
    asterisks = "*" * len(mensagem_final)

    print(asterisks.center(terminal_width))
    print(mensagem_final.center(terminal_width))
    print(asterisks.center(terminal_width))

os.system('cls')


title = "SISTEMA DE NOTAS"
asterisks = "*" * len(title)

terminal_width = os.get_terminal_size().columns
print(asterisks.center(terminal_width))
print(title.center(terminal_width))
print(asterisks.center(terminal_width))

show_help()

nota1 = nota2= 0

while True:
    nomeAluno = input('\nDigite o nome do aluno ou pressione X para sair: ')
    if(nomeAluno == 'X' or nomeAluno == 'x'):
        os.system('cls')
        mensagem_final()
        break

    else:
        print(F'\nAluno {nomeAluno}')
        nota1 = float(input('\nInforme a primeira nota: '))
        nota2 = float(input('\nInforme a segunda nota: '))

        médiaNota = (nota1 + nota2)/2
        print(F'\nA média do aluno {nomeAluno} é {médiaNota:.2f}.')  
