import sys
from PyQt5.QtWidgets import QApplication
import game
import menu

if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = menu.Menu()
    m.show()
    sys.exit(app.exec_())