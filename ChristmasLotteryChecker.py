# INSERTAR AQUÍ LOS NÚMEROS JUGADOS Y SUS RESPECTIVOS VALORES --> (numero) : (valor)
# ----------------------------------------------------------------------------------
numbers = {86148: 20, 0: 2.5, 39000: 5}  # Dictionary with the played numbers and the money spent on them. Key: number, value: money
# No deben escribirse ceros a la izquierda de un número ni puntos para los miles. Los costes que tengan decimales no deben
# llevar ',' sino '.'



# Imports
from bs4 import BeautifulSoup
import requests

# Initialization of lists
winning_numbers = []
number_prizes = []

# Gets the winning numbers and their prizes
for i in range(0, 95001, 5000):
    url = 'https://www.rtve.es/loterias/loteria-navidad/Loteria_'+str(i).zfill(5)+'.shtml'  # Database-web with the prizes
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    
    # Winning numbers getter
    for num in soup.find_all('td', attrs={'class' : 'n'}):
        winning_numbers.append(int(num.text.replace('.', '')))
    for num in soup.find_all('b', attrs={'class' : 'n'}):
        winning_numbers.append(int(num.text.replace('.', '')))
        
    # Prizes getter
    for pri in soup.find_all('td', attrs={'class' : 'p'}):
        number_prizes.append(int(pri.text.replace('.', '').replace('€', '')))
    for pri in soup.find_all('b', attrs={'class' : 'p'}):
        number_prizes.append(int(pri.text.replace('.', '').replace('€', '')))

total_cost = sum(numbers.values())
won = 0
prize = 0

# Number checker
for number, cost in numbers.items():
    if number in winning_numbers:
        prize = round(cost * number_prizes[winning_numbers.index(number)] / 200, 2)
        won += prize
        print(f'Número {number} premiado con {round(cost * number_prizes[winning_numbers.index(number)] / 200, 2)}€. Invertidos {cost}€')

if won == 0:
    print('Lo siento, no ha habido suerte este año')
else:
    print(f'\nResultados:\nGastado: {total_cost}€ Ganado: {won}€')
