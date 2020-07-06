import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""A class to manage the ship."""
	def __init__(self, t_game):
		"""Initialize the ship and set its starting position."""
		super().__init__()
		self.screen = t_game.screen
		self.screen_rect = self.screen.get_rect()

		self.settings = t_game.settings
		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/bullet(2).bmp')
		self.rect = self.image.get_rect()

		# Start each new ship at the left bottom of the screen.
		self.rect.bottom = self.screen_rect.bottom

		# Store a decimal value for the ship's horizontal position.
		self.y = float(self.rect.y)

		# Movement flag
		self.moving_up = False
		self.moving_down = False


	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)


	def left_bottom_ship(self):
		"""Place the ship at left bottom of the screen."""
		self.rect.bottom = self.screen_rect.bottom
		self.y = float(self.rect.y)


	def update(self):
		"""Update the ship's position based on the movement flag."""
		# Update the ship's y value, not the rect.
		if self.moving_up and self.rect.top > 0:
			self.y -= (self.settings.ship_speed)
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += (self.settings.ship_speed)

		# Update rect object from self.y
		self.rect.y = self.y