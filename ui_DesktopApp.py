# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DesktopAppIiwrzg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import source_image_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1626, 848)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: rgb(241, 240, 245);")
        MainWindow.setIconSize(QSize(30, 30))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_menu_container = QFrame(self.centralwidget)
        self.side_menu_container.setObjectName(u"side_menu_container")
        self.side_menu_container.setMaximumSize(QSize(0, 16777215))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        self.side_menu_container.setFont(font)
        self.side_menu_container.setFrameShape(QFrame.StyledPanel)
        self.side_menu_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.side_menu_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slide_menu = QFrame(self.side_menu_container)
        self.slide_menu.setObjectName(u"slide_menu")
        self.slide_menu.setMinimumSize(QSize(198, 0))
        self.slide_menu.setFrameShape(QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.slide_menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.slide_menu)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_2, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.frame_7 = QFrame(self.slide_menu)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet(u"background-color: rgb(211, 222, 216);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.home_button = QPushButton(self.frame_7)
        self.home_button.setObjectName(u"home_button")
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setWeight(75)
        self.home_button.setFont(font2)
        self.home_button.setStyleSheet(u"background-color: rgb(96, 140, 117);\n"
"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"icons/fa_home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home_button.setIcon(icon)

        self.verticalLayout_5.addWidget(self.home_button)

        self.about_button = QPushButton(self.frame_7)
        self.about_button.setObjectName(u"about_button")
        self.about_button.setFont(font2)
        self.about_button.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"icons/bi_people-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.about_button.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.about_button)

        self.displayResults_button = QPushButton(self.frame_7)
        self.displayResults_button.setObjectName(u"displayResults_button")
        self.displayResults_button.setFont(font2)
        self.displayResults_button.setStyleSheet(u"background-color: rgb(96, 140, 117);\n"
"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u"icons/Vector.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.displayResults_button.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.displayResults_button)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.slide_menu)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.exit_button = QPushButton(self.frame_8)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u"icons/fa_external-link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon3)
        self.exit_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_8.addWidget(self.exit_button, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout_4.addWidget(self.frame_8, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.slide_menu)


        self.horizontalLayout.addWidget(self.side_menu_container)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_body_contents = QFrame(self.main_body)
        self.main_body_contents.setObjectName(u"main_body_contents")
        sizePolicy.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy)
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.header_frame = QFrame(self.main_body_contents)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.header_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.frame_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon4 = QIcon()
        icon4.addFile(u"icons/ant-design_menu-outlined.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.pushButton_6, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_5.addWidget(self.frame_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 0))
        icon5 = QIcon()
        icon5.addFile(u"icons/bi_person-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon5)

        self.horizontalLayout_5.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon6 = QIcon()
        icon6.addFile(u"icons/fluent_sign-out-24-filled.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon6)

        self.horizontalLayout_5.addWidget(self.pushButton_5)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame = QFrame(self.header_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon7 = QIcon()
        icon7.addFile(u"icons/carbon_minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon7)

        self.horizontalLayout_4.addWidget(self.minimize_window_button)

        self.maximize_window_button = QPushButton(self.frame)
        self.maximize_window_button.setObjectName(u"maximize_window_button")
        icon8 = QIcon()
        icon8.addFile(u"icons/bi_arrows-angle-expand.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_window_button.setIcon(icon8)

        self.horizontalLayout_4.addWidget(self.maximize_window_button)

        self.close_button = QPushButton(self.frame)
        self.close_button.setObjectName(u"close_button")
        icon9 = QIcon()
        icon9.addFile(u"icons/ant-design_close-circle-outlined.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon9)
        self.close_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.close_button)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.header_frame)

        self.stackedWidget = QStackedWidget(self.main_body_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(211, 222, 216);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.label_4 = QLabel(self.home_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(790, 100, 331, 41))
        font3 = QFont()
        font3.setPointSize(15)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"background-color: rgb(74, 122, 98);\n"
"color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.home_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(900, 0, 101, 91))
        self.label_7.setStyleSheet(u"image: url(:/images/Downloads/kwf_logo-0.png);")
        self.label_7.setPixmap(QPixmap(u"../../Downloads/kwf_logo-0.png"))
        self.label_7.setScaledContents(True)
        self.label_8 = QLabel(self.home_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(700, 220, 511, 361))
        self.label_8.setStyleSheet(u"image: url(:/images/Downloads/image 2.png);")
        self.label_8.setPixmap(QPixmap(u"../../Downloads/image 2.png"))
        self.label_8.setScaledContents(True)
        self.stackedWidget.addWidget(self.home_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.label_9 = QLabel(self.about_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(890, 0, 101, 91))
        self.label_9.setStyleSheet(u"image: url(:/images/Downloads/kwf_logo-0.png);")
        self.label_9.setPixmap(QPixmap(u"../../Downloads/kwf_logo-0.png"))
        self.label_9.setScaledContents(True)
        self.label_5 = QLabel(self.about_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(700, 100, 501, 51))
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"background-color: rgb(74, 122, 98);\n"
"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.about_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(120, 280, 191, 61))
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"background-color: rgb(28, 89, 58);\n"
"color: rgb(255, 255, 255);")
        self.label_15 = QLabel(self.about_page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(810, 600, 151, 31))
        font5 = QFont()
        font5.setFamily(u"MS Shell Dlg 2")
        font5.setPointSize(12)
        self.label_15.setFont(font5)
        self.label_16 = QLabel(self.about_page)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(460, 600, 111, 31))
        self.label_16.setFont(font5)
        self.label_17 = QLabel(self.about_page)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(600, 600, 161, 31))
        self.label_17.setFont(font5)
        self.label_18 = QLabel(self.about_page)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(1330, 600, 171, 31))
        self.label_18.setFont(font5)
        self.label_19 = QLabel(self.about_page)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(1020, 600, 251, 31))
        self.label_19.setFont(font5)
        self.label_20 = QLabel(self.about_page)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(1560, 600, 181, 31))
        self.label_20.setFont(font5)
        self.label_21 = QLabel(self.about_page)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(130, 580, 161, 61))
        self.label_21.setFont(font4)
        self.label_21.setStyleSheet(u"background-color: rgb(28, 89, 58);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.textBrowser = QTextBrowser(self.about_page)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(580, 260, 821, 141))
        font6 = QFont()
        font6.setFamily(u"HelvLight")
        font6.setPointSize(8)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.textBrowser.setFont(font6)
        self.textBrowser.setStyleSheet(u"background-color: rgb(241, 240, 245);\n"
"font: 8pt \"HelvLight\";\n"
"")
        self.stackedWidget.addWidget(self.about_page)
        self.displayResults_page = QWidget()
        self.displayResults_page.setObjectName(u"displayResults_page")
        self.label_3 = QLabel(self.displayResults_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 211, 40))
        font7 = QFont()
        font7.setPointSize(20)
        self.label_3.setFont(font7)
        self.label_3.setStyleSheet(u"background-color: rgb(28, 89, 58);\n"
"color: rgb(255, 255, 255);")
        self.save_images_button = QPushButton(self.displayResults_page)
        self.save_images_button.setObjectName(u"save_images_button")
        self.save_images_button.setGeometry(QRect(40, 70, 151, 31))
        font8 = QFont()
        font8.setFamily(u"MS Shell Dlg 2")
        font8.setPointSize(10)
        self.save_images_button.setFont(font8)
        self.save_images_button.setStyleSheet(u"background-color: rgb(74, 122, 98);\n"
"color: rgb(255, 255, 255);\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"icons/fa_upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_images_button.setIcon(icon10)
        self.upload_button = QPushButton(self.displayResults_page)
        self.upload_button.setObjectName(u"upload_button")
        self.upload_button.setGeometry(QRect(0, 950, 75, 27))
        font9 = QFont()
        font9.setPointSize(12)
        self.upload_button.setFont(font9)
        self.upload_button.setStyleSheet(u"background-color: rgb(74, 122, 98);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.stackedWidget.addWidget(self.displayResults_page)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.main_body_contents)

        self.footer = QFrame(self.main_body)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.footer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font10 = QFont()
        font10.setBold(True)
        font10.setWeight(75)
        self.label.setFont(font10)

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Wildlife A.I. Portal", None))
        self.home_button.setText(QCoreApplication.translate("MainWindow", u"   Home", None))
        self.about_button.setText(QCoreApplication.translate("MainWindow", u"  About", None))
        self.displayResults_button.setText(QCoreApplication.translate("MainWindow", u"     Upload and Results", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"   Exit", None))
        self.pushButton_6.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.minimize_window_button.setText("")
        self.maximize_window_button.setText("")
        self.close_button.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"       Wildlife A.I. Software Portal", None))
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"              About the Wildlife A.I. Software Portal", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"    MISSION", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Saketh Vangara", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Yuhao Shi", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Rohan Magesh", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Amudhan Selvam", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Keerthana Eswarapragada", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Arjun Vangala", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"     TEAM", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'HelvLight'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">The Wildlife A.I. Software Portal aims to support biologists and researchers through technological means. In our debut version, users can upload images of various animals. These images will be processed through the YoloV5 model, which detects the species of the animals. Results can be viewed immediately after images are uploaded. As a whole, Kashmir World Foundation strives to integrate advanced technology solutions through education, science, and art for wildlife conservation and protection.</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"        YoloV5", None))
        self.save_images_button.setText(QCoreApplication.translate("MainWindow", u"    Save Images", None))
        self.upload_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Wildlife A.I. Software Portal V 1.0.0", None))
    # retranslateUi

