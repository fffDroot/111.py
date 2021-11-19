import copy
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setMouseTracking(True)
        self.cars = ['1.png', '2.png', '3.png']
        self.carnow = '1.png'
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('CAR')

        self.pixmap = QPixmap(self.carnow)

        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)

        self.show()

    def mouseMoveEvent(self, event):
        if (event.x() in range(0, 250)) and (event.y() in range(0, 250)):
            self.lbl.move(event.x(), event.y())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            template = copy.copy(self.cars)
            template.remove(self.carnow)
            self.carnow = random.choice(template)
            self.pixmap.load(self.carnow)
            self.lbl.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
