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

        # Predict rushing yards per team
        self.predict_rushing_yards()

        """
        Predicting the passing yards per team
        """

        """
        Predict score per team by rushing and passing yards
        """

        exit()

    def predict_rushing_yards(self):
        path = "classes/regression_functions/predict_rushing_yards/" + str(self.first_team) + "-" + str(self.second_team) + ".json"
        data_function = Path(path)

        if data_function.is_file():
            print("Load the data for rushing yards.")

            file = open(path, "r")
            json_string = file.readline()

            function_parameter = json.loads(json_string)
        else:
            print("Generate the data for rushing yards.")
            f = CalculateRegressionFunction()
            function_parameter = f.calculate_average_rushing_yards(self.first_team, self.second_team)

            file = open(path, "w")
            file.write(json.dumps(function_parameter))

        self.rushing_yards_home = function_parameter[0]
        self.rushing_yards_away = function_parameter[1]
