import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	'''Класс, представляющий одного пришельца.'''
	def __init__(self, ai_settings, screen):
		'''Инициализирует пришельца и задает его начальную позицию.'''
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		#загрузка изображения пришельца и получение прямоугольника:
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		#каждый новый пришелец появляется в левом верхнем углу экрана.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#сохранение точной позиции пришельца
		self.x = float(self.rect.x)
	
	def blitme(self):
		'''Выводит пришельца в текущем положении.'''
		self.screen.blit(self.image, self.rect)

	def check_edges(self):
		'''Возвращает True, если пришелец находится у края экрана.'''
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
			
	def update(self):
		'''Перемещает пришельца вправо или влево.'''
		self.x += (self.ai_settings.alien_speed_factor *
						self.ai_settings.fleet_direction)
		self.rect.x = self.x
		
		

