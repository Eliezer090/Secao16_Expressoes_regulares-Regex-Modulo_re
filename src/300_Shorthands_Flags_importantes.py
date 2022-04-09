import re
texto = """Este ja Joao é um teste teste de string, todos os testes devem ser feitos com re, 
pois é mais rápido, e mais seguro, e mais flexível, joao e mais eficiente, este e mais seguro, 
sempre que for fazer joooooooooooooaooooooo, e mais    seguro, 123 8545  sempre que for fazer"""

# Pega todas as palavras
print(re.findall('\w+', texto))
# \W+ maiuscula é o inverso do \w
print(re.findall('\W+', texto))

# Pegar todos os numeros
print(re.findall('\d+', texto))
# \D+ maiuscula é o inverso do \d
print(re.findall('\D+', texto))
# Pega espaço \r \n \t
print(re.findall('\s+', texto))
# \S+ maiuscula é o inverso do \s
print(re.findall('\S+', texto))
# Pega a palavra inteira que coma com e
print(re.findall(r'\be\w+', texto, flags=re.IGNORECASE))