nascimento = str(input('Qual cidade você naceu? ')).strip()
print(nascimento[:nascimento.find(' ')].lower() == 'santo')