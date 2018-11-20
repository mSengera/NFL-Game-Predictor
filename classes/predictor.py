class Predictor:

    first_team = ""
    second_team = ""

    def __init__(self, first_team, second_team):
        self.first_team = first_team
        self.second_team = second_team
        self.predict()

    def predict(self):
        print('I will predict...' + str(self.first_team) + "/" + str(self.second_team))


