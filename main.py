paises_africanos = {
    'Argélia': 'Argel',
    'Angola': 'Luanda',
    'Benin': 'Porto Novo',
    'Botsuana': 'Gaborone',
    'Burquina Faso': 'Ouagadougou',
    'Burundi': 'Bujumbura',
    'Cabo Verde': 'Praia',
    'Camarões': 'Yaoundé',
    'Chade': 'Djamena',
    'Comores': 'Moroni',
    'Congo': 'Brazzaville',
    'Costa do Marfim': 'Yamoussoukro',
    'Djibuti': 'Djibuti',
    'Egito': 'Cairo',
    'Eritreia': 'Asmara',
    'Eswatini': 'Lobamba',
    'Etiópia': 'Adis Abeba',
    'Gabão': 'Libreville',
    'Gâmbia': 'Banjul',
    'Gana': 'Acra',
    'Guiné': 'Conacri',
    'Guiné-Bissau': 'Bissau',
    'Guiné Equatorial': 'Malabo',
    'Lesoto': 'Maseru',
    'Libéria': 'Monróvia',
    'Líbia': 'Trípoli',
    'Madagáscar': 'Antananarivo',
    'Maláui': 'Lilongwe',
    'Mali': 'Bamako',
    'Marrocos': 'Rabat',
    'Maurícia': 'Port Louis',
    'Mauritânia': 'Nouakchott',
    'Moçambique': 'Maputo',
    'Namíbia': 'Windhoek',
    'Níger': 'Niamey',
    'Nigéria': 'Abuja',
    'Quênia': 'Nairóbi',
    'Ruanda': 'Quigali',
    'São Tomé e Príncipe': 'São Tomé',
    'Senegal': 'Dacar',
    'Seicheles': 'Victoria',
    'Serra Leoa': 'Freetown',
    'Somália': 'Mogadíscio',
    'Sudão': 'Cartum',
    'Sudão do Sul': 'Juba',
    'Tanzânia': 'Dodoma',
    'Togo': 'Lomé',
    'Tunísia': 'Túnis',
    'Uganda': 'Kampala',
    'Zâmbia': 'Lusaka',
    'Zimbábue': 'Harare'
}


frutas = ["maça",[]]


def ln(x):
    print("-"*30)

print("Programa para estudar listas")
ln(45)


# for indice, pais in enumerate(paises_africanos): 
#     print(f"""País: {pais}\nCapital: {paises_africanos[pais]}""")
#     ln(30) 

for i in range(3):
    fruta = str(input("Digite uma fruta"))
    frutas[1].append(fruta)
print(frutas)