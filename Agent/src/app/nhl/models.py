class PlayerModel:
    def __init__(self, player_id, name, team, headshot, position, height, weight, age, career, season):
        self.player_id = player_id
        self.name = name
        self.team = team
        self.headshot = headshot
        self.position = position
        self.height = height
        self.weight = weight
        self.age = age
        self.career = career
        self.season = season

    def to_json(self):
        return {
            "PlayerId": self.player_id,
            "Name": self.name,
            "Team": self.team,
            "Headshot": self.headshot,
            "Position": self.position,
            "Height": self.height,
            "Weight": self.weight,
            "Age": self.age,
            "Career Stats": self.career,
            "Season Stats": self.season
        }

    def debug(self):
        print(self.to_json())