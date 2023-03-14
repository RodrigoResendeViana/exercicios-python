var_a = int(input('Digite o valor da variavel a: '))
var_b = int(input('Digite o valor da variavel b: '))

aux = var_a
var_a = var_b
var_b = aux

print(f' Os valores das variaveis foram invertidos, tendo a variavel a como {var_a} e a variavel b como {var_b}')