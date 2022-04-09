import re
texto = """
ONLINE 192.168.1.1 active
OFFLINE 192.168.1.2 inactive
ONLINE 192.168.1.3 active
OFFLINE 192.168.1.4 inactive
"""
# Pega todos os ip e seu status
print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+(\w+)', texto))
# Pega todos os ip mas já filtrando - Positive lookahead
print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+(?=active)', texto))
# Pega todos os ip mas já filtrando - Negative lookahead
print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+(?!active)', texto))
# Pega as linhas que contem inactive - positive lookahead
print(re.findall(r'(?=.*inactive).+', texto))
# Pega as linhas que contem inactive - negative lookahead
print(re.findall(r'(?=.*[^in]active).+', texto))
# Pega as linhas que tem o online no \w+ - Positive lookbehind
print(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+(\w+)', texto))
