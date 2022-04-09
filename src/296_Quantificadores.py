"""
    * 0 ou N vezes
    + 1 ou mais vezes
    ? 0 ou 1 vezes
    {n} exatamente n vezes
    {n,} pelo menos n vezes
    {n,m} entre n e m vezes    
"""

import re

texto = """Este ja Joao é um teste teste de string, todos os testes devem ser feitos com re, 
pois é mais rápido, e mais seguro, e mais flexível, joao e mais eficiente, este e mais seguro, 
sempre que for fazer joooooooooooooaooooooo, e mais seguro,  sempre que for fazer"""

print(re.findall('jo+ao', texto, flags=re.IGNORECASE))
print(re.findall('jo+ao+', texto, flags=re.IGNORECASE))
print(re.sub('jo+ao+', 'Felipe', texto, flags=re.IGNORECASE))
print('')
# O ja neste caso vai ser pego tambem, pois é 0 ou n
print(re.sub('jo*ao*', 'Felipe', texto, flags=re.IGNORECASE))
print('\n')
print(re.sub('jo?ao', 'Felipe', texto, flags=re.IGNORECASE))
print('\n')
print(re.sub('jo{1,}ao{1,}', 'Felipe', texto, flags=re.IGNORECASE))
