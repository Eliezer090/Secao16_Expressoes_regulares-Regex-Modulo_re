import re
texto = """
    <p>Frase1</p> <p>Frase2</p> <p>Frase3</p> <div>Frase4</div>
"""
print(re.findall('<[pdiv]{1,3}>(.*?)</[pdiv]{1,3}>', texto))
# Guloso pois pega tudo te o fim
print(re.findall('<p>.*?</p>', texto))
print(re.findall('<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto))
