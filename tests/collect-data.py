import nflgame
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

datapoints = []

nflyears = [2017]

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
Visualize data
"""

score = []
ps_yrds = []
rs_yrds = []

for point in datapoints:
    score.append(point['score'])
    ps_yrds.append(point['passing_yards'])
    rs_yrds.append(point['rushing_yards'])


fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(score, ps_yrds, rs_yrds, color='#ef1234')
ax.set_xlabel('Score')
ax.set_ylabel('Passing Yards')
ax.set_zlabel('Rushing Yards')
plt.show()
