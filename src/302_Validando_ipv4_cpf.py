import re

cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
cpf = '123.456.789-10'
# print(cpf_reg_exp.search(cpf))
# Melor maneira  e mais precisa todo ip pode ir de 0.0.0.0 até 255.255.255.255
ip_reg_exp = re.compile(r'''
    ^
    (?:
    25[0-5]| #250-255
    2[0-4][0-9]| #200-249
    1[0-9]{2}| #100-199
    [1-9][0-9]| #10-99
    [0-9]#0-9
    )\.
    (?:
    25[0-5]| #250-255
    2[0-4][0-9]| #200-249
    1[0-9]{2}| #100-199
    [1-9][0-9]| #10-99
    [0-9]#0-9
    )\.
    (?:
    25[0-5]| #250-255
    2[0-4][0-9]| #200-249
    1[0-9]{2}| #100-199
    [1-9][0-9]| #10-99
    [0-9]#0-9
    )\.
    (?:
    25[0-5]| #250-255
    2[0-4][0-9]| #200-249
    1[0-9]{2}| #100-199
    [1-9][0-9]| #10-99
    [0-9]#0-9
    )$
''', flags=re.X)

for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip, ip_reg_exp.findall(ip))
