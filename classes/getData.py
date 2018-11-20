import nflgame


class GetData:

    nfl_years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

    def get_rushing_yards_per_team(self, home, away):

        rushing_yards_home = []
        rushing_yards_away = []

        for year in self.nfl_years:
            games = nflgame.games(year)

            for g in games:
                if g.home == home and g.away == away:
                    rushing_home = 0

                    for rushing in g.data['home']['stats']['rushing']:
                        rushing_home = rushing_home + g.data['home']['stats']['rushing'][rushing]['yds']

                    rushing_yards_home.append(rushing_home)

                    # ========

                    rushing_away = 0

                    for rushing in g.data['away']['stats']['rushing']:
                        rushing_away = rushing_away + g.data['away']['stats']['rushing'][rushing]['yds']

                    rushing_yards_away.append(rushing_away)

        return [rushing_yards_home, rushing_yards_away]
