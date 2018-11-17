# [Machine learning] NFL-Game-Predictor
To get some practice in machine learning, I trying to solve the prediction of an NFL Game with machine learning.

I use the NFL Game API (https://api.nfl.com/docs/getting-started/index.html) for the underlaying data.

To prevent reengineering the whole nflgame data collection, I used following PyPi Project:
- https://pypi.org/project/nflgame/

Thanks to that really nice api conenctor @BruntShishi ! (https://github.com/BurntSushi/nflgame)

Special thanks to @mlenzen to port the nflgame extension to Python3! (https://github.com/mlenzen/nflgame)

### First prediction
First I was predicting the total game score per team, by knowing the total passing yards and the
total rushing yards per game. So, i tried following:

Passing yards: 324<br />
Rushing yards: 146<br />
<br />
Score: 29.59975832

The values are from the Denver Broncos vs. Seattle Seahawks Game. (first week of 2018). I trained my model with all
plays from 2009 - 2017.

The real points where 27 for the Broncos. My prediction was 29.59 Points.

Linear regression gave me following function:

    Scores = -0.02393084 + 0.05351758 * passing_yards + 0.08413694 * rushing_yards
    
Linear regression is computed in tests/predict-score-with-yards_get-linear-regression.py
