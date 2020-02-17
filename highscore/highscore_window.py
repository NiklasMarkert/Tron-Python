from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt
from constants import WindowSize as w, Colors as c

class HighscoreWindow(QMainWindow):

    def back_menu(self):
        self.close()
        self.parent().show()

    def add_back(self):
        button = QPushButton('< Back to Menu', self)
        button.move(10, 10)
        button.resize(120, 40)
        button.clicked.connect(self.back_menu)

    def add_titel(self):
        titel = QLabel('Highscores', self)
        titel.resize(w.HIGHSCORE_WINDOW_WIDTH, 80)
        font = titel.font()
        font.setBold(True)
        font.setPointSize(40)
        titel.setFont(font)
        titel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        titel.move(0, 0)

    def add_background(self):
        """ Setzt den weißen Hintergrund
        """
        bg = QLabel('', self)
        bg.resize(w.HIGHSCORE_WINDOW_WIDTH, w.HIGHSCORE_WINDOW_HEIGHT)
        bg.move(0,0)
        bg.setStyleSheet('QLabel {background-color : white;}')

    def add_rank(self, pos, rank, color):
        rank = QLabel(str(rank) + '.', self)
        rank.resize(60, 50)
        font = rank.font()
        font.setBold(True)
        font.setPointSize(25)
        rank.setFont(font)
        rank.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        rank.setStyleSheet('QLabel { color : '+ color + '; }')
        rank.move(180, pos)

    def add_name(self, pos, color):
        label = QLabel('---', self)
        label.resize(390, 50)
        font = label.font()
        font.setBold(True)
        font.setPointSize(25)
        label.setFont(font)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        label.setStyleSheet('QLabel { color : '+ color + '; }')
        label.move(250, pos)
        return label

    def add_score(self, pos, color):
        label = QLabel('--', self)
        label.resize(60, 50)
        font = label.font()
        font.setBold(True)
        font.setPointSize(25)
        label.setFont(font)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        label.setStyleSheet('QLabel { color : '+ color + '; }')
        label.move(650, pos)
        return label

    def set_scores(self):
        """ Schreibt die 10 besten Scores in die dafür vorgesehenen Labels
        """
        top10 = self.highscore.get_scores(10)
        for i in range(0,len(top10)):
            self.names[i].setText(top10[i].name)
            self.scores[i].setText(str(top10[i].score))

    def __init__(self, parent, highscore):
        super(HighscoreWindow, self).__init__(parent)
        self.setWindowTitle('Tron')
        self.setFixedSize(w.HIGHSCORE_WINDOW_WIDTH, w.HIGHSCORE_WINDOW_HEIGHT)
        self.highscore = highscore
        self.add_background()
        self.add_titel()
        self.add_back()
        self.names = []
        self.scores = []
        for i in range(1, 11):
            color = 'black'
            if i == 1:  # 1. Platz wird in Gold geschrieben
                color = c.GOLD
            if i == 2:  # 2. Platz wird in Silber geschrieben
                color = c.SILVER
            if i == 3:  # 3. Platz wird in Bronze geschrieben
                color = c.BRONZE
            self.add_rank(90 + (i-1)*50, i, color)
            self.names = self.names + [self.add_name(90 + (i-1)*50, color)]
            self.scores = self.scores + [self.add_score(90 + (i-1)*50, color)]
        self.set_scores()
