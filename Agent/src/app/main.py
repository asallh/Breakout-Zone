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

logger = logging.getLogger(__name__)

def job_start():
    print(f"Staring job at {datetime.now()}")

def player_collection_job():
    logging.info("player_collection_job started")
    PlayerCollector().collect_and_send()


def main():
    scheduler = BlockingScheduler()
    scheduler.add_job(player_collection_job, 'interval', hours=24, next_run_time=datetime.now())
    scheduler.start()

if __name__ == "__main__":
    job_start()
    main()