import logging
from venv import logger

from app.app_config import Constants
from app.nhl.connectors import NhlConnector


class NhlCollectorBase:

    logger = logging.getLogger(__name__)

    def __init__(self):
        self.nhl_connector = NhlConnector()

        def send(self, model, base_url):
            print(f"Sending {model} to {base_url}")



class PlayerCollector(NhlCollectorBase):
    def __init__(self):
        super().__init__()
    def collect_and_send(self):
        players = self.nhl_connector.get_player_stats()
        for player in players:
            logger.info(player.to_json())