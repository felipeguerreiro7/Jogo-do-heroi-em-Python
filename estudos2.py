#Perguntar o nome do herói e começar a jornada
heroi = input("Qual o nome do heroi? ")
print(f"muito bem %s! Vamos começar, você está na frente de uma caverna, o que você escolhe? " %heroi)
print(1,"- Entrar")
print(2,"- fugir")
escolha_1 = int(input("Digite sua escolha: "))

#caminho 1 
if escolha_1 == 1:
    print("Você entrou na caverna e viu um monstro dormindo! O que vai fazer?")
    print("1 - Lutar")
    print("2 - Passar sorrateiramente")
    escolha_na_caverna = input("Qual a sua escolha? ")

    if escolha_na_caverna == 1:
        print("Você derrotou o monstro!")
    else:
        print("O monstro acordou e... te devorou!")
        print("Fim da jornada, {heroi}")
else:
    print("Covarde!")
    