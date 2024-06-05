# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashboardFyOFJW.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QProgressBar, QSizePolicy,
    QVBoxLayout, QWidget)

import sys

class Flashcard(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1748, 1079)
        MainWindow.setMaximumSize(QSize(1920, 1080))
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: red;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1920, 1080))
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	background-color: #EAEAEA;\n"
"}	")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(380, 1080))
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: white;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 302, 421))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(300, 90))
        font = QFont()
        font.setFamilies([u"Auro"])
        font.setPointSize(45)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"QLabel {\n"
"padding : 10px;\n"
"color: rgb(241, 72, 18)\n"
"}")
        self.label_5.setScaledContents(True)

        self.verticalLayout.addWidget(self.label_5)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(290, 70))
        self.label.setStyleSheet(u"QLabel {\n"
"padding : 20px;\n"
"\n"
"}")
        self.label.setPixmap(QPixmap(u"Assets/Learning.png"))

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(290, 70))
        self.label_2.setStyleSheet(u"QLabel {\n"
"padding : 20px;\n"
"}")
        self.label_2.setPixmap(QPixmap(u"Assets/Flashcards.png"))
        self.label_2.setScaledContents(False)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(290, 80))
        self.label_3.setStyleSheet(u"QLabel {\n"
"padding : 20px;\n"
"}")
        self.label_3.setPixmap(QPixmap(u"Assets/DRAWING BOARD.png"))

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(290, 80))
        self.label_4.setStyleSheet(u"QLabel {\n"
"padding : 20px;\n"
"}")
        self.label_4.setPixmap(QPixmap(u"Assets/MULTIPLE CHOICE.png"))

        self.verticalLayout.addWidget(self.label_4)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QSize(960, 1080))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(89, 69, 671, 531))
        self.frame_4.setStyleSheet(u"QFrame {\n"
"	background-color: white;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.depan = QLabel(self.frame_4)
        self.depan.setObjectName(u"depan")
        self.depan.setMaximumSize(QSize(671, 71))
        font1 = QFont()
        font1.setFamilies([u"Jellee Roman"])
        font1.setPointSize(28)
        self.depan.setFont(font1)
        self.depan.setStyleSheet(u"QLabel {\n"
"	color: #ED913C;\n"
"}")
        self.depan.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.depan, 0, Qt.AlignHCenter)

        self.image = QLabel(self.frame_4)
        self.image.setObjectName(u"image")
        self.image.setMaximumSize(QSize(501, 311))
        self.image.setPixmap(QPixmap(u"Assets/Flashcards/Image.png"))
        self.image.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.image, 0, Qt.AlignHCenter)

        self.pertanyaan = QLabel(self.frame_4)
        self.pertanyaan.setObjectName(u"pertanyaan")
        self.pertanyaan.setMaximumSize(QSize(671, 71))
        font2 = QFont()
        font2.setFamilies([u"Jellee Roman"])
        font2.setPointSize(20)
        self.pertanyaan.setFont(font2)
        self.pertanyaan.setStyleSheet(u"QLabel {\n"
"	color: #424242;\n"
"}")
        self.pertanyaan.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.pertanyaan, 0, Qt.AlignHCenter)

        self.background = QLabel(self.frame_2)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(50, 50, 751, 591))
        self.background.setPixmap(QPixmap(u"Assets/Flashcards/Background.png"))
        self.background.setScaledContents(True)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(150, 800, 561, 261))
        self.label_6.setPixmap(QPixmap(u"Assets/Flashcards/Kartu.png"))
        self.label_6.setScaledContents(True)
        self.background.raise_()
        self.frame_4.raise_()
        self.label_6.raise_()

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(380, 1080))
        self.frame_3.setStyleSheet(u"horizontalLayout_4 {\n"
"	margin-right: 50px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 100, 351, 471))
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	border: 2px solid #CCCCCC;\n"
"	border-radius: 20px;\n"
"}")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 10, 291, 51))
        font3 = QFont()
        font3.setFamilies([u"Jellee"])
        font3.setPointSize(16)
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"QLabel {\n"
"	border: 0px;\n"
"	color: #585858;\n"
"}")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(180, 90, 141, 31))
        font4 = QFont()
        font4.setFamilies([u"Jellee"])
        font4.setPointSize(14)
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"QLabel {\n"
"	border: 0px;\n"
"	color: #585858;\n"
"}")
        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 130, 301, 51))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    background: #E0E0E0;\n"
"	border-radius: 20px;\n"
"    text-align: center;\n"
"	color: transparent;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #843DB0;\n"
"	border-radius: 20px;\n"
"	margin: 2px;\n"
"}\n"
"")
        self.progressBar.setValue(24)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 220, 311, 51))
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"QLabel {\n"
"	border: 0px;\n"
"	color: #585858;\n"
"}")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 290, 151, 151))
        self.label_10.setStyleSheet(u"QLabel {\n"
"	border-color: 0px;\n"
"}	")
        self.label_10.setPixmap(QPixmap(u"Assets/maskot.png"))
        self.label_10.setScaledContents(True)
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(180, 290, 151, 81))
        font5 = QFont()
        font5.setFamilies([u"Jellee"])
        font5.setPointSize(12)
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"QLabel {\n"
"	border: 0px;\n"
"	color: #585858;\n"
"}")
        self.label_11.setWordWrap(True)
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(170, 400, 141, 41))
        self.label_12.setPixmap(QPixmap(u"Assets/Button Atur.png"))
        self.label_12.setScaledContents(True)
        self.widget_2 = QWidget(self.frame_3)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, 740, 351, 161))
        self.widget_2.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	border: 2px solid #CCCCCC;\n"
"	border-radius: 20px;\n"
"}")
        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 20, 291, 51))
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"QLabel {\n"
"	border: 0px;\n"
"	color: #585858;\n"
"}")
        self.label_14 = QLabel(self.widget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 80, 311, 51))
        self.label_14.setPixmap(QPixmap(u"Assets/Masuk Button.png"))
        self.label_14.setScaledContents(True)
        self.layoutWidget1 = QWidget(self.frame_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 20, 351, 61))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setSpacing(14)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Jepang = QLabel(self.layoutWidget1)
        self.Jepang.setObjectName(u"Jepang")
        self.Jepang.setMaximumSize(QSize(130, 16777213))
        self.Jepang.setPixmap(QPixmap(u"Assets/Logo Jepang.png"))
        self.Jepang.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.Jepang)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.api = QLabel(self.layoutWidget1)
        self.api.setObjectName(u"api")
        self.api.setPixmap(QPixmap(u"Assets/Streak.png"))
        self.api.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.api)

        self.angka = QLabel(self.layoutWidget1)
        self.angka.setObjectName(u"angka")
        font6 = QFont()
        font6.setFamilies([u"Jellee"])
        font6.setPointSize(18)
        self.angka.setFont(font6)
        self.angka.setStyleSheet(u"QLabel {\n"
"	color: #C3C3C3;\n"
"}")

        self.horizontalLayout_2.addWidget(self.angka)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.segitiga = QLabel(self.layoutWidget1)
        self.segitiga.setObjectName(u"segitiga")
        self.segitiga.setPixmap(QPixmap(u"Assets/Points.png"))
        self.segitiga.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.segitiga)

        self.angka_2 = QLabel(self.layoutWidget1)
        self.angka_2.setObjectName(u"angka_2")
        self.angka_2.setFont(font6)
        self.angka_2.setStyleSheet(u"QLabel {\n"
"	color: #E16834;\n"
"}")

        self.horizontalLayout_3.addWidget(self.angka_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.Star = QLabel(self.layoutWidget1)
        self.Star.setObjectName(u"Star")
        self.Star.setMaximumSize(QSize(200, 100))
        self.Star.setPixmap(QPixmap(u"Assets/Stars.png"))
        self.Star.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.Star)


        self.horizontalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"duahasa", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.depan.setText(QCoreApplication.translate("MainWindow", u"Depan", None))
        self.image.setText("")
        self.pertanyaan.setText(QCoreApplication.translate("MainWindow", u"Apa yang dia lakukan?", None))
        self.background.setText("")
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Progress Flashcard Kamu", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"3/10 Dipelajari", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Atur Flashcard Kamu!", None))
        self.label_10.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Kamu bisa menambahkan hal yang ingin kamu pelajari di sini", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Atur Profile Kamu!", None))
        self.label_14.setText("")
        self.Jepang.setText("")
        self.api.setText("")
        self.angka.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.segitiga.setText("")
        self.angka_2.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.Star.setText("")
    # retranslateUi

if __name__ == "__main__":
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = Flashcard()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec())

