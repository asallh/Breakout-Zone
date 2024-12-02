from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from src.app.models.players import Player
from src.app.models.team import Team

MONGO_URI = "mongodb://localhost:27017"  # Update with your MongoDB URI

async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    await init_beanie(database=client.your_database_name, document_models=[Player, Team])