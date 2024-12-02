from fastapi import FastAPI, HTTPException
from app.models.player import Player
from app.models.team import Team

app = FastAPI()

# Fetch all players
@app.get("/players")
async def get_players():
    players = await Player.find_all().to_list()
    return {"players": players}

# Add a new player
@app.post("/players")
async def add_player(player: Player):
    existing_player = await Player.find_one(Player.id == player.id)
    if existing_player:
        raise HTTPException(status_code=400, detail="Player already exists")
    await player.insert()
    return {"message": "Player added successfully"}

# Fetch all teams
@app.get("/teams")
async def get_teams():
    teams = await Team.find_all().to_list()
    return {"teams": teams}