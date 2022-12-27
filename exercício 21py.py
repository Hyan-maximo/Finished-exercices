# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 20:24:21 2022

@author: Hyan Máximo
"""

import pygame
pygame.init()
pygame.mixer.music.load('wam.mp3')
pygame.mixer.music.play()
pygame.event.wait()
