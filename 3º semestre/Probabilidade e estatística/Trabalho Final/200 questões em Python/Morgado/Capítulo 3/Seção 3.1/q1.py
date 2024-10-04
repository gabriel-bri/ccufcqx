def divisores(inicio, fim, divisores_list):
  contagem = {
      "pelo_menos_tres": 0,
      "nenhum": 0,
      "exatamente_um": 0,
      "pelo_menos_um": 0
  }

  for num in range(inicio, fim + 1):
      divisores_do_num = [divisor for divisor in divisores_list if num % divisor == 0]
      if len(divisores_do_num) >= 3:
          contagem["pelo_menos_tres"] += 1
      elif len(divisores_do_num) == 0:
          contagem["nenhum"] += 1
      elif len(divisores_do_num) == 1:
          contagem["exatamente_um"] += 1
      else:
          contagem["pelo_menos_um"] += 1

  return contagem

divisores_lista = [2, 3, 7, 10]

resultado = divisores(1, 1000, divisores_lista)
print("Quantidade de números:")
for chave, valor in resultado.items():
    print(f"- {chave}: {valor}")