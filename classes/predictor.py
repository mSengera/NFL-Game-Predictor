from pathlib import Path

class Predictor:

    first_team = ""
    second_team = ""

    def __init__(self, first_team, second_team):
        self.first_team = first_team
        self.second_team = second_team
        self.predict()

    def predict(self):
        print('I will predict... ' + str(self.first_team) + "/" + str(self.second_team))

        """
        Start by predicting the rushing yards per team
        """
        regression_function = Path("regression_functions/predict_rushing_yards/" + str(self.first_team) + "-" + str(self.second_team) + ".json")

        if regression_function.is_file():
            print("Load the regression function.")
        else:
            print("Generate the regression function.")

        exit()
