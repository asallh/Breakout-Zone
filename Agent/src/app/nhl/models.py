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
        packet = {
            "PlayerId": "",
            "Name": "",
            "Team": "",
            "Headshot": "",
            "Position": "",
            "Height": "",
            "Weight": "",
            "Age": "",
            "career": {
                "assists": "",
                "gameWinningGoals": "",
                "gamesPlayed": "",
                "goals": "",
                "otGoals": "",
                "pim": "",
                "plusMinus": "",
                "points": "",
                "powerPlayGoals": "",
                "powerPlayPoints": "",
                "shootingPctg": "",
                "shorthandedGoals": "",
                "shorthandedPoints": "",
                "shots": ""
            },
            "20232024": {
                "assists": "",
                "avgToi": "",
                "faceoffWinningPctg": "",
                "gameTypeId": "",
                "gameWinningGoals": "",
                "gamesPlayed": "",
                "goals": "",
                "leagueAbbrev": "",
                "otGoals": "",
                "pim": "",
                "plusMinus": "",
                "points": "",
                "powerPlayGoals": "",
                "powerPlayPoints": "",
                "season": "",
                "sequence": "",
                "shootingPctg": "",
                "shorthandedGoals": "",
                "shorthandedPoints": "",
                "shots": "",
            }
        }
        return packet

    def print_json(self):
        packet = self.to_json()
        print(packet)


