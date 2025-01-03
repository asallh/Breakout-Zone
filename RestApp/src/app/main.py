from contextlib import asynccontextmanager
from venv import logger

import uvicorn
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
import os

from starlette.middleware.cors import CORSMiddleware

from app.app_constants import Constants
from app.connectors.database_odm import init_db
from app.routers.v1 import players as v1_players

# MongoDB URI (using environment variable or default connection string)
MONGO_URI = "mongodb://{}:{}@{}:{}/{}".format(Constants.get_mongo_username(),
                                                      Constants.get_mongo_password(),
                                                      Constants.get_mongo_host(),
                                                      Constants.get_mongo_port(),
                                                      Constants.get_mongo_database())

# MongoDB client
client = AsyncIOMotorClient(MONGO_URI)

# Create a custom lifespan context manager for FastAPI
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Ping MongoDB server on startup
        await client.admin.command("ping")
        print("MongoDB connected successfully")
        logger.info("starting up BreakoutZone REST")
        logger.info("Current Environment context: {}".format(Constants.get_environment()))
        logger.debug("Waiting for database to be available...")
        await init_db()
        # logger.info("Database connection established")
        yield
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise

# Create the FastAPI app instance and pass the lifespan context
app = FastAPI(lifespan=lifespan)

app.include_router(v1_players.router, prefix="/api/v1/players")

# origins = [
#     "*"
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/")
async def root():
    return {"message": "MongoDB Ping Test Passed!"}
@app.get("/api/ping")
async def ping():
    return {"msg": "pong", "Environment": Constants.get_environment()}

if __name__ == "__main__":
    # Run the Uvicorn server directly from the script
    print("MongoDB URI:", MONGO_URI)
    print("Environment:", Constants.get_environment())
    print("Mongo Host:", Constants.get_mongo_host())
    print("Mongo Port:", Constants.get_mongo_port())
    print("Mongo Username:", Constants.get_mongo_username())
    print("Mongo Database:", Constants.get_mongo_database())
    print("Mongo Attributes:", Constants.get_mongo_attributes())

    print("Starting Uvicorn server...")
    uvicorn.run("src.app.main:app", host="0.0.0.0", port=8000, reload=True)