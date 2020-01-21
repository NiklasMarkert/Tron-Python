from PyQt5.QtWidgets import QMainWindow, QPushButton
import constants as c

class Options(QMainWindow):

    def back_menu(self):
        self.close()
        self.parent().show()

    def add_select(self, text, fkt):
        button = QPushButton(text, self)
        button.move(10, 10)
        button.resize(120, 40)
        button.clicked.connect(fkt)

    def __init__(self, parent):
        super(Options, self).__init__(parent)
        self.setWindowTitle('Tron')
        self.resize(c.OPTIONS_WINDOW_WIDTH, c.OPTIONS_WINDOW_HEIGHT)
        self.add_select('< Back to Menu', self.back_menu)
