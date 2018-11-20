from classes.getData import GetData
import numpy as np


class CalculateRegressionFunction:

    def regression_function_for_rushing_yards(self, home_team, away_team):
        print('Calculating...')

        data_model = GetData()
        data = data_model.get_rushing_yards_per_team(home_team, away_team)

        rushing_home = data[0]
        rushing_away = data[1]

        average_rushing_home = sum(data[0]) / len(data[0])
        average_rushing_away = sum(data[1]) / len(data[1])

        return [0, 0, 0]

    """
    Linear Regression functions
    """
    def cost_function(self, X, Y, B):
        m = len(Y)
        J = np.sum((X.dot(B) - Y) ** 2) / (2 * m)
        return J

    def gradient_descent(self, X, Y, B, alpha, iterations):
        cost_history = [0] * iterations
        m = len(Y)

        for iteration in range(iterations):
            # Hypothesis Values
            h = X.dot(B)

            # Difference b/w Hypothesis and Actual Y
            loss = h - Y

            # Gradient Calculation
            gradient = X.T.dot(loss) / m

            # Changing Values of B using Gradient
            B = B - alpha * gradient

            # New Cost Value
            cost = self.cost_function(X, Y, B)
            cost_history[iteration] = cost

        return B, cost_history
