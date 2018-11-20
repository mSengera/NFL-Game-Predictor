from classes.getData import GetData


class CalculateRegressionFunction:

    def regression_function_for_rushing_yards(self, home_team, away_team):
        print('Calculating...')

        data_model = GetData()
        data = data_model.get_rushing_yards_per_team(home_team, away_team)

        exit()

        return [0, 0, 0]
