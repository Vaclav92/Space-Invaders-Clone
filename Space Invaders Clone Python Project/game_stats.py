class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Start Alien Invasion in an active state.
        self.game_active = False # Originally set to True

        # High score should never be reset.
        self.high_score = 0
        
        with open('HighScore.txt') as file_object:
            self.high_score = int(file_object.read()) # Opens the text file 'HighScore.txt' and reads in the file but had to convert to an int - can't believed it worked


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 0
