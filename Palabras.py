numeros = [1, 3, 67, 5, 88, 54, 54, 54, 5, 7, 4, 12, 6, 88, 88]

control = ""
resultado = []
for num in numeros:
    if num != control:
        resultado.append(num)
    control = num

print resultado
