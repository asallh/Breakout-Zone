import logging
import motor.motor_asyncio
from beanie import init_beanie

import motor

from app.app_constants import Constants
from app.models.players import PlayerMasterDocument


async def init_db():
    logger = logging.getLogger(Constants.LOGGER_DEFAULT)

    logger.info("Connecting to MongoDB: {}:{}/{}".format(Constants.get_mongo_host(),
                                                         Constants.get_mongo_port(),
                                                         Constants.get_mongo_database()))

    connection_string = "mongodb://{}:{}@{}:{}/{}".format(Constants.get_mongo_username(),
                                                          Constants.get_mongo_password(),
                                                          Constants.get_mongo_host(),
                                                          Constants.get_mongo_port(),
                                                          Constants.get_mongo_database())


    client = motor.motor_asyncio.AsyncIOMotorClient(connection_string)

    db = client[Constants.get_mongo_database()]

    beanie_objects = [PlayerMasterDocument]

    await init_beanie(database=db, document_models=beanie_objects)