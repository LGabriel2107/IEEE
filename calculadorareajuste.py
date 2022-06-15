print("\nCalculadora de Reajuste Salarial")
print("~"*50)

def calc():
    print("Porcentagens de reajuste disponíveis:\n1 - 3,43%\n2 - 2,07%\n3 - 6,58%")
    print("~"*50)
    rej = int(input("Escolha o reajuste que você deseja aplicar: "))
    print("~"*50)
    sal = int(input("Digite o valor de seu salário: "))
    print("~"*50)

    if rej == 1:
        print("Reajuste de número 1 foi escolhido.\n")
        print("Salário reajustado: R$", sal * 343/10000 + sal)
        print("~"*50)

    elif rej == 2:
        print("Reajuste de número 2 foi escolhido.\n")
        print("Salário reajustado: R$", sal * 207/10000 + sal)
        print("~"*50)

    elif rej == 3:
        print("Reajuste de número 3 foi escolhido.\n")
        print("Salário reajustado: R$", sal * 658/10000 + sal)
        print("~"*50)

    else:
        print("Não existe essa opção de reajuste, escolha outra vez")
        print("~"*50)
 
    restart = input("Gostaria de tentar novamente? [S/N] ")
    if restart == "S" or restart == "s":
        calc()
    if restart == "N" or restart == "n":
        print("Certo. Até logo!")
calc()