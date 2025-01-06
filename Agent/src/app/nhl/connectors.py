import requests

class NhlConnector:

    teams ={
    "Anaheim Ducks": "ANA",
    "Arizona Coyotes": "ARI",
    "Boston Bruins": "BOS",
    "Buffalo Sabres": "BUF",
    "Carolina Hurricanes": "CAR",
    "Columbus Blue Jackets": "CBJ",
    "Calgary Flames": "CGY",
    "Chicago Blackhawks": "CHI",
    "Colorado Avalanche": "COL",
    "Dallas Stars": "DAL",
    "Detroit Red Wings": "DET",
    "Edmonton Oilers": "EDM",
    "Florida Panthers": "FLA",
    "Los Angeles Kings": "LAK",
    "Minnesota Wild": "MIN",
    "Montreal Canadiens": "MTL",
    "New Jersey Devils": "NJD",
    "Nashville Predators": "NSH",
    "New York Islanders": "NYI",
    "New York Rangers": "NYR",
    "Ottawa Senators": "OTT",
    "Philadelphia Flyers": "PHI",
    "Pittsburgh Penguins": "PIT",
    "Seattle Kraken": "SEA",
    "San Jose Sharks": "SJS",
    "St. Louis Blues": "STL",
    "Tampa Bay Lightning": "TBL",
    "Toronto Maple Leafs": "TOR",
    "Utah Hockey Club": "UTA",
    "Vancouver Canucks": "VAN",
    "Vegas Golden Knights": "VGK",
    "Washington Capitals": "WSH",
    "Winnipeg Jets": "WPG"
}

    def __init__(self):
        self.teams_url = 'https://api-web.nhle.com/v1/roster/{}/20242025'
        self.players_url='https://api-web.nhle.com/v1/player/{}/landing'

    def get_team_roster(self, team_abbr):
        url = self.teams_url.format(team_abbr)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch roster for {team_abbr}")

    def get_all_athletes(cls, collector):
        athletes = []
        for team in self.teams:
            athletes.append(self.get_team_roster(self.teams[team]))
        return athletes