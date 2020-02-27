# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *

import final_all
# class Btn(QPushButton):
#     clicked = pyqtSignal(list)
#     def mousePressEvent(self, *args, **kwargs):
#         pass

class Ui_fir(object):
    def setupUi(self, fir):
        fir.setObjectName("fir")
        fir.resize(588, 381)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/window_icon/favicon-20191211100205340.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fir.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(fir)
        self.centralwidget.setObjectName("centralwidget")
        self.begin = QtWidgets.QPushButton(self.centralwidget)
        self.begin.setGeometry(QtCore.QRect(440, 300, 75, 23))
        self.begin.setObjectName("begin")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 160, 505, 78))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.x0 = QtWidgets.QLineEdit(self.layoutWidget)
        self.x0.setObjectName("x0")
        self.gridLayout.addWidget(self.x0, 0, 1, 1, 1)
        self.y0 = QtWidgets.QLineEdit(self.layoutWidget)
        self.y0.setObjectName("y0")
        self.gridLayout.addWidget(self.y0, 0, 2, 1, 1)
        self.z0 = QtWidgets.QLineEdit(self.layoutWidget)
        self.z0.setObjectName("z0")
        self.gridLayout.addWidget(self.z0, 0, 3, 1, 1)
        self.x1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.x1.setObjectName("x1")
        self.gridLayout.addWidget(self.x1, 1, 1, 1, 1)
        self.y1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.y1.setObjectName("y1")
        self.gridLayout.addWidget(self.y1, 1, 2, 1, 1)
        self.z1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.z1.setObjectName("z1")
        self.gridLayout.addWidget(self.z1, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.x_deta = QtWidgets.QLineEdit(self.layoutWidget)
        self.x_deta.setObjectName("x_deta")
        self.horizontalLayout.addWidget(self.x_deta)
        self.y_deta = QtWidgets.QLineEdit(self.layoutWidget)
        self.y_deta.setObjectName("y_deta")
        self.horizontalLayout.addWidget(self.y_deta)
        self.z_deta = QtWidgets.QLineEdit(self.layoutWidget)
        self.z_deta.setObjectName("z_deta")
        self.horizontalLayout.addWidget(self.z_deta)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 50, 494, 50))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.lenth = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lenth.setText("")
        self.lenth.setObjectName("lenth")
        self.gridLayout_2.addWidget(self.lenth, 0, 1, 1, 1)
        self.wedth = QtWidgets.QLineEdit(self.layoutWidget1)
        self.wedth.setObjectName("wedth")
        self.gridLayout_2.addWidget(self.wedth, 1, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.w = QtWidgets.QLineEdit(self.layoutWidget1)
        self.w.setObjectName("w")
        self.gridLayout_3.addWidget(self.w, 0, 1, 1, 1)
        self.h = QtWidgets.QLineEdit(self.layoutWidget1)
        self.h.setObjectName("h")
        self.gridLayout_3.addWidget(self.h, 1, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_3)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(50, 270, 121, 48))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.direction_num = QtWidgets.QLineEdit(self.layoutWidget2)
        self.direction_num.setObjectName("direction_num")
        self.gridLayout_4.addWidget(self.direction_num, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")
        fir.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(fir)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        fir.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(fir)
        self.statusbar.setObjectName("statusbar")
        fir.setStatusBar(self.statusbar)
        self.zu_path = QtWidgets.QAction(fir)
        self.zu_path.setObjectName("zu_path")
        self.menuFile.addAction(self.zu_path)
        self.menubar.addAction(self.menuFile.menuAction())
        self.label_4.setBuddy(self.x0)
        self.label_6.setBuddy(self.x_deta)
        self.label_5.setBuddy(self.lenth)
        self.label_2.setBuddy(self.w)
        self.label.setBuddy(self.direction_num)
        self.label_3.setBuddy(self.lineEdit)

        rightclicked = QtCore.pyqtSignal(list)
        self.retranslateUi(fir)
        self.begin.clicked.connect(fir.begin_cal)

        self.zu_path.triggered.connect(fir.msg)



        # self.lenth.textChanged['QString'].connect(data_changed)
        # self.w.textChanged['QString'].connect(data_changed)
        # self.wedth.textEdited['QString'].connect(data_changed)
        # self.h.textEdited['QString'].connect(data_changed)
        # self.x0.textChanged['QString'].connect(data_changed)
        # self.y0.textEdited['QString'].connect(data_changed)
        # self.z0.textEdited['QString'].connect(data_changed)
        # self.x1.textChanged['QString'].connect(data_changed)
        # self.y1.textChanged['QString'].connect(data_changed)
        # self.z1.textChanged['QString'].connect(data_changed)
        # self.x_deta.textEdited['QString'].connect(data_changed)
        # self.y_deta.textChanged['QString'].connect(data_changed)
        # self.z_deta.textChanged['QString'].connect(data_changed)
        # self.direction_num.textEdited['QString'].connect(data_changed)
        # self.lineEdit.textChanged['QString'].connect(data_changed)
        self.pushButton.clicked.connect(fir.ensure)
        QtCore.QMetaObject.connectSlotsByName(fir)

    def retranslateUi(self, fir):
        _translate = QtCore.QCoreApplication.translate
        fir.setWindowTitle(_translate("fir", "火焰三维测量"))
        self.begin.setText(_translate("fir", "开始计算"))
        self.label_4.setText(_translate("fir", "三维离散点起始"))
        self.label_6.setText(_translate("fir", "三维离散点步长"))
        self.label_5.setText(_translate("fir", "图片尺寸（长/宽）"))
        self.label_2.setText(_translate("fir", "棋盘格规格（x/y）"))
        self.label.setText(_translate("fir", "方向数目"))
        self.label_3.setText(_translate("fir", "比例尺"))
        self.pushButton.setText(_translate("fir", "确定参数"))
        self.menuFile.setTitle(_translate("fir", "文件"))
        self.zu_path.setText(_translate("fir", "打开"))







class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()


    def msg(self):
        self.directory1 = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "./")  # 起始路径
        print(self.directory1)
        # fileName1, filetype = QFileDialog.getOpenFileName(self,
        #                                                   "选取文件",
        #                                                   "./",
        #                                                   "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
        # print(fileName1, filetype)
        #
        # files, ok1 = QFileDialog.getOpenFileNames(self,
        #                                           "多文件选择",
        #                                           "./",
        #                                           "All Files (*);;Text Files (*.txt)")
        # print(files, ok1)
        #
        # fileName2, ok2 = QFileDialog.getSaveFileName(self,
        #                                              "文件保存",
        #                                              "./",
        #                                              "All Files (*);;Text Files (*.txt)")

    def begin_cal(self):
        # signal_begin_int = map(eval,signal_begin)
        # final_all.begin_cal([
        #     ui.direction_num.text(), ui.w.text(), ui.h.text(), ui.lenth.text(), ui.wedth.text(), ui.x_deta.text(),
        #     ui.y_deta.text(), ui.z_deta.text(),
        #     ui.x0.text(), ui.x1.text(), ui.y0.text(), ui.y1.text(), ui.z0.text(), ui.z1.text()
        # ])
        final_all.begin_cal(['4', '6', '9', '640', '480', '0.2', '0.2', '0.2', '-5', '6', '0', '30', '-5', '6'],
                            fir.directory1)
    # signal_begin = []
    # def data_changed():
    #     signal_begin = [
    #         ui.direction_num.text(), ui.w.text(), ui.h.text(), ui.lenth.text(), ui.wedth.text(), ui.x_deta.text(),
    #         ui.y_deta.text(), ui.z_deta.text(),
    #         ui.x0.text(), ui.x1.text(), ui.y0.text(), ui.y1.text(), ui.z0.text(), ui.z1.text()
    #     ]
    #     print(signal_begin)
    # signal_begin_int = list(map(eval, signal_begin))
    # print(signal_begin_int)
    # sys.exit()
    def ensure(self):
        print("aaa")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fir = MyWindow()
    ui = Ui_fir()
    ui.setupUi(fir)
    fir.show()

    sys.exit(app.exec_())
