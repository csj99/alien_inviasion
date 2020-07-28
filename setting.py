class Settings():

    def __init__(self):
        self.Screen_width = 1200
        self.Screen_hight = 600
        self.bg_color = (230,230,230)

        self.ship_limit = 3
        self.ship_speed_factor = 1

        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 5

        self.alien_dorp_speed = 3
        self.alien_move_speed = 1
        self.alien_move_dirc = 1

        self.speedup_scale = 1.5
        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        self.ship_speed_factor = 1.1
        self.bullet_speed_factor = 3
        self.alien_dorp_speed = 3
        self.alien_move_speed = 1
        self.alien_move_dirc = 1
        self.alien_point = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_move_speed *= self.speedup_scale
        self.alien_point = int(self.alien_point*self.speedup_scale)