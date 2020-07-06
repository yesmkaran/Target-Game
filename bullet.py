import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
	"""A class to manage bullets fired from the ship."""

	def __init__(self, t_game):
		"""Create a bullet object at the ship's current position"""
		super().__init__()
		self.screen = t_game.screen
		self.settings = t_game.settings

		# Create a bullet rect at (0,0) and then set correct position
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.centery = t_game.ship.rect.centery

		# Store the bullet's position as a decimal value
		self.x = float(self.rect.x)


	def update(self):
		"""Move the bullet across the screen."""
		# Update the decimal position of the bullet.
		self.x += (self.settings.bullet_speed)
		# Update the rect position
		self.rect.x = self.x


	def draw_bullet(self):
		"""Draw the bullet to the screen"""
		pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)

