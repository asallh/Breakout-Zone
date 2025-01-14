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
        # self.age = age
        self.career = career
        self.season = season

    def to_json(self):
        return {
            "PlayerId": self.player_id,
            "Name": self.name,
            "Team": self.team,
            "Headshot": self.headshot,
            "Hero": self.hero,
            "Position": self.position,
            "Jersey Number": self.sweater,
            "Height": self.height,
            "Weight": self.weight,
            # "Age": self.age,
            "Career Stats": self.career,
            "Season Stats": self.season
        }

    def debug(self):
        print(self.to_json())

    def get_season_stats(self):
        return self.season

    def get_career_stats(self):
        return self.career