# -*- coding: utf-8 -*-
"""
# Exercícios com Listas em Python
Resolva os exercícios abaixo **apenas nas células de código**. Não há gabarito incluído neste notebook.

## Exercício 1 — Dashboard de Vendas (Análise de Dados)

Você recebeu uma lista com as vendas diárias de uma equipe:

vendas = [1500, 2000, 800, 3500, 1200]

Crie um programa que exiba um pequeno relatório contendo:

1. O total de vendas na semana
2. A média de vendas diária
3. O valor da melhor venda e da pior venda do período
"""

# Escreva sua solução aqui
vendas = [1500, 2000, 800, 3500, 1200]
total_vendas = sum(vendas)
maior_venda = max(vendas)
menor_venda = min(vendas)
media_vendas = total_vendas / len(vendas)
print(f"O total de vendas na semana foi de {total_vendas}")
print(f"A média de vendas diária foi de {media_vendas}")
print(f"A maior venda do período foi de {maior_venda}")
print(f"A menor venda do período foi de {menor_venda}")

"""## Exercício 2 — Gestão de Estoque (Edição e Verificação)

Uma loja de eletrônicos possui os seguintes produtos:

estoque = ["monitor", "teclado", "mouse", "headset"]

Faça o seguinte:

1. Adicione o item "webcam" ao final da lista
2. Atualize "teclado" para "teclado mecanico"
3. Verifique se "impressora" está no estoque (exibir True ou False)
4. Remova "mouse" da lista

"""

# Escreva sua solução aqui
estoque = ["monitor", "teclado", "mouse", "headset"]
estoque.append("webcam")
indice_teclado = estoque.index("teclado")
estoque[indice_teclado] = "teclado mecanico"
print("impressora" in estoque)
estoque.remove("mouse")
print(estoque)

"""## Exercício 3 — Organização de Preços (Ordenação e Slicing)

Uma importadora listou os preços de frete em dólar:

fretes = [50, 80, 20, 150, 40]

Faça:

1. Ordene a lista do maior para o menor preço
2. Pegue os 2 fretes mais caros usando slicing e salve em `top_fretes`
3. Exiba a lista ordenada e a lista `top_fretes`

"""

fretes = [50, 80, 20, 150, 40]

# Ordene a lista do maior para o menor preço
ordem_decrescente = sorted(fretes, reverse=True)

# Pegue os 2 fretes mais caros usando slicing e salve em top_fretes
top_fretes = ordem_decrescente[:2]

# Exiba a lista ordenada e a lista top_fretes
print(ordem_decrescente, top_fretes, sep="\n")

"""## Exercício 4 — Sistema de Logística (Busca e Extensão)

A empresa tem a rota:

rota = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"]

Novas cidades:

novas_cidades = ["Itu", "Valinhos"]

Faça:

1. Una as duas listas usando `extend`
2. Descubra o índice da cidade "Sorocaba"
3. Exiba a lista completa
4. Mostre a mensagem: "Sorocaba é a Xª cidade da rota"

"""

# Escreva sua solução aqui
rota = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"]
novas_cidades = ["Itu", "Valinhos"]
rota.extend(novas_cidades)
indice_sorocaba = rota.index("Sorocaba") + 1
print(f"Sorocaba é {indice_sorocaba}ª cidade da rota")

"""## Exercício 5 — Atualização de Preços Interativa

Listas:

precos = [100.0, 250.0, 500.0]  
vinhos = ["Branco", "Tinto", "Champagne"]

Crie um programa que:

1. Peça ao usuário o nome do produto
2. Peça o novo preço
3. Atualize o preço correto na lista
4. Mostre as listas completas de vinhos e preços

"""

# Escreva sua solução aqui
precos = [100.0, 250.0, 500.0]
vinhos = ["Branco", "Tinto", "Champagne"]
while True:
  novo_produto = input("Digite o nome do produto: ")
  if novo_produto == "":
    break
  preco = float(input("Digite o novo preço: "))
  vinhos.append(novo_produto)
  precos.append(preco)
print(vinhos, precos)