import logging
from venv import logger

import requests

from app.app_config import Constants
from app.nhl.connectors import NhlConnector


class NhlCollectorBase:

    logger = logging.getLogger(__name__)
    __extension_URL = "v1/players/"

    def __init__(self):
        self.nhl_connector = NhlConnector()

    def send(self, model, base_url):
        packet = model.to_json()
        url = base_url + self.__extension_URL
        logging.info(f"Sending to {url}: {packet}")
        
        try:
            response = requests.post(url, json=packet)
            response.raise_for_status()  # Raises an exception for 4XX/5XX status codes
            logging.info(f"Successfully sent player data. Status: {response.status_code}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send player data: {str(e)}")
            return None



class PlayerCollector(NhlCollectorBase):
    def __init__(self):
        super().__init__()
        self.players_endpoint = Constants.get_players_rest_endpoint()

    def collect_and_send(self):
       logging.info(NhlConnector.get_player_stats(self))
       NhlConnector.get_player_stats(self)