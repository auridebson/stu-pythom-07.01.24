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

frutas_tropicais = [
    'Abacaxi',
    'Manga',
    'Goiaba',
    'Banana',
    'Coco',
    'Maracujá',
    'Caju',
    'Abacate',
    'Pitaya',
    'Graviola',
    'Kiwi',
    'Papaya',
    'Jabuticaba',
    'Lichia',
    'Rambutã'
]

frutas = ["Maça","Limão","Pera",]

def ln(x):
    print("-"*30)

print("Programa para estudar listas")
ln(45)

# for indice, pais in enumerate(paises_africanos): 
#     print(f"""País: {pais}\nCapital: {paises_africanos[pais]}""")
#     ln(30) 

while True:
    for item, fruta in enumerate(frutas_tropicais):
        print(f"""{item+1}º - {fruta}""")
    escolha = int(input("Qual a fruta que você quer deletar? "))
    if escolha == 100:
        break
    frutas_tropicais.pop(escolha-1)

