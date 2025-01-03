from beanie import Document
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class SeasonStats(BaseModel):
    NHL: Dict[str, Any] = {}

class PlayerMasterDocument(Document):
    first: str
    last: str
    sweater: int
    team: Optional[str]  # References Team name or ObjectId if using relations
    season_totals: Optional[SeasonStats] = Field(default_factory=SeasonStats)
    career_totals: Optional[Dict[str, Any]] = Field(default_factory=dict)

    class Settings:
        name = "players"
