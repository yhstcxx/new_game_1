import sys
from PyQt5.QtWidgets import (QWidget, QSlider,
                             QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QImage
import numpy as np
import cv2
from io import BytesIO

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):


        self.label = QLabel(self)
        pic = cv2.imread(r'C:\Users\yhstc\Desktop\image_18.png')
        pic = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)


        height, width, channel = pic.shape
        bytesPerLine = 3 * width
        label_image = QImage(pic.data, width, height, bytesPerLine, QImage.Format_RGB888)

        # label_image = QImage(pic.data, pic.shape[1], pic.shape[0], QImage.Format_RGB888)


        # self.label.setPixmap(QPixmap(pic))
        self.label.setPixmap(QPixmap(label_image))

        # self.label.setGeometry(160, 40, 150, 150)

        # self.label.move(160, 40)
        self.setGeometry(300, 300,  width, height)
        self.setWindowTitle('QSlider')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())    