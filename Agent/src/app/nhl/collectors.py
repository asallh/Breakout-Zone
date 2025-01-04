import logging

from app.nhl.connectors import NhlConnector


class NhlCollectorBase:
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.nhl_connector = NhlConnector()