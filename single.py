# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'single.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SingleWindow(object):
    def setupUi(self, SingleWindow):
        SingleWindow.setObjectName("SingleWindow")
        SingleWindow.resize(743, 527)
        self.centralwidget = QtWidgets.QWidget(SingleWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(60, 380, 54, 12))
        self.label_15.setObjectName("label_15")
        self.LineDisplayGB = QtWidgets.QGroupBox(self.centralwidget)
        self.LineDisplayGB.setGeometry(QtCore.QRect(210, 120, 161, 221))
        self.LineDisplayGB.setObjectName("LineDisplayGB")
        self.LineDisplayGB_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.LineDisplayGB_2.setGeometry(QtCore.QRect(40, 120, 161, 221))
        self.LineDisplayGB_2.setObjectName("LineDisplayGB_2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 400, 160, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.volome = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.volome.setReadOnly(True)
        self.volome.setObjectName("volome")
        self.verticalLayout_4.addWidget(self.volome)
        self.area = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.area.setReadOnly(True)
        self.area.setObjectName("area")
        self.verticalLayout_4.addWidget(self.area)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 501, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_zu_path = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_zu_path.setObjectName("label_zu_path")
        self.horizontalLayout.addWidget(self.label_zu_path)
        self.lineEdit_zu_path = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_zu_path.setReadOnly(False)
        self.lineEdit_zu_path.setObjectName("lineEdit_zu_path")
        self.horizontalLayout.addWidget(self.lineEdit_zu_path)
        self.pushButton_zu_path = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_zu_path.setObjectName("pushButton_zu_path")
        self.horizontalLayout.addWidget(self.pushButton_zu_path)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 120, 54, 12))
        self.label_4.setObjectName("label_4")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(600, 410, 101, 80))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ensure = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ensure.setObjectName("ensure")
        self.verticalLayout_5.addWidget(self.ensure)
        self.begin_cal = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.begin_cal.setObjectName("begin_cal")
        self.verticalLayout_5.addWidget(self.begin_cal)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(460, 150, 241, 241))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_6.addWidget(self.label_13)
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_6.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_6.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_6.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_6.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_6.addWidget(self.label_21)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.w_h = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.w_h.setObjectName("w_h")
        self.verticalLayout_7.addWidget(self.w_h)
        self.l_w = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.l_w.setObjectName("l_w")
        self.verticalLayout_7.addWidget(self.l_w)
        self.x0_y0_z0 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.x0_y0_z0.setObjectName("x0_y0_z0")
        self.verticalLayout_7.addWidget(self.x0_y0_z0)
        self.x_deta_y_deta_z_deta = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.x_deta_y_deta_z_deta.setObjectName("x_deta_y_deta_z_deta")
        self.verticalLayout_7.addWidget(self.x_deta_y_deta_z_deta)
        self.direction_num = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.direction_num.setObjectName("direction_num")
        self.verticalLayout_7.addWidget(self.direction_num)
        self.yuzhi = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.yuzhi.setObjectName("yuzhi")
        self.verticalLayout_7.addWidget(self.yuzhi)
        self.scal_number = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.scal_number.setObjectName("scal_number")
        self.verticalLayout_7.addWidget(self.scal_number)
        self.te_zheng = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.te_zheng.setObjectName("te_zheng")
        self.verticalLayout_7.addWidget(self.te_zheng)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        SingleWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SingleWindow)
        self.statusbar.setObjectName("statusbar")
        SingleWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SingleWindow)
        self.ensure.clicked.connect(SingleWindow.ensure)
        self.begin_cal.clicked.connect(SingleWindow.begin)
        self.pushButton_zu_path.clicked.connect(SingleWindow.file_dir)
        QtCore.QMetaObject.connectSlotsByName(SingleWindow)

    def retranslateUi(self, SingleWindow):
        _translate = QtCore.QCoreApplication.translate
        SingleWindow.setWindowTitle(_translate("SingleWindow", "单幅火焰处理"))
        self.label_15.setText(_translate("SingleWindow", "结果："))
        self.LineDisplayGB.setTitle(_translate("SingleWindow", "火焰三维图像"))
        self.LineDisplayGB_2.setTitle(_translate("SingleWindow", "单方向火焰图像/示例"))
        self.label_11.setText(_translate("SingleWindow", "体积(m3)"))
        self.label_12.setText(_translate("SingleWindow", "表面积(m2)"))
        self.volome.setText(_translate("SingleWindow", "待计算..."))
        self.area.setText(_translate("SingleWindow", "待计算..."))
        self.label_zu_path.setText(_translate("SingleWindow", "火焰文件所在路径"))
        self.lineEdit_zu_path.setText(_translate("SingleWindow", "C:/Users/yhstc/Desktop/90"))
        self.pushButton_zu_path.setText(_translate("SingleWindow", "选择"))
        self.label_4.setText(_translate("SingleWindow", "参数设置"))
        self.ensure.setText(_translate("SingleWindow", "确定参数"))
        self.begin_cal.setText(_translate("SingleWindow", "开始计算"))
        self.label_13.setText(_translate("SingleWindow", "棋盘规格（x/y）"))
        self.label_16.setText(_translate("SingleWindow", "图片尺寸（长/宽）"))
        self.label_17.setText(_translate("SingleWindow", "三维起始点"))
        self.label_18.setText(_translate("SingleWindow", "三维步长"))
        self.label_19.setText(_translate("SingleWindow", "方向数目"))
        self.label_20.setText(_translate("SingleWindow", "阈值"))
        self.label_21.setText(_translate("SingleWindow", "比例尺"))
        self.label.setText(_translate("SingleWindow", "实验文件夹特征"))
        self.w_h.setText(_translate("SingleWindow", "6/9"))
        self.l_w.setText(_translate("SingleWindow", "1920/1200"))
        self.x0_y0_z0.setText(_translate("SingleWindow", "-5/5/-4/80/-5/5"))
        self.x_deta_y_deta_z_deta.setText(_translate("SingleWindow", "30/150/30"))
        self.direction_num.setText(_translate("SingleWindow", "3"))
        self.yuzhi.setText(_translate("SingleWindow", "10"))
        self.scal_number.setText(_translate("SingleWindow", "1"))
        self.te_zheng.setText(_translate("SingleWindow", "kw"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SingleWindow = QtWidgets.QMainWindow()
    ui = Ui_SingleWindow()
    ui.setupUi(SingleWindow)
    SingleWindow.show()
    sys.exit(app.exec_())
