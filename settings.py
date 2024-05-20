
# This class stores all settings for the game
class Settings:
    # Initialize game settings
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.3

        # How quickly alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    # Initializes settings that change throughout the game
    def initialize_dynamic_settings(self):
        self.ship_speed = 3
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1            # 1 represents right, -1 represents left

        # Scoring
        self.alien_points = 50


    # Increases speed settings
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)


