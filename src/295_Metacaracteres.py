import re

texto = """Este Joao é um teste teste de string, todos os testes devem ser feitos com re, 
pois é mais rápido, e mais seguro, e mais flexível, joao e mais eficiente, este e mais seguro, sempre que for fazer"""

# O . serve para reconhecer qualquer caractere
print(re.findall('rápido|flexível|se...', texto))
print(re.findall('[Jj]oao', texto))
print(re.findall('[a-zA-Z]oao', texto))
# Flas para auxiliar na busca
print(re.findall('jOaO', texto, flags=re.IGNORECASE))
