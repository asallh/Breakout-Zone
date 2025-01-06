import logging
import sys
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

import requests

from app.nhl.connectors import NhlConnector

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

def job_start():
    print(f"Staring job at {datetime.now()}")

def player_collection_job():
    logging.info(f"player_collector_job started at {datetime.now()}")
    connector = NhlConnector()
    players_url = connector.get_players()
    response = requests.get(players_url)
    response.raise_for_status()
    players = response.json()
    logging.info(f"Fetched players: {players}")



def main():
    scheduler = BlockingScheduler()
    scheduler.add_job(player_collection_job, 'interval', hours=24)
    scheduler.start()

if __name__ == "__main__":
    job_start()
    main()