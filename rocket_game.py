import sys

import pygame

from settings import Settings
from rocket import Rocket

class RocketGame:
	"""Overall class to manage the game assets and behavior"""

	def __init__ (self):
		"""Initialize the game and create the game resources."""

		pygame.init()
		self.bg = pygame.image.load("images/space.bmp")
		self.settings = Settings()
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption = ("Space Rocket!")

		self.rocket = Rocket(self)

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			#Watch for keyboard and mouse events.
			self._check_events()

			#Update the rocket's position.
			self.rocket.update()

			#Redraw the screen during each loop.
			self._update_screen()
	
	def _check_events(self):
		"""Respond to keypresses and mouse events"""
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					self._check_keydown_events(event)
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)

	def _check_keydown_events(self,event):
		"""Respond to key presses."""
		if event.key == pygame.K_RIGHT:
			self.rocket.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.rocket.moving_left = True
		#Up and down press detection added:
		elif event.key == pygame.K_UP:
			self.rocket.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.rocket.moving_down = True	
		elif event.key == pygame.K_q:
			sys.exit()
		
	def _check_keyup_events(self,event):
		"""Respond to key releases."""
		if event.key== pygame.K_RIGHT:
			self.rocket.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.rocket.moving_left = False
		#Up and down press release detection added:
		elif event.key == pygame.K_UP:
			self.rocket.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.rocket.moving_down = False

	def _update_screen(self):
		"""Update images on the screen and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		#Add background picture.
		self.screen.blit(self.bg, (0, 0))
		self.rocket.blitme()
			
		#Make the most recently drawn screen visible.
		pygame.display.flip()

if __name__ == '__main__':
	#Make a game instance, and run the game.
	rg = RocketGame()
	rg.run_game()


