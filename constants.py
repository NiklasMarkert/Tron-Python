from PyQt5.QtCore import Qt
from enum import Enum

#Board
BOARD_WIDTH = 90    #Breite des Boards (Felder)
BOARD_HEIGHT = 60   #Höhe des Boards (Felder)
FIELD_SIZE = 10     #Groesse der Felder auf dem Board (Pixel)


#Farben
BLUE = [0x00A7B5, 0x00DEF0]
PINK = [0xD500C1, 0xFE54EE]
RED = [0xE30B00, 0xFE352B]
GREEN = 0x53F302


#Fenstergrößen
MENU_WINDOW_WIDTH = 900
MENU_WINDOW_HEIGHT = 600

OPTIONS_WINDOW_WIDTH = 700
OPTIONS_WINDOW_HEIGHT = 500

BOARD_WINDOW_WIDTH = BOARD_WIDTH * FIELD_SIZE
BOARD_WINDOW_HEIGHT = BOARD_HEIGHT * FIELD_SIZE


#Fahrtrichtungen
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


#Tastaturbefehle
PLAYER1_UP = Qt.Key_W
PLAYER1_DOWN = Qt.Key_S
PLAYER1_LEFT = Qt.Key_A
PLAYER1_RIGHT = Qt.Key_D

PLAYER2_UP = Qt.Key_Up
PLAYER2_DOWN = Qt.Key_Down
PLAYER2_LEFT = Qt.Key_Left
PLAYER2_RIGHT = Qt.Key_Right

START = Qt.Key_Space
MENU = Qt.Key_M
PAUSE = Qt.Key_Escape