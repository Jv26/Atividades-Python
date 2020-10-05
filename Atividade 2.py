time = input('nome do time:')
derrotas = int(input('números de derrotas:'))
empates = int(input('números de empates:'))
vitorias = int(input('números de vitórias:'))
pontos = vitorias * 3 + empates
perdidos = derrotas * 3 + empates * 2
print('pontos ganhos:', pontos)
print('pontos perdidos:', perdidos)
