class PlayerModel:
    def __init__(self, player_id, name, team, headshot, hero, position, sweater, height, weight, career, season):
        self.player_id = player_id
        self.name = name
        self.team = team
        self.headshot = headshot
        self.hero = hero
        self.position = position
        self.sweater = sweater
        self.height = height
        self.weight = weight
        self.career = career
        self.season = season

    def to_json(self):
        return {
            "player_id": str(self.player_id),  # Ensure player_id is string
            "name": self.name,
            "team": self.team,
            "headshot": self.headshot,
            "hero": self.hero,
            "position": self.position,
            "sweater": self.sweater,
            "height": self.height,
            "weight": self.weight,
            "career_totals": self.career,
            "season_totals": self.season
        }

    def debug(self):
        print(self.to_json())

    def get_season_stats(self):
        return self.season

    def get_career_stats(self):
        return self.career