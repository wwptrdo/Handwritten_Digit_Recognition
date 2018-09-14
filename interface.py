# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from mnist_test import *
from Drawer import *
from mnist_app import *
from mnist_backward import *


class Ui_MainWindow(object):

    # 槽函数刷新UI
    def flashTextEdit(self, str):
        print(str)
        self.textEdit.setText(self.textEdit.toPlainText() + str)

    # 点击识别按钮调用此方法，进行识别
    def btRecog(self):
        self.drawer.saveImage("./pic/new.png", "png")  # 先保存图片
        print("保存图片成功！")
        self.recogThread.start()  # 开启识别线程
        # QtWidgets.QMessageBox.information(self.pushButton, "标题", "这是第一个PyQt5 GUI程序")

    # 点击训练按钮调用此方法，进行训练
    def btTrain(self):
        self.trainThread.start()  # 开启线程
        self.trainBackwardThread.start()  # 开启线程
        # self.thread.start()
        # QtWidgets.QMessageBox.information(self.pushButton, "标题", "这是第一个PyQt5 GUI程序")

    # 点击了清空按钮
    def btClear(self):
        self.drawer.clearImage()

    # 点击了停止按钮
    def btStop(self):
        self.trainThread.stop()
        self.trainBackwardThread.stop()
        self.textEdit.setText(self.textEdit.toPlainText() + "已停止\n")

    # 槽函数：获得识别的结果，在这里进行显示
    def flashRetNum(self, num):
        print(num)
        self.lcdNumber.display(num)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(814, 808)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 400, 93, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 390, 93, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 10, 161, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 610, 121, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(420, 560, 141, 141))
        self.lcdNumber.setObjectName("lcdNumber")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 80, 321, 291))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(460, 90, 301, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonClear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonClear.setGeometry(QtCore.QRect(490, 390, 101, 41))
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.pushButtonStop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStop.setGeometry(QtCore.QRect(260, 400, 81, 41))
        self.pushButtonStop.setObjectName("pushButtonStop")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 814, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.trainThread = TrainThread()  # 实例化Thread类
        self.trainThread.logOut.connect(self.flashTextEdit)  # 将信号连接至槽函数

        self.trainBackwardThread = TrainBackwardThread()
        self.trainBackwardThread.logOutB.connect(self.flashTextEdit)

        self.drawer = Drawer()  # 绘图控件
        self.verticalLayout.addWidget(self.drawer)  # 信号与槽函数绑定

        self.recogThread = RecogThread()  # 进行识别的线程类
        self.recogThread.retOut.connect(self.flashRetNum)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.btRecog)
        self.pushButton.clicked.connect(self.btTrain)
        self.pushButtonClear.clicked.connect(self.btClear)
        self.pushButtonStop.clicked.connect(self.btStop)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "手写数字图片识别程序"))
        self.pushButton.setText(_translate("MainWindow", "训练"))
        self.pushButton_2.setText(_translate("MainWindow", "识别"))
        self.label.setText(_translate("MainWindow", "手写数字识别"))
        self.label_2.setText(_translate("MainWindow", "  识别结果"))
        self.pushButtonClear.setText(_translate("MainWindow", "清除"))
        self.pushButtonStop.setText(_translate("MainWindow", "停止训练"))

