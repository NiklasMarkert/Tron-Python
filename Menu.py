from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys 

class Menu:
    def __init__(self):
        app = QApplication(sys.argv)
        win = QMainWindow()
        #win.top = 1000
        win.resize(1200,900)
        win.setWindowTitle("Menu")

        win.show()
       
        sys.exit(app.exec_())

m = Menu()