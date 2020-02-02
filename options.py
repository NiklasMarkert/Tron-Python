from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
import constants as c

class Options(QMainWindow):

    def test(self):
        print('Hey')

    def add_cbutton(self):
        button = QPushButton('', self)
        button.move(200, 200)
        button.resize(20, 20)
        button.setStyleSheet("background-color: green");
        button.clicked.connect(self.test)
        return button

    def back_menu(self):
        self.close()
        self.parent().show()

    def controls(self):
        self.titel.setText('Controls')

    def colors(self):
        self.titel.setText('Colors')
        self.red.show()


    def add_titel(self):
        text = QLabel('', self)
        text.resize(500, 50)
        font = text.font()
        font.setBold(True)
        font.setPointSize(30)
        text.setFont(font)
        text.move(150, 0)
        return text

    def add_select(self, text, pos, fkt):
        button = QPushButton(text, self)
        button.move(10, pos)
        button.resize(120, 40)
        button.clicked.connect(fkt)

    def __init__(self, parent):
        super(Options, self).__init__(parent)
        self.setWindowTitle('Tron')
        self.setFixedSize(c.OPTIONS_WINDOW_WIDTH, c.OPTIONS_WINDOW_HEIGHT)
        self.add_select('< Back to Menu', 10, self.back_menu)
        self.add_select('Controls' , 80, self.controls)
        self.add_select('Colors', 130, self.colors)
        self.titel = self.add_titel()
        self.red = self.add_cbutton()
        self.red.hide()
        self.controls()

