cadastros = inferior = entre = superior = 0
for cadastros in range (10):
    altura = float(input('altura:'))
    if altura < 1.6:
        inferior += 1
    elif 1.8 >= altura >= 1.6:
        entre += 1
    else:
        superior += 1
print(f'''
Foram cadastradas {cadastros+1} pessoas.
Pessoas com altura < 1,60 metros: {inferior}
Pessoas com altura entre 1,60 e 1,80: {entre}
Pessoas com altura superior a 1,80 metros: {superior}
''')