import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	
	def __init__(self, ai_settings, screen):
		'''Инициализирует корабль и задает его нач. позицию.'''
		super().__init__()
		
		self.screen = screen
		self.ai_settings = ai_settings
		
		#загрузка изображения корабля и получение прямоугоьника
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		#Каждый новый корабль появляется у нижнего края экрана
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#сохранение вещественной координаты центра корабля
		self.center = float(self.rect.centerx)
		
		#флаги перемещения.
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		'''Обновляет позицию корабля с учетом флага.'''
		#обновляет атрибут center, не rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		
		#обновляет атрибут rect на основании self.center
		self.rect.centerx = self.center
		
	def blitme(self):
		'''Рисует корабль в текущей позиции'''
		self.screen.blit(self.image, self.rect)
		
	def center_ship(self):
		'''Размещает корабль в центре нижней стороны'''	
		self.center = self.screen_rect.centerx
