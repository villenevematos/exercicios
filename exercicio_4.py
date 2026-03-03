# Exercício 4: Extração de Username para Log (Setor de Segurança)
#
# Para criar um log de acessos, o sistema precisa extrair apenas a parte do nome 
# do usuário de um e-mail corporativo (tudo o que vem antes do @). 
# Dado o e-mail beatriz.oliveira@grupocorp.com, use a função .find() e o 
# fatiamento de texto para extrair e exibir apenas o nome beatriz.oliveira.

email = "beatriz.oliveira@grupocorp.com"
indice_arroba = email.find("@")
username = email[:indice_arroba]
print(username)

# outra forma
indice_arroba = email.index("@")
username = email[:indice_arroba]
print(username)