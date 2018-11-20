"""
NFL Game Predictor
"""
print('-------------------------------')
print('--- NFL Game Predictor --------')
print('-------------------------------\n')

print('Input in following way - DEN/NE')
print('To exit, type "exit"\n')


def main():
    while True:
        raw_input = input("Prediction for: ")

        if raw_input == "exit":
            exit()


main()
