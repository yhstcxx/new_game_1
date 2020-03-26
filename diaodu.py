
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QMessageBox,QLabel,QGridLayout
from PyQt5.QtGui import QPixmap, QImage
import sys
from main import Ui_mainWindow
from single import Ui_SingleWindow
from many import Ui_ManyWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.lines import Line2D


class single_window(QtWidgets.QMainWindow,Ui_SingleWindow):
    # FinishSignal = QtCore.pyqtSignal([list,object],[object])

    def __init__(self):
        super(single_window, self).__init__()
        # self.FinishSignal[list,object].connect(self.finish1)
        # self.FinishSignal[object].connect(self.finish2)


        # print(self.FinishSignal)
    def file_dir(self):
        from PyQt5.Qt import QFileDialog
        self.directory1 = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "./")  # 起始路径
        self.file_dir_modify(self.directory1)
    def file_dir_modify(self,file_dir_data):
        _translate = QtCore.QCoreApplication.translate
        if file_dir_data:
            single_Ui.lineEdit_zu_path.setText(_translate("ManyWindow", "%s"%file_dir_data))
            print(single_Ui.lineEdit_zu_path.text())
    def ensure(self):
        # single_Ui.pic_label = QLabel(self)
        # import cv2
        # pic = cv2.imread(r'C:\Users\yhstc\Desktop\90\kw\point\surface1.png')
        # pic=cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
        # height, width, channel = pic.shape
        # bytesPerLine = 3 * width
        # label_image = QImage(pic.data, width, height, bytesPerLine, QImage.Format_RGB888)
        # single_Ui.pic_label.setPixmap(QPixmap(label_image))
        # single_Ui.pic_label.setMargin(15)
        # # single_Ui.pic_label.layout(3)
        # single_Ui.pic_label.setGeometry(single_Ui.LineDisplayGB.geometry())
        # single_Ui.pic_label.setScaledContents(True)  # 让图片自适应label大小
        # # single_Ui.pic_label.setText("aaasjdajidjasjdiasjfijoiajfjasifjio")
        # single_Ui.pic_label.show()
        try:
            dir_num = str(int(single_Ui.direction_num.text())+1)
            w,h = single_Ui.w_h.text().split("/")
            lenth,width = single_Ui.l_w.text().split("/")
            x_deta,y_deta,z_deta = single_Ui.x_deta_y_deta_z_deta.text().split("/")
            x0,x1,y0,y1,z0,z1 = single_Ui.x0_y0_z0.text().split("/")
            yuzhi = single_Ui.yuzhi.text()
            scale_num = single_Ui.scal_number.text()
            te_zheng = single_Ui.te_zheng.text()
            self.list_begin = [dir_num,w,h,lenth,width,x_deta,y_deta,z_deta,x0,x1,y0,y1,z0,z1,yuzhi,scale_num,'single',te_zheng]
            print(self.list_begin)
            try :
                if single_Ui.lineEdit_zu_path.text():
                    self.directory1 =single_Ui.lineEdit_zu_path.text()
                    single_Ui.ensure.setEnabled(False)
                    single_Ui.pushButton_zu_path.setEnabled(False)
                    single_Ui.direction_num.setReadOnly(True)
                    single_Ui.w_h.setReadOnly(True)
                    single_Ui.l_w.setReadOnly(True)
                    single_Ui.x_deta_y_deta_z_deta.setReadOnly(True)
                    single_Ui.x0_y0_z0.setReadOnly(True)
                    single_Ui.yuzhi.setReadOnly(True)
                    single_Ui.scal_number.setReadOnly(True)
                    single_Ui.lineEdit_zu_path.setReadOnly(True)
                    single_Ui.te_zheng.setReadOnly(True)




            except Exception as e:

                # QMessageBox.warning(self, '参数错误', '请输入正确参数？', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                #                              QMessageBox.Cancel)
                QMessageBox.warning(self, '参数错误1', '请输入正确参数和地址', QMessageBox.Yes)
                # if reply == QMessageBox.Yes:
                #     print('退出')
                # else:
                #     print('不退出')
        except:

            # QMessageBox.warning(self, '参数错误', '请输入正确参数？', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
            #                              QMessageBox.Cancel)
            QMessageBox.warning(self, '参数错误2', '请输入正确参数和地址', QMessageBox.Yes)
    def begin(self):
        import final_all
        _translate = QtCore.QCoreApplication.translate
        print(self.list_begin,self.directory1)
        single_Ui.begin_cal.setText(_translate("ManyWindow", "计算中..."))
        single_Ui.volome.setText(_translate("ManyWindow", "计算中..."))
        single_Ui.area.setText(_translate("ManyWindow", "计算中..."))
        single_Ui.begin_cal.setEnabled(False)
        try:
            final_all.begin_cal(self.list_begin,self.directory1,self)
        except:
            QMessageBox.warning(self, '参数错误', '请输入正确参数和地址', QMessageBox.Yes)
        # temp_single_Ui=single_Ui
        # p2 = Process(target=final_all.begin_cal, args=(self.list_begin,self.directory1,single_Ui))
        # p2.daemon = False
        # p2.start()


    def finish1(self,data,obj):
        #体积、面积、灰度图，或者  三维图
        _translate = QtCore.QCoreApplication.translate
        single_Ui.volome.setText(_translate("SingleWindow", "%s" % float('%.2f'%data[0])))
        single_Ui.area.setText(_translate("SingleWindow", "%s"%float('%.2f'%data[1])))
        single_Ui.ensure.setEnabled(True)
        single_Ui.pushButton_zu_path.setEnabled(True)
        single_Ui.begin_cal.setEnabled(True)
        single_Ui.direction_num.setReadOnly(False)
        single_Ui.w_h.setReadOnly(False)
        single_Ui.l_w.setReadOnly(False)
        single_Ui.x_deta_y_deta_z_deta.setReadOnly(False)
        single_Ui.x0_y0_z0.setReadOnly(False)
        single_Ui.yuzhi.setReadOnly(False)
        single_Ui.scal_number.setReadOnly(False)
        single_Ui.lineEdit_zu_path.setReadOnly(False)
        single_Ui.te_zheng.setReadOnly(False)
        single_Ui.begin_cal.setText(_translate("ManyWindow", "开始计算"))
        single_Ui.pic_label = QLabel(self)
        # import cv2
        pic = obj
        height, width, channel = pic.shape
        bytesPerLine = 3 * width
        label_image = QImage(pic.data, width, height, bytesPerLine, QImage.Format_RGB888)
        single_Ui.pic_label.setPixmap(QPixmap(label_image))
        single_Ui.pic_label.setMargin(15)
        # single_Ui.pic_label.layout(3)
        single_Ui.pic_label.setGeometry(single_Ui.LineDisplayGB_2.geometry())
        single_Ui.pic_label.setScaledContents(True)  # 让图片自适应label大小
        # single_Ui.pic_label.setText("aaasjdajidjasjdiasjfijoiajfjasifjio")
        single_Ui.pic_label.show()
        QMessageBox.warning(self, '完成', '计算完成，请在相应文件夹查看数据', QMessageBox.Yes)

    def finish2(self,obj):
        single_Ui.pic_3d_label = QLabel(self)
        # import cv2
        pic = obj
        height, width, channel = pic.shape
        bytesPerLine = 3 * width
        label_image = QImage(pic.data, width, height, bytesPerLine, QImage.Format_RGB888)
        single_Ui.pic_3d_label.setPixmap(QPixmap(label_image))
        single_Ui.pic_3d_label.setMargin(15)
        # single_Ui.pic_label.layout(3)
        single_Ui.pic_3d_label.setGeometry(single_Ui.LineDisplayGB.geometry())
        single_Ui.pic_3d_label.setScaledContents(True)  # 让图片自适应label大小
        # single_Ui.pic_label.setText("aaasjdajidjasjdiasjfijoiajfjasifjio")
        single_Ui.pic_3d_label.show()
class many_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(many_window, self).__init__()
        super(many_window, self).__init__()

    def file_dir(self):
        from PyQt5.Qt import QFileDialog
        self.directory1 = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "./")  # 起始路径
        self.file_dir_modify(self.directory1)
    def file_dir_modify(self,file_dir_data):
        _translate = QtCore.QCoreApplication.translate
        if file_dir_data:
            many_Ui.lineEdit_zu_path.setText(_translate("ManyWindow", "%s"%file_dir_data))
            print(many_Ui.lineEdit_zu_path.text())
    def ensure(self):
        # many_Ui.progressBar.setGeometry(0, 0, 100, 5)

        try:
            dir_num = str(int(single_Ui.direction_num.text()) + 1)
            w, h = many_Ui.w_h.text().split("/")
            lenth, width = many_Ui.l_w.text().split("/")
            x_deta, y_deta, z_deta = many_Ui.x_deta_y_deta_z_deta.text().split("/")
            x0, x1, y0, y1, z0, z1 = many_Ui.x0_y0_z0.text().split("/")
            yuzhi = many_Ui.yuzhi.text()
            scale_num = many_Ui.scal_number.text()
            te_zheng = many_Ui.te_zheng.text()
            self.list_begin = [dir_num, w, h, lenth, width, x_deta, y_deta, z_deta, x0, x1, y0, y1, z0, z1, yuzhi,
                               scale_num, 'many',te_zheng]
            try:
                if many_Ui.lineEdit_zu_path.text():
                    self.directory1 = many_Ui.lineEdit_zu_path.text()
                    many_Ui.ensure.setEnabled(False)
                    many_Ui.pushButton_zu_path.setEnabled(False)
                    many_Ui.direction_num.setReadOnly(True)
                    many_Ui.w_h.setReadOnly(True)
                    many_Ui.l_w.setReadOnly(True)
                    many_Ui.x_deta_y_deta_z_deta.setReadOnly(True)
                    many_Ui.x0_y0_z0.setReadOnly(True)
                    many_Ui.yuzhi.setReadOnly(True)
                    many_Ui.scal_number.setReadOnly(True)
                    many_Ui.lineEdit_zu_path.setReadOnly(True)
                    many_Ui.te_zheng.setReadOnly(True)



            except:

                # QMessageBox.warning(self, '参数错误', '请输入正确参数？', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                #                              QMessageBox.Cancel)
                QMessageBox.warning(self, '参数错误1', '请输入正确参数和地址', QMessageBox.Yes)
                # if reply == QMessageBox.Yes:
                #     print('退出')
                # else:
                #     print('不退出')
        except:

            # QMessageBox.warning(self, '参数错误', '请输入正确参数？', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
            #                              QMessageBox.Cancel)
            QMessageBox.warning(self, '参数错误2', '请输入正确参数和地址', QMessageBox.Yes)

    def begin(self):
            import final_all
            _translate = QtCore.QCoreApplication.translate
            print(self.list_begin, self.directory1)
            many_Ui.begin_cal.setText(_translate("ManyWindow", "计算中..."))
            many_Ui.begin_cal.setEnabled(False)
            # single_Ui.volome.setText(_translate("ManyWindow", "计算中..."))
            # single_Ui.area.setText(_translate("ManyWindow", "计算中..."))
            try:
                self.plot_load()
                final_all.begin_cal(self.list_begin, self.directory1, self,many_Ui)
                # 如果出错
            except Exception as e:
                QMessageBox.warning(self, '计算错误', '计算过程出错，请确保按照说明书格式设置文件夹', QMessageBox.Yes)

            # p2.start()
    def plot_load(self):
        self.x_v = []
        self.y_v = []
        # print('绘制画布')
        self.LineFigure = Figure_Canvas()
        # print('传递格局')
        self.LineFigureLayout = QGridLayout(many_Ui.LineDisplayGB_Volume)
        # print('传递格局')
        self.LineFigureLayout.addWidget(self.LineFigure)
        # self.LineFigureLayout = QGridLayout(self.)
        # self.LineDisplayGB_Volume.addWidget(self.LineFigure)


        # print('绘制线设置')
        self.LineFigure.ax.set_xlim(0, 1)
        self.LineFigure.ax.set_ylim(0, 1)
        # print('2D线')
        self.line = Line2D(self.x_v, self.y_v)
        # print('2D线')
        self.LineFigure.ax.add_line(self.line)
        # print('2D线')
        self.LineFigure.draw()

        self.x_a = []
        self.y_a = []
        # print('绘制画布')
        self.LineFigure_a = Figure_Canvas()
        # print('传递格局')
        self.LineFigureLayout_a = QGridLayout(many_Ui.LineDisplayGB_Area)
        # print('传递格局')P
        self.LineFigureLayout_a.addWidget(self.LineFigure_a)
        # self.LineFigureLayout = QGridLayout(self.)
        # self.LineDisplayGB_Volume.addWidget(self.LineFigure)


        # print('绘制线设置')
        self.LineFigure_a.ax.set_xlim(0, 1)
        self.LineFigure_a.ax.set_ylim(0, 1)
        # print('2D线')
        self.line_a = Line2D(self.x_a, self.y_a,color='red')
        # print('2D线')
        self.LineFigure_a.ax.add_line(self.line_a)
        # print('2D线')
        self.LineFigure_a.draw()


    def loading(self,volum_area_data):
        # print('绘图开始')
        volum,area,pic_num= volum_area_data

        self.x_v.append(pic_num)  # 将每次传过来的n追加到xdata中
        self.y_v.append(volum)
        # print('2D线')
        self.line.set_data(self.x_v, self.y_v)  # 重新设置曲线的值
        # print('设置轴')

        self.x_a.append(pic_num)  # 将每次传过来的n追加到xdata中
        self.y_a.append(area)
        # print('2D线')
        self.line_a.set_data(self.x_a, self.y_a)  # 重新设置曲线的值
        # print('设置轴')


        if pic_num==1:
            self.max_volumn = volum
        elif self.max_volumn < volum:
            self.max_volumn = volum
        # print('设置轴')
        if pic_num == 1:
            self.max_area = area
        elif self.max_area < area:
            self.max_area = area
        # print('设置轴')


        if pic_num > 201:
            # print('设置轴1')
            self.LineFigure.ax.set_xlim(self.x_v[-200], pic_num)  # 设置x轴的范围pi代表3.14...圆周率，
            self.LineFigure.ax.set_ylim(0, self.max_volumn)  # 设置y轴的范围

            self.line.set_xdata(self.x_v[-200:])
            self.line.set_ydata(self.y_v[-200:])

            self.LineFigure.draw()
            # print('设置轴1')


            # print('设置轴1')
            self.LineFigure_a.ax.set_xlim(self.x_a[-200], pic_num)  # 设置x轴的范围pi代表3.14...圆周率，
            self.LineFigure_a.ax.set_ylim(0, self.max_area)  # 设置y轴的范围
            self.line_a.set_xdata(self.x_a[-200:])
            self.line_a.set_ydata(self.y_a[-200:])
            self.LineFigure_a.draw()
            # print('设置轴1')


        else:
            # print('设置轴2')
            self.LineFigure.ax.set_xlim(0, pic_num)  # 设置x轴的范围pi代表3.14...圆周率，
            self.LineFigure.ax.set_ylim(0, self.max_volumn)  # 设置y轴的范围
            self.line.set_xdata(self.x_v)
            self.line.set_ydata(self.y_v)
            self.LineFigure.draw()
            # print('设置轴2')
            # plt.plot(xdata[-100:], ydata[-100:], color='red')


            # print('设置轴2')
            self.LineFigure_a.ax.set_xlim(0, pic_num)  # 设置x轴的范围pi代表3.14...圆周率，
            self.LineFigure_a.ax.set_ylim(0, self.max_area)  # 设置y轴的范围
            self.line_a.set_xdata(self.x_a)
            self.line_a.set_ydata(self.y_a)
            self.LineFigure_a.draw()
            # print('设置轴2')
            # plt.plot(xdata[-100:], ydata[-100:], color='red')
    def finish(self):
        #体积、面积、灰度图，或者  三维图
        _translate = QtCore.QCoreApplication.translate

        many_Ui.ensure.setEnabled(True)
        many_Ui.pushButton_zu_path.setEnabled(True)
        many_Ui.begin_cal.setEnabled(True)
        many_Ui.direction_num.setReadOnly(False)
        many_Ui.w_h.setReadOnly(False)
        many_Ui.l_w.setReadOnly(False)
        many_Ui.x_deta_y_deta_z_deta.setReadOnly(False)
        many_Ui.x0_y0_z0.setReadOnly(False)
        many_Ui.yuzhi.setReadOnly(False)
        many_Ui.scal_number.setReadOnly(False)
        many_Ui.lineEdit_zu_path.setReadOnly(False)
        many_Ui.te_zheng.setReadOnly(False)
        many_Ui.begin_cal.setText(_translate("ManyWindow", "开始计算"))
        QMessageBox.warning(self, '完成', '计算完成，请在相应文件夹查看数据', QMessageBox.Yes)

class Figure_Canvas(FigureCanvas):
    def __init__(self,parent=None,width=3.9,height=2.7,dpi=100):
        self.fig=Figure(figsize=(width,height),dpi=100)
        super(Figure_Canvas,self).__init__(self.fig)
        self.ax=self.fig.add_subplot(111)

class main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()

    def show_single(self):

        singleWindow.show()

    def show_many(self):

        #界面初始化
        many_Ui.progressBar.setRange(0, 500)  # 设置进度条的范围
        many_Ui.progressBar.setValue(0)
        manyWindow.show()

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

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = main_window()
    Mian_Ui = Ui_mainWindow()
    Mian_Ui.setupUi(mainWindow)
    mainWindow.show()

    single_Ui = single_window()
    singleWindow = single_window()
    single_Ui.setupUi(singleWindow)


    many_Ui = Ui_ManyWindow()
    manyWindow = many_window()

    many_Ui.setupUi(manyWindow)



    sys.exit(app.exec_())