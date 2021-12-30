class Settings:
	"""A Class to store all settings for Rocket Game."""

	def __init__ (self):
		"""Initialize the game's settings."""
		
		# Screen settings
		self.screen_width = 960
		self.screen_height = 540
		self.bg_color = (230,230,230)

		#Rocket settings
		self.rocket_speed = 1.5

		#Bullet settings
		self.bullet_speed = 1.5
		self.bullet_width = 15
		self.bullet_height = 4
		self.bullet_color = (252.15.192)
		self.bullets_allowed = 3

		#Alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10

		#Fleet direction of 1 represents up, -1 represents down.
		self.fleet_direction = 1