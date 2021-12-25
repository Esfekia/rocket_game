class Settings:
	"""A Class to store all settings for Rocket Game."""

	def __init__ (self):
		"""Initialize the game's settings."""
		
		# Screen settings
		self.screen_width = 960
		self.screen_height = 540
		self.bg_color = (230,230,230)

		#Rocket settings
		self.rocket_speed = 1.0