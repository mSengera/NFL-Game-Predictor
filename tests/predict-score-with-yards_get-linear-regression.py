import nflgame
import numpy as np

datapoints = []

nflyears = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

for year in nflyears:
    games = nflgame.games(year)
    plays = nflgame.combine_plays(games)

    for g in games:
        """
        Proceed home team
        """
        new_data_home = {}

        new_data_home['team'] = g.home
        new_data_home['opponent'] = g.away
        new_data_home['score'] = g.data['home']['score']['T']

        passing_home = 0

        for passing in g.data['home']['stats']['passing']:
            passing_home = passing_home + g.data['home']['stats']['passing'][passing]['yds']

        new_data_home['passing_yards'] = passing_home

        rushing_home = 0

        for rushing in g.data['home']['stats']['rushing']:
            rushing_home = rushing_home + g.data['home']['stats']['rushing'][rushing]['yds']

        new_data_home['rushing_yards'] = rushing_home

        datapoints.append(new_data_home)

        """
        Proceed away team
        """
        new_data_away = {}

        new_data_away['team'] = g.away
        new_data_away['opponent'] = g.home
        new_data_away['score'] = g.data['away']['score']['T']

        passing_away = 0

        for passing in g.data['away']['stats']['passing']:
            passing_away = passing_away + g.data['away']['stats']['passing'][passing]['yds']

        new_data_away['passing_yards'] = passing_away

        rushing_away = 0

        for rushing in g.data['away']['stats']['rushing']:
            rushing_away = rushing_away + g.data['away']['stats']['rushing'][rushing]['yds']

        new_data_away['rushing_yards'] = rushing_away

        datapoints.append(new_data_away)

"""
Predict Score with Passing- and Rushing Yards
"""


def cost_function(X, Y, B):
    m = len(Y)
    J = np.sum((X.dot(B) - Y) ** 2)/(2 * m)
    return J


def gradient_descent(X, Y, B, alpha, iterations):
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
        cost = cost_function(X, Y, B)
        cost_history[iteration] = cost

    return B, cost_history


score = []
ps_yrds = []
rs_yrds = []

for point in datapoints:
    score.append(point['score'])
    ps_yrds.append(point['passing_yards'])
    rs_yrds.append(point['rushing_yards'])

m = len(ps_yrds)
x0 = np.ones(m)
X = np.array([x0, ps_yrds, rs_yrds]).T

# Initial Coefficients
B = np.array([0, 0, 0])
Y = np.array(score)
alpha = 0.000001

inital_cost = cost_function(X, Y, B)
print(inital_cost)

# 100.000 Iterations
newB, cost_history = gradient_descent(X, Y, B, alpha, 100000)

# New Values of B
print(newB)

# Final Cost of new B
print(cost_history[-1])
