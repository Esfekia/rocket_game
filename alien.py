import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
	"""A class to represent a single alien in the fleet."""

	def __init__(self, rg_game):
		"""Initialize the alien and set its starting position."""
		super().__init__()
		self.screen = rg_game.screen
		self.settings = rg_game.settings

		#Load the alien image and set its rect attribute.
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		#Start each new alien near the top right of the screen.
		self.rect.left = self.screen.get_rect().right

		#The farthest down the scren we will place the alien is
		#the height of the screen, minus the height of the alien.
		alien_top_max = self.settings.screen_height - self.rect.height
		self.rect.top = randint (0, alien_top_max)

		#Store the alien's exact horizontal position.
		self.x = float(self.rect.x)

	def check_edges(self):
		"""Return True if alien is at edge of screen."""
		screen_rect = self.screen.get_rect()
		if self.rect.bottom >=screen_rect.bottom or self.rect.top < 0:
			return True

	def update (self):
		"""Move the alien up or down."""
		self.y+= (self.settings.alien_speed * 
			self.settings.fleet_direction)
		self.rect.y = self.y