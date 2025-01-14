from beanie import Document
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class SeasonStats(BaseModel):
    NHL: Dict[str, Any] = {}

class PlayerMasterDocument(Document):
    player_id: str
    name: str
    team: str
    headshot: str
    hero: str
    position: str
    sweater: int
    height: int
    weight: int
    career_totals: Optional[Dict[str, Any]] = Field(default_factory=dict)
    season_totals: Optional[Dict[str, Any]] = Field(default_factory=dict)

    class Settings:
        name = "players"
