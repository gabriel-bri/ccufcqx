def avaliar_teste(valor_p, nivel_significancia=0.05):
    conclusao = 'Rejeitar H0' if valor_p < nivel_significancia else 'Aceitar H0'
    risco_erro = valor_p if valor_p < nivel_significancia else 'Não aplicável'
    
    return {
        'Conclusao': conclusao,
        'Risco de erro': risco_erro
    }

# a) Valor p = 0,0001
resultado_a = avaliar_teste(0.0001)
print("a) Resultados para valor p = 0,0001:")
print(f"Conclusão: {resultado_a['Conclusao']}")
print(f"Risco de erro: {resultado_a['Risco de erro']}")

# b) Valor p = 0,25
resultado_b = avaliar_teste(0.25)
print("\nb) Resultados para valor p = 0,25:")
print(f"Conclusão: {resultado_b['Conclusao']}")
print(f"Risco de erro: {resultado_b['Risco de erro']}")

# c) Comparar os valores p
p_1 = 0.0001
p_2 = 0.01

if p_1 < p_2:
    conclusao_c = f"Maior convicção no teste com p = {p_1}"
else:
    conclusao_c = f"Maior convicção no teste com p = {p_2}"

print(f"\nc) {conclusao_c}")