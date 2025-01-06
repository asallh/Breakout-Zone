import logging

from app.nhl.connectors import NhlConnector


class NhlCollectorBase:
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.nhl_connector = NhlConnector()

class PlayerCollector(NhlCollectorBase):
    def collect(self):
        self.logger.info("Collecting players")
        players = self.nhl_connector.get_all_athletes()
        return players