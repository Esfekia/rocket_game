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
		self.bullet_color = (252,15,192)
		self.bullets_allowed = 3
		
		# Alien settings.
        #  alien_frequency controls how often a new alien appear.s
        #    Higher values -> more frequent aliens. Max = 1.0.
		self.alien_frequency = 0.008
		self.alien_speed = 1.5
