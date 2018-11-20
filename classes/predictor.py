from pathlib import Path
from classes.calculateRegressionFunction import CalculateRegressionFunction
import json


class Predictor:

    first_team = ""
    second_team = ""

    rushing_yards_home = 0
    rushing_yards_away = 0

    def __init__(self, first_team, second_team):
        self.first_team = first_team
        self.second_team = second_team
        self.predict()

    def predict(self):
        print('I will predict... ' + str(self.first_team) + "/" + str(self.second_team))

        """
        Start by predicting the rushing yards per team
        """
        path = "classes/regression_functions/predict_rushing_yards/" + str(self.first_team) + "-" + str(self.second_team) + ".json"
        data_function = Path(path)

        if data_function.is_file():
            print("Load the data.")

            file = open(path, "r")
            json_string = file.readline()

            function_parameter = json.loads(json_string)
        else:
            print("Generate the data.")
            f = CalculateRegressionFunction()
            function_parameter = f.calculate_average_rushing_yards(self.first_team, self.second_team)

            file = open(path, "w")
            file.write(json.dumps(function_parameter))

        self.rushing_yards_home = function_parameter[0]
        self.rushing_yards_away = function_parameter[1]

        """
        Predicting the passing yards per team
        """

        """
        Predict score per team by rushing and passing yards
        """

        exit()
