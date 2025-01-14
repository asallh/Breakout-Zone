import logging
from venv import logger

from app.app_config import Constants
from app.nhl.connectors import NhlConnector


class NhlCollectorBase:

    logger = logging.getLogger(__name__)

    def __init__(self):
        self.nhl_connector = NhlConnector()

    def send(self, model, base_url):
        # Use this method to send data into the database
        print(f"Sending data to {base_url} Mongo Database")
        print(model)



class PlayerCollector(NhlCollectorBase):
    def __init__(self):
        super().__init__()
        self.players_endpoint = Constants.get_players_rest_endpoint()

    def collect_and_send(self):
       logging.info(NhlConnector.get_player_stats(self))
       NhlConnector.get_player_stats(self)