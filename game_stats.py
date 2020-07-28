import json

class GameStats():
    def __init__(self,ai_setting):
        self.ai_setting = ai_setting
        self.rest_stats()
        #最高分不需要重置
        try:
            with open('high_score.json','r') as jf:
                high_score = json.load(jf)
        except FileNotFoundError:
            self.high_score = 0
        else:
            self.high_score = high_score

    def rest_stats(self):
        self.ship_left = self.ai_setting.ship_limit
        self.game_active = False
        self.score = 0
        self.level = 1
