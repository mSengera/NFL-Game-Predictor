"""
Usw newB generated in predict-score-with-yards_get-linear-refression.py
"""
newB = [-5.58921627e+79, -1.47992621e+82, -6.35457306e+81]

print('Get a prediction of game score by typing in passing and rushing yards of the game.')
for seen_passing_yards in input('Passing yards: '):
    seen_rushing_yards = input('Rushing yards: ')

    print(newB[0] + newB[1] * float(seen_passing_yards) + newB[2] * float(seen_rushing_yards))
