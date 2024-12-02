from fastapi import APIRouter, HTTPException
from typing import List
from src.app.models.players import Player
from src.app.models.team import Team
from src.app.models.players import SeasonStats

router = APIRouter()

@router.post("/players/", response_model=Player)
async def create_player(player: Player):
    if player.team and not await Team.find_one(Team.name == player.team):
        raise HTTPException(status_code=404, detail="Team not found")
    await player.create()
    return player

@router.get("/players/", response_model=List[Player])
async def get_players():
    return await Player.find_all().to_list()

@router.get("/players/{player_id}", response_model=Player)
async def get_player(player_id: str):
    player = await Player.get(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player