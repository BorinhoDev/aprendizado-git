nomes = []
idade = []

for i in range(2):
    name = str(input("Digite o nome do aluno: "))
    nomes.append(name)
    age = int(input("Digite a idade do aluno: "))
    idade.append(age)

for name in nomes:
    print(f"O aluno {name} tem {age} anos.")