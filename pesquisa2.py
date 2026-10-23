print("Pesquisa de Atendimento - TudoWeb")

excelente = 0
ruim = 0

for i in range(10):
    print("\nEntrevistado", i + 1)

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    opiniao = int(input("Opinião (1-Excelente / 2-Bom / 3-Ruim): "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1

print("\n--- RESULTADO DA PESQUISA ---")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)