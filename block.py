import pygame

class Block:
	"""A class to represent a single block."""
	def __init__(self, t_game):
		"""Initialize the block and set its starting position."""

		self.screen = t_game.screen
		self.settings = t_game.settings
		self.screen_rect = self.screen.get_rect()

		# Load the block image and set its rect attribute.
		self.image = pygame.image.load('images/block(2).bmp')
		self.rect = self.image.get_rect()

		# start block near the center right of the screen.
		self.rect.right = self.screen_rect.right
		self.rect.centery = self.settings.screen_height / 2

		# store the block exact vertical position.
		self.y = float(self.rect.y)


	def update(self):
		"""Move the block up or down."""
		self.y += (self.settings.block_speed * self.settings.block_direction)
		self.rect.y = self.y


	def check_edges(self):
		"""Return True if block is at edge of screen."""
		if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0:
			return True

	def place_center(self):
		"""Place the ship vertically center on the right edge."""
		self.rect.right = self.screen_rect.right
		self.rect.centery = self.settings.screen_height / 2
		self.y = float(self.rect.y)


	def blitme(self):
		# blit means to copy graphics from one image to another
		self.screen.blit(self.image, self.rect)


