from venv import logger
import requests

from app.nhl.models import PlayerModel


class NhlConnector:

    teams_url = "https://api-web.nhle.com/v1/club-stats/{}/now"
    players_url = "https://api-web.nhle.com/v1/player/{}/landing"

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

    @classmethod
    def get_player_stats(cls):
        players = "This is a test string"
        # for team_name, team_abbr in cls.teams.items():
        #     roster_url = cls.teams_url.format(team_abbr)
        #     try:
        #         roster_response = requests.get(roster_url)
        #         roster_response.raise_for_status()
        #         roster_data = roster_response.json()
        #
        #         for player in roster_data.get('roster', []):
        #             player_id = player.get('playerId')
        #             player_url = cls.players_url.format(player_id)
        #             player_response = requests.get(player_url)
        #             player_response.raise_for_status()
        #             player_data = player_response.json()
        #
        #             player_obj = PlayerModel(
        #                 player_id=player_id,
        #                 name=f"{player.get('firstName')} {player.get('lastName')}",
        #                 team=team_name,
        #                 headshot=player_data.get('headshot', ''),
        #                 position=player.get('positionCode', ''),
        #                 height=player.get('height', ''),
        #                 weight=player.get('weight', ''),
        #                 age=player.get('age', ''),
        #                 career=player_data.get('careerStats', {}).get('regularSeason', {}),
        #                 season=player_data.get('seasonStats', {}).get('regularSeason', {})
        #             )
        #             players.append(player_obj)
        #
        #     except requests.RequestException as e:
        #         logger.error(f"Error fetching data: {e}")

        return players