import re

string = 'Este é um teste teste de string'
print(re.search('teste', string))
print(re.findall('teste', string))
if re.search('teste', string):
    print('Encontrei o teste')
else:
    print('Não encontrei o teste')

print(re.sub('teste', 'AVS', string))
print(re.sub('teste', 'AVS', string, count=1))

# Se tiver varias interações com a string o melhor é fazer assim
regex = re.compile('teste')
print(regex.search(string))
