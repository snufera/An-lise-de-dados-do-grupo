print("""\nBem-vindo!
Esse programa serve para analisar os dados de um grupo.
Informe a idade e o sexo do grupo!
\033[31mPOR FAVOR, INFORME UMA IDADE DE 0 A 130 ANOS!\033[m""")

c_man = c_woman = id_pessoa = c_idade = 0
while True:
    id_pessoa += 1
    idade = int(input(f"\nDigite a idade da {id_pessoa}º pessoa: "))
    if 0 <= idade <= 130:  # VALIDAR A IDADE
        if idade > 18:  # MAIORES DE 18 ANOS
            c_idade += 1
        while True:  # VALIDAR O SEXO
            sexo = str(input("Qual seu sexo? Masculino [M] ou Feminino [F]: ")).strip()
            if sexo in "MmFf":
                if sexo in "Mm":  # QUANTIDADE DE HOMENS
                    c_man += 1
                else:
                    if idade < 20:  # MULHER MENOR DE 20
                        c_woman += 1
                end = str(input("Quer continuar? [S] ou [N]: ")).strip()  # QUER CONTINUAR?
                break
            else:  # VALIDAR O SEXO
                print("\033[33mTecla inválida, utilize [M] para masculino e [F] para feminino!\033[m")
    else:  # VALIDAR A IDADE
        break
    if end in "Nn":
        break

#  FIM, DADOS E ERRO DO USUÁRIO
if idade < 0:
    print(f"\033[31mInforme uma idade válida entre 0 e 130 anos!\033[m")
elif idade > 130:
    print(f"\033[31mInforme uma idade válida entre 0 e 130 anos!\033[m")
else:
    print("=="*15)
    print(f"\033[34m{c_idade} pessoa(s) tem mais de 18 anos.")
    print(f"{c_man} homen(s) foi/foram cadastrados.")
    print(f"{c_woman} mulhere(s) com menos de 20 anos.\033[m")
