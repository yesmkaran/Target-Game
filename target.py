import sys
import pygame
from block import Block
from ship import Ship
from bullet import Bullet
from button import Button
from game_stats import GameStats
from settings import Settings
from scoreboard import Scoreboard

class Target:
	"""Overall class to manage game assets and behavior"""

	def __init__(self):
		"""Initialie the game, and create game resources."""

		# Initializes the background settings that Pygame needs to work properly
		pygame.init()

		self.settings = Settings()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption('Target')

		self.block = Block(self)
		self.ship = Ship(self)
		# Create an instance to store game statistics.
		self.stats = GameStats(self)
		self.sb = Scoreboard(self)

		self.bullets = pygame.sprite.Group()

		# Make the play button.
		self.play_button = Button(self, 'Play')



	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()

			if self.stats.game_active:
				self._update_block()
				self.ship.update()
				self._update_bullet()
				
			self._update_screen()



	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				with open('high_score.txt', 'w') as f:
					f.write(str(self.stats.high_score))
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)
				


	def _check_play_button(self, mouse_pos):
		"""Start a new game when the player clicks Play."""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			# Reset the game statistics
			self.settings.initialize_dynamic_settings()
			# Reset the statistics
			self.stats.reset_stats()
			self.stats.game_active = True

			self.sb.prep_score()
			self.sb.prep_ships()
			self.sb.prep_level()

			self.bullets.empty()

			# Place the block in center and the ship at the left bottom.
			self.block.place_center()
			self.ship.left_bottom_ship()
			# Hide the mouse cursor.
			pygame.mouse.set_visible(False)



	def _check_keydown_events(self, event):
		"""Respond to keypresses."""
		if event.key == pygame.K_q:
			# Store the high score before closing the game.
			with open('high_score.txt', 'w') as f:
				f.write(str(self.stats.high_score))
			sys.exit()
		elif event.key == pygame.K_d:
			self.ship.moving_up = True
		elif event.key == pygame.K_m:
			self.ship.moving_down = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()


	def _check_keyup_events(self, event):
		"""Respond to key releases."""
		if event.key == pygame.K_d:
			self.ship.moving_up = False
		elif event.key == pygame.K_m:
			self.ship.moving_down = False



	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group."""
		if len(self.bullets) < self.settings.bullet_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)



	def _update_bullet(self):
		"""Update position of bullets and get rid of old bullets."""
		self.bullets.update()

		# Get rid of bullets that have disappeared.
		for bullet in self.bullets.copy():
			if bullet.rect.right >= self.settings.screen_width:
				self.bullets.remove(bullet)

				if self.stats.ship_left > 0:
					# Decrement ships left, and update scoreboard
					self.stats.ship_left -= 1

					self.sb.prep_ships()

				else:
					self.stats.game_active = False
					# Reset the stats
					self.stats.reset_stats()
					# Make cursor visible
					pygame.mouse.set_visible(True)

		self._check_bullet_block_collision()
		


	def _check_bullet_block_collision(self):

		# Check for any bullets that have hit block.
		# If so, get rid of the bullet and increment the score.
		# (sprite, group) -> returns the first bullet that has collided with the block
		bullet = pygame.sprite.spritecollideany(self.block, self.bullets)
		if bullet:
			self.stats.bullet_hit_count += 1
			self.stats.score += (self.settings.block_points)
			self.bullets.remove(bullet)
			self.sb.prep_score()
			self.sb.check_high_score()

		if self.stats.bullet_hit_count == 3:
			self._start_new_level()
	


	def _start_new_level(self):
		"""Start a new level."""
		self.bullets.empty()
		self.settings.increase_speed()
		self.stats.bullet_hit_count = 0

		# Increase level.
		self.stats.level += 1
		self.sb.prep_level()



	def _update_block(self):
		"""Check if the block is at the edge,
		and then update the position of the block"""
		if self.block.check_edges():
			self.settings.block_direction *= -1

		self.block.update()



	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""

		# Redraw the screen during each pass through the loop.
		self.screen.fill(self.settings.bg_color)
		self.block.blitme()
		self.ship.blitme()

		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		if not self.stats.game_active:
			self.play_button.draw_button()

		self.sb.show_score()

		# Make the most recently drawn screen visible.
		pygame.display.flip()



if __name__ == '__main__':
	# Make an instance of the class and execute the game.
	t = Target()
	t.run_game()
