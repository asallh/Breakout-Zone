import logging
import sys
from datetime import datetime

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
    