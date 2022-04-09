import re

def validar_email(email):
    regex = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')
    if regex.search(email):
        return True
    else:
        return False

print(validar_email('eliezer@gmail.com'))
print(validar_email('eliezer@gmail'))
print(validar_email('asdfa@asd.asd'))
print(validar_email('émail@gmail.com'))
print(validar_email('nao é email'))

