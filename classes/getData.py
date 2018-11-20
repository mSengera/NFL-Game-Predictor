import nflgame


class GetData:

    nfl_years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

    def get_rushing_yards_per_team(self, home, away):

        for year in self.nfl_years:
            games = nflgame.games(year)

            print(year)

        return []
