import sys

from PyQt5.QtWidgets import QApplication
from Controller.controller import Controller

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Controller()
    window.show()
    sys.exit(app.exec_())