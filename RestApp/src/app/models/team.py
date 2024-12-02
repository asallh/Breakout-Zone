from pydantic import BaseModel, Field
from typing import Optional, Dict

class SequenceStats(BaseModel):
    overall: int
    home: Optional[int] = None
    road: Optional[int] = None
    l10: Optional[int] = None

class GoalStats(BaseModel):
    for_: int = Field(..., alias="for")
    against: int
    differential: int
    forPctg: Optional[float] = None
    differentialPctg: Optional[float] = None

class WinStats(BaseModel):
    total: int
    percentage: float
    regulation: Optional[Dict[str, Optional[float]]] = None
    regulationPlusOt: Optional[Dict[str, Optional[float]]] = None

class StreakStats(BaseModel):
    code: str
    count: int

class TeamInfo(BaseModel):
    abbreviation: str
    logo: str
    placeName: Dict[str, str]
    commonName: Dict[str, str]
    name: Dict[str, str]

class LocationStats(BaseModel):
    gamesPlayed: int
    wins: int
    regulationWins: Optional[int] = None
    regulationPlusOtWins: Optional[int] = None
    losses: int
    otLosses: Optional[int] = None
    ties: int
    points: int
    goals: GoalStats

class Last10Stats(LocationStats):
    pass

class ConferenceStats(BaseModel):
    abbrev: str
    name: str
    sequence: SequenceStats

class DivisionStats(BaseModel):
    abbrev: str
    name: str
    sequence: SequenceStats

class Team(BaseModel):
    conference: ConferenceStats
    division: DivisionStats
    leagueSequence: SequenceStats
    seasonId: int
    gameTypeId: int
    date: str
    gamesPlayed: int
    goals: GoalStats
    points: Dict[str, float]
    wins: WinStats
    losses: Dict[str, Optional[int]]
    ties: int
    streak: StreakStats
    home: LocationStats
    road: LocationStats
    last10: Last10Stats
    teamInfo: TeamInfo

    class Config:
        allow_population_by_field_name = True