import logging
from app.app_constants import Constants


async def init_db():
    logger = logging.getLogger(Constants.LOGGER_DEFAULT)

    logger.info("Connecting to MongoDB: {}:{}/{}".format(Constants.get_mongo_host(),
                                                         Constants.get_mongo_port(),
                                                         Constants.get_mongo_database()))

    connection_string = "mongodb://{}:{}@{}:{}/{}".format(Constants.get_mongo_username(),
                                                          Constants.get_mongo_password(),
                                                          Constants.get_mongo_host(),
                                                          Constants.get_mongo_port(),
                                                          Constants.get_environment())
