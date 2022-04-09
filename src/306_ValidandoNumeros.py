import re


def is_float(string) -> bool:
    return bool(re.search(r'^[+-]?\d+(?:\.\d+)?$', string))


def is_int(string) -> bool:
    return bool(re.search(r'^[+-]?\d+$', string))


def is_numer(string) -> bool:
    if is_int(string):
        return True
    elif is_float(string):
        return True
    return False


print(is_float('1.2'))
print(is_float('1.2.3'))
print(is_float('12'))
print(is_float('-12'))
print(is_int('1'))
print(is_int('1.2'))

print("number")
print(is_numer('1'))
print(is_numer('1.2'))
print(is_numer('1.2.3'))
print(is_numer('12'))
print(is_numer('-12'))
print(is_numer('-12.3'))
print(is_numer('-12.3.4'))
print(is_numer('aaaaa'))


texto = '''
Válidos
0.0
00.00
000.000
+0.0
-00.00
+000.000
10
+10
-1
50
8.5
-8.5
+10.5005412136
1231345458.54654564
-133215646589.6543215648978977
+1.11123123
-0.154987
1.121654987
10.123
10.1
-1.1

Inválidos
10..2
++1213
--1235050
.124546
-.1231324
10.
.1
.10
10.
+10.
-10.
5a
b5
'''
