# Número de funcionários em cada empresa
funcionarios = {
    "A": 20,
    "B": 15,
    "C": 7,
    "D": 5,
    "E": 3
}

# Total de funcionários
total_funcionarios = sum(funcionarios.values())

# Probabilidade de cada empresa ser selecionada
probabilidades = {empresa: num_func / total_funcionarios for empresa, num_func in funcionarios.items()}

# Probabilidade de a Empresa A não ser selecionada
probabilidade_a_nao_selecionada = 1 - probabilidades["A"]

# Resultados
print("Probabilidade de cada empresa ser selecionada:")
for empresa, probabilidade in probabilidades.items():
    print(f"{empresa}: {probabilidade:.2f}")

print(f"\nProbabilidade de a Empresa A não ser selecionada: {probabilidade_a_nao_selecionada:.2f}")
