
# This class tracks the statistics for the game
class GameStats:
    # Initializes statistics
    def __init__(self, ai_game):
        # High score should never be reset
        self.high_score = 0

        self.settings = ai_game.settings
        self.reset_stats()

        # Start alien invasion in an inactive state
        self.game_active = False

    
    # Initializes stats that can change during game
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1