"""
The main driver file it will be responsible for handling the players user input and displaying the current gamestate obj
shout some random teacher on the internet who im learning this from thanks :)
"""
import pygame as p
from chess import chess_engine

WIDTH = HEIGHT = 512
DIMENSION = 8 #chess board is 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 60 #for anim
IMAGES = {}
