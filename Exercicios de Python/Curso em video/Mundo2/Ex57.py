sexo = str(input('Digite o seu sexo: M/F: ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Nome invalido, digite novamento o seu nome: ')).upper()
print(sexo)