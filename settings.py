class Settings:
	"""A class to store all settings for Target."""

	def __init__(self):
		"""Initialize the game's static settings."""
		# Screen settings
		self.screen_width = 1000
		self.screen_height = 650
		self.bg_color = (239, 222, 205)

		# Ship settings
		self.ship_left = 3

		# Bullet settings
		self.bullet_height = 3
		self.bullet_width = 15
		self.bullet_color = (60, 60, 60)
		self.bullet_allowed = 3

		# How quickly the block point values increase
		self.score_scale = 1.5

		# How quickly the game speeds up
		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.block_speed = 3.0
		self.ship_speed = 2.0
		self.bullet_speed = 5.5

		# Block direction of 1 represents down and -1 otherwise.
		self.block_direction = 1

		# Scoring
		self.block_points = 20


	def increase_speed(self):
		"""Increase speed settings."""
		self.block_speed *= self.speedup_scale
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale

		self.block_points = int(self.block_points * self.score_scale)
