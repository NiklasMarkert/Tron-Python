from PyQt5.QtCore import Qt
from enum import IntEnum, Enum

#Board
class BoardSize:
    BOARD_WIDTH = 90    #Breite des Boards (Felder)
    BOARD_HEIGHT = 60   #Höhe des Boards (Felder)
    FIELD_SIZE = 10     #Groesse der Felder auf dem Board (Pixel)


#Farben
class Colors:
    #für Objekte auf dem Spielfeld
    BLUE = [0x00A7B5, 0x00DEF0]
    PINK = [0xD500C1, 0xFE54EE]
    RED = [0xE30B00, 0xFE352B]
    GREEN = 0x63F701
    ORANGE = 0xFF660E
    YELLOW = 0xC5C200
    PURPLE = 0xC700E1
    BLACK = 0x6D0000
    BLUEGREEN = 0x27AE60

    OBJECT_COLOR = [GREEN, ORANGE, YELLOW, PURPLE, BLACK, BLUEGREEN]


    #für Text
    GOLD = '#FFD700'
    SILVER = '#A9A9A9'
    BRONZE = '#CD7F32'
    GREY = '#9D9D9D'


#Fenstergrößen
class WindowSize:
    MENU_WINDOW_WIDTH = 900
    MENU_WINDOW_HEIGHT = 600

    OPTIONS_WINDOW_WIDTH = 800
    OPTIONS_WINDOW_HEIGHT = 500

    HIGHSCORE_WINDOW_WIDTH = 900
    HIGHSCORE_WINDOW_HEIGHT = 600

    BOARD_WINDOW_WIDTH = BoardSize.BOARD_WIDTH * BoardSize.FIELD_SIZE
    BOARD_WINDOW_HEIGHT = BoardSize.BOARD_HEIGHT * BoardSize.FIELD_SIZE


#Fahrtrichtungen
class Directions(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

AI_DIR = [Directions.NORTH, Directions.WEST, Directions.EAST]

#Spiel Modi
class Modes(Enum):
    AI = 1
    MULTIPLAYER = 2
    POWER_UP = 3
    SNAKE = 4

#Power Up Typen
class Types(IntEnum):
    PLUS_LENGTH = 0
    MINUS_LENGTH = 1
    SELFDMG_OF = 2
    DESTROY_TAIL = 3
    LOSE = 4
    BORDERDMG_OF = 5

TYPE_TIMER = [0, 300, 500, 300, 200, 500]       # Speichert, wie lange ein Objekt eines bestimmten Typen auf dem Board
                                                # Board bleibt, bis es verschwindet; Typ Plus_Length verschwindet nie von allein

#Startpositionen
class StartingPositions:
    BOARD_HEIGHT = BoardSize.BOARD_HEIGHT
    BOARD_WIDTH = BoardSize.BOARD_WIDTH

    START_X_1P = int(BOARD_WIDTH / 2)
    START_Y_1P = int(BOARD_HEIGHT / 2)

    START_X_2P_1 = int(BOARD_WIDTH / 3)
    START_Y_2P_1 = int(BOARD_HEIGHT / 2)
    START_X_2P_2 = int((BOARD_WIDTH / 3) * 2)
    START_Y_2P_2 = int(BOARD_HEIGHT / 2)

    START_X = [0, 0, 0, 0]
    START_Y = [0, 0, 0, 0]
    START_X[0] = int(BOARD_WIDTH / 5)
    START_Y[0] = int(BOARD_HEIGHT / 4)
    START_X[1] = int((BOARD_WIDTH / 5) * 4)
    START_Y[1] = int((BOARD_HEIGHT / 4) * 3)
    START_X[2] = int((BOARD_WIDTH / 5) * 4)
    START_Y[2] = int(BOARD_HEIGHT / 4)
    START_X[3] = int(BOARD_WIDTH / 5)
    START_Y[3] = int((BOARD_HEIGHT / 4) * 3)


#Tastaturbefehle
class Keys:
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

#Spieleinstellungen
class Options:
    #Spielername
    PLAYER_NAME = 'Player1'

    #Anzahl der Bots im AI-Mode
    AMOUNT_BOTS = 1

    #Multiplayer / KI-Gegner im Power-Up Mode
    MULTIPLAYER_PU = True