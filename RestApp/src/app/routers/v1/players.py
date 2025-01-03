from fastapi import APIRouter, HTTPException
from typing import List
from app.models.players import PlayerMasterDocument
from app.models.team import Team
from app.models.players import SeasonStats

router = APIRouter()


@router.post("/", response_model=PlayerMasterDocument)
async def create_player(player: PlayerMasterDocument):
    if player.team and not await Team.find_one(Team.name == player.team):
        raise HTTPException(status_code=404, detail="Team not found")
    await player.create()
    return player


@router.get("/", response_model=List[PlayerMasterDocument])
async def get_players():
    return await PlayerMasterDocument.find_all().to_list()


@router.get("/{player_id}", response_model=PlayerMasterDocument)
async def get_player(player_id: str):
    player = await PlayerMasterDocument.get(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@router.post("/test-insert/")
async def test_insert():
    test_player = PlayerMasterDocument(
        first="Aj",
        last="Sallh",
        team="Parking Lot Bears",
        sweater=17,
        season_totals=SeasonStats(NHL={"goals": 30, "assists": 40}),
        career_totals={"NHL": {"goals": 100, "assists": 150}}
    )
    await test_player.insert()
    return test_player
