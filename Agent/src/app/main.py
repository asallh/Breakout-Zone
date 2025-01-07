import logging
import sys
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

import requests

from app.nhl.collectors import PlayerCollector
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
    logging.info("player_collection_job started")
    PlayerCollector().collect_and_send()

def run_get_player_stats():
    connector = NhlConnector()
    players_stats = connector.get_player_stats(None)  # Pass None or appropriate collector instance
    for player in players_stats:
        print(player.to_json())


logging = logging.getLogger(__name__)

def main():
    scheduler = BlockingScheduler()
    scheduler.add_job(player_collection_job, 'interval', hours=24, next_run_time=datetime.now())
    scheduler.start()

if __name__ == "__main__":
    job_start()
    main()