from venv import logger

import requests

from app.app_config import Constants
from app.nhl.models import PlayerModel


class NhlConnector:

    teams = {
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

    # Helper function to get player data

    def get_player_data(self):
        players_url = f"https://api-web.nhle.com/v1/player/{self}/landing"
        player_response = requests.get(players_url)
        if player_response.status_code == 200:
            return player_response.json()
        else:
            logger.error(f"Failed to fetch player data for {self} - Status code: {player_response.status_code}")
            return None

    @classmethod
    def get_player_stats(cls, collector):
        player_data = []
        teams_count = 0
        for team, abbreviation in cls.teams.items():
            logger.info(f"Getting team data for {team}")
            teams_url = f"https://api-web.nhle.com/v1/club-stats/{abbreviation}/now"
            teams_response = requests.get(teams_url)
            if teams_response.status_code == 200:
                teams_count += 1
                teams_data = teams_response.json()
                # iterating for the skaters
                for skater in teams_data.get("skaters", []):
                    player_id = skater.get("playerId")
                    if player_id:
                        player_data = cls.get_player_data(player_id)
                        if player_data:
                            logger.info(
                                f"Successfully fetched player data for Skater: {skater['firstName']['default']} {skater['lastName']['default']}")
                            player_model = PlayerModel(
                                player_id=player_data.get("playerId"),
                                name=f"{player_data.get('firstName')['default']} {player_data.get('lastName')['default']}",
                                team=team,
                                headshot=player_data.get("headshot"),
                                hero=player_data.get("heroImage"),
                                position=player_data.get("position"),
                                height=player_data.get("heightInInches"),
                                weight=player_data.get("weightInPounds"),
                                career=player_data.get("featuredStats", {}).get("regularSeason", {}).get("career", {}),
                                season=player_data.get("featuredStats", {}).get("regularSeason", {}).get("subSeason", {})
                            )
                            print(player_model.to_json())
                            # Sending to DB
                            collector.send(player_model, Constants.get_players_rest_endpoint())

                        else:
                            logger.error(f"Failed to fetch data for Skater with playerId {player_id}")

                #  iterating over for the goalies
                for goalie in teams_data.get("goalies", []):
                    player_id = goalie.get("playerId")
                    if player_id:
                        goalie_data = cls.get_player_data(player_id)
                        if goalie_data:
                            logger.info(
                                f"Successfully fetched player data for goalie: {goalie['firstName']['default']} {goalie['lastName']['default']}")
                            player_model = PlayerModel(
                                player_id=goalie_data.get("playerId"),
                                name=f"{goalie_data.get('firstName')['default']} {goalie_data.get('lastName')['default']}",
                                team=team,
                                headshot=goalie_data.get("headshot"),
                                hero=goalie_data.get("hero"),
                                position=goalie_data.get("position"),
                                height=goalie_data.get("heightInInches"),
                                weight=goalie_data.get("weightInPounds"),
                                career=goalie_data.get("featuredStats", {}).get("regularSeason", {}).get("career", {}),
                                season=goalie_data.get("featuredStats", {}).get("regularSeason", {}).get("subSeason", {})
                            )
                            print(player_model.to_json())
                            # Sending to DB
                            collector.send(player_model, Constants.get_players_rest_endpoint())
                        else:
                            logger.error(f"Failed to fetch data for Skater with playerId {player_id}")

            else:
                logger.error(f"Error getting team data {team}, {teams_response.status_code}")
        print(f"Teams count: {teams_count}")
