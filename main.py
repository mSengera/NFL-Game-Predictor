"""
NFL Game Predictor
"""
from classes.predictor import Predictor

print('-------------------------------')
print('--- NFL Game Predictor --------')
print('-------------------------------\n')

print('Input in following way - DEN/NE')
print('To exit, type "exit"\n')

allowed_input = [
    'SF',   # 49ers
    'CHI',  # Bears
    'CIN',  # Bengals
    'BUF',  # Bills
    'DEN',  # Broncos
    'CLE',  # Browns
    'ARI',  # Cardinals
    'LAC',  # Chargers
    'KC',   # Chiefs
    'IND',  # Colts
    'DAL',  # Cowboys
    'MIA',  # Dolphins
    'PHI',  # Eagles
    'ATL',  # Falcons
    'NYG',  # Giants
    'JAC',  # Jaguars
    'NYJ',  # Jets
    'DET',  # Lions
    'GB',   # Packers
    'CAR',  # Panthers
    'NE',  # Patriots
    'OAK',  # Raiders
    'LAR',  # Rams
    'BAL',  # Ravens
    'WAS',  # Redskins
    'NO',   # Saints
    'SEA',  # Seahawks
    'PIT',  # Steelers
    'TB',   # Tampa Bay
    'HOU',  # Texans
    'TEN',  # Titans
    'MIN'   # Vikings
]


def main():
    while True:
        raw_input = input("Prediction for: ")

        if raw_input == "exit":
            exit()

        input_split = raw_input.split('/')

        if input_split[0] in allowed_input and input_split[1] in allowed_input:
            predictor = Predictor(input_split[0], input_split[1])
        else:
            print('Wrong input. Please try again. Only use valid team short names.')


main()
