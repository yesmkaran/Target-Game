import pygame
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
	"""A class to report scoring information."""

	def __init__(self, t_game):
		"""Initialize scorekeeping atrributes."""
		self.t_game = t_game
		self.screen = t_game.screen
		self.screen_rect = self.screen.get_rect()

		self.stats = t_game.stats
		self.settings = t_game.settings

		# Font settings for scoring information.
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 30)

		self.prep_score()
		self.prep_high_score()
		self.prep_ships()
		self.prep_level()


	def prep_score(self):
		"""Turn the score into a rendered image."""
		score_str = round(self.stats.score, -1)
		score_str = "{:,}".format(score_str)
		score_str = "score: {0}".format(score_str)
		self.score_image = self.font.render(score_str, True,
					self.text_color, self.settings.bg_color)

		# Display the score at the top right besides the high score.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.x = (self.settings.screen_width / 2) + 20
		self.score_rect.top = 20


	def prep_high_score(self):
		"""Turn the high score into a rendered image."""
		high_score_str = round(int(self.stats.high_score), -1)
		high_score_str = "{:,}".format(high_score_str)
		high_score_str = "High score: {0}".format(high_score_str)
		self.high_score_image = self.font.render(high_score_str, True,
					self.text_color, self.settings.bg_color)

		# Center the high score at the top of the screen.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.x = (self.settings.screen_width / 2) - self.high_score_rect.width
		self.high_score_rect.top = self.score_rect.top



	def prep_level(self):
		"""Turn the level into a rendered image."""
		level_str = "level: {0}".format(self.stats.level)
		self.level_image = self.font.render(level_str, True,
					self.text_color, self.settings.bg_color)

		# Position the level besides the score.
		self.level_rect = self.level_image.get_rect()
		self.level_rect.x = (self.settings.screen_width / 2) + self.high_score_rect.width + self.level_rect.width
		self.level_rect.top = self.score_rect.top



	def prep_ships(self):
		"""How many ships are left."""
		# Empty group to hold the ship instances
		self.ships = Group()
		for ship_number in range(self.stats.ship_left):
			ship = Ship(self.t_game)
			ship.rect.x = 20 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)


	def check_high_score(self):
		"""Check if the current score is the high score."""
		if self.stats.score > int(self.stats.high_score):
			self.stats.high_score = self.stats.score
			self.prep_high_score()



	def show_score(self):
		"""Draw scores to the screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.ships.draw(self.screen)

