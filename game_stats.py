
class GameStats:
	"""Track statistics for Target."""

	def __init__(self, t_game):
		"""Initialize statistics"""
		self.settings = t_game.settings
		# Start Target in an active state.
		self.game_active = False

		# High score should never be reset.
		try:
			with open('high_score.txt') as f:
				self.high_score = f.read()
		except FileNotFoundError:
			self.high_score = 0

		self.reset_stats()


	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ship_left = self.settings.ship_left
		self.bullet_hit_count = 0
		self.score = 0
		self.level = 1

