class Settings():
	'''Класс для хранения всех настроек игры Alien Invasion.'''
	
	def __init__(self):
		'''Инициализирует статические настройки игры.'''
		#Параметры экрана:
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		
		#настройки корабля
		self.ship_limit = 3
		
		#Параметры пули:
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3
				
		#Настройки пришельцев.
		self.fleet_drop_speed = 10
		
		#Темп ускорения игры
		self.speedup_scale = 1.1
		
		#Темп роста стоимости пришельцев.
		self.score_scale = 1.5
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		'''Инициализирует настройки, изменяющиеся в ходе игры.'''
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 2
		self.alien_speed_factor = 1
		
		# fleet_direction = 1 обозначает движение вправо; а -1 - влево.
		self.fleet_direction = 1
		
		#подсчет очков
		self.alien_points = 50
	
	def increase_speed(self):
		'''Увеличивает настройки скорости и стоимости пришельцев.'''
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale	
		
		self.alien_points = int(self.alien_points * self.score_scale)
		
		
		
