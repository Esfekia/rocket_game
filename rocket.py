import pygame

class Rocket:
	"""A Class to manage the rocket."""

	def __init__ (self, rg_game):
		"""Initialize the rocket and set its starting position."""
		self.screen = rg_game.screen
		self.settings = rg_game.settings
		self.screen_rect = rg_game.screen.get_rect()

		#Load the rocket image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		#Start each new rocket at the midleft of the screen.
		self.rect.midleft = self.screen_rect.midleft

		#Store a decimal value for the rocket's horizontal position.
		self.x = float(self.rect.x)
		#Store a decimal value for the rocket's vertical position.
		self.y = float(self.rect.y)

		#Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update the rocket's position based on the movement flags."""

		#Update the rocket's x value, not the rect.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.rocket_speed

		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.rocket_speed

		#Update the rocket's y value, not the rect.
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.rocket_speed

		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.rocket_speed	

		#Update rect object from self.x
		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		"""Draw the rocket at its current location."""
		self.screen.blit(self.image, self.rect)