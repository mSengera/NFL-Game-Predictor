"""
Usw newB generated in predict-score-with-yards_get-linear-refression.py
"""
newB = [-0.02393084, 0.05351758, 0.08413694]

print('Get a prediction of game score by typing in passing and rushing yards of the game.')
seen_passing_yards = input('Passing yards: ')
seen_rushing_yards = input('Rushing yards: ')

print(newB[0] + newB[1] * float(seen_passing_yards) + newB[2] * float(seen_rushing_yards))
