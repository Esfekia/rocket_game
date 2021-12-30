import sys

import pygame

from settings import Settings
from rocket import Rocket
from bullet import Bullet
from alien import Alien

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
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			#Watch for keyboard and mouse events.
			self._check_events()

			#Update the rocket's position.
			self.rocket.update()

			#Update the bullet's position.
			self._update_bullets()

			#Update the Alien's movement.
			self._update_aliens()

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

	def _fire_bullets(self):
		"""Create a new bullet and add it to the bullets group."""
		#First check max bullets allowed in settings.
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Update position of bullets and get rid of old bullets."""
		self.bullets.update()

		#Get rid of old bullets that have disappeared from screen.
		for bullet in self.bullets.copy():
			if bullet.rect.bottom<= 0:
				self.bullets.remove(bullet)

		self._check_bullet_alien_collisions()

	def _check_bullet_alien_collisions(self):
		"""Respond to bullet-alien collisions."""

		#Remove any bullets and aliens that have collided.
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)

		#Check to see if all aliens are dead:
		if not self.aliens:
			#Destroy existing bullets and create new fleet.
			self.bullets.empty()
			self._create_fleet()

	def _update_aliens(self):
		"""First check if the fleet is at an edge,
		Then update the positions of all aliens in the fleet."""
		self._check_fleet_edges()
		self.aliens.update()

	def _create_fleet(self):
		"""Create the fleet of aliens."""

		#Create an alien and find the number of aliens in a column.
		#Spacing between each alien is equal to one alien height.

		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_y = self.settings.screen_height - (2*alien_height)
		number_aliens_y = available_space_y // (2*alien_height)

		#Determine the number of columns that fit on the screen:

		rocket_width = self.rocket.rect.width
		available_space_x = (self.settings.screen_width -
				(3*alien_width) - rocket_width)
		number_columns = available_space_x // (2*alien_width)

		#Create full fleet of aliens.
		for column_number in range(number_columns):
			for alien_number in range(number_aliens_y):
				self._create_alien(alien_number, column_number)

	def _create_alien(self, alien_number, column_number):
		"""Create an alien and place it in the column."""

		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.y =alien_height + 2*alien_height*alien_number
		alien.rect.y = alien.y
		alien.rect.x = alien.rect.width + 2*alien.rect.alien_width * column_number
		self.aliens.add(alien)

	def _check_fleet_edges(self):
		"""Respond if aliens have reached an edge."""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _update_screen(self):
		"""Update images on the screen and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		#Add background picture.
		self.screen.blit(self.bg, (0, 0))
		self.rocket.blitme()

		#Draw the bullets
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		#Draw the aliens
		self.aliens.draw(self.screen)
			
		#Make the most recently drawn screen visible.
		pygame.display.flip()

if __name__ == '__main__':
	#Make a game instance, and run the game.
	rg = RocketGame()
	rg.run_game()


