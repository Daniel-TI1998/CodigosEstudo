altura = float(input('Qual a sua altura em cm:'))
peso = float(input('Qual o seu peso em Kg:'))

IMC = peso / (altura/100)** 2

print (IMC)

if IMC < 18.5:
  print(f'Seu IMC é de {IMC}, e é calculada como da classificação Magreza')

elif IMC >= 18.5 and IMC < 24.9:
  print(f'Seu IMC é de {IMC}, e é calculada como  classificação normal')

elif IMC >= 25 and IMC < 29.9:
  print(f'Seu IMC é de {IMC}, e é calculada como classificação sobrepeso')

elif IMC >= 30 and IMC < 34.9:
  print(f'Seu IMC é de {IMC}, e é calculada como classificação obsedidade grau 1')

elif IMC >= 35 and IMC < 39.9:
  print(f'Seu IMC é de {IMC}, e é calculada como classificação obsedidade grau 2')

elif IMC > 40:
  print(f'Seu IMC é de {IMC}, e é calculada como classificação obsedidade grau 3')

else:
  print(" de acordo com as informações, fornecidas busque um medico.")