# Feita por Adriano Carvalho e Luiz Gabriel Lima

print("\nCalculadora de Reajuste Salarial")
print("~"*50)

# função para o reajuste salarial
def calc():
    print("Porcentagens de reajuste disponíveis:\n1 - 3,43%\n2 - 2,07%\n3 - 6,58%\n4 - 11,28%")
    print("~"*50)
    rej = float(input("Escolha o reajuste que você deseja aplicar: "))
    print("~"*50)
    sal = float(input("Digite o valor de seu salário: "))
    print("~"*50)

# condicional para calcular o salário com reajuste escolhido pelo usuário
    if rej == 1:
        print("Reajuste de número 1 foi escolhido.\n")
        print("Salário reajustado: R$", sal * 0.0343 + sal)
        print("~"*50)

    elif rej == 2:
        print("Reajuste de número 2 foi escolhido.\n")
        print("Salário reajustado: R$", sal * 0.0207 + sal)
        print("~"*50)

    elif rej == 3:
        print("Reajuste de número 3 foi escolhido.\n")
        print("Salário reajustado: R$", sal * 0.0658 + sal)
        print("~"*50)
    
    elif rej == 4:
        print("Reajuste de número 4 foi escolhido.\n")
        print("Salário reajustado: R$", sal * 0.1128 + sal)
        print("~"*50)

# finalizar ou reiniciar o pragrama, caso o usuário deseje
    else:
        print("Não existe essa opção de reajuste, escolha outra vez")
        print("~"*50)
 
    restart = input("Gostaria de tentar novamente? [S/N] ")
    if restart == "S" or restart == "s":
        calc()
    if restart == "N" or restart == "n":
        print("Certo. Até logo!")
calc()
