from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMaximumSize(QSize(1920, 1080))
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #EAEAEA;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1920, 1080))
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"    background-color: #EAEAEA;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(404, 1080))
        self.frame.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 930, 300, 90))
        self.label_6.setMaximumSize(QSize(300, 90))
        self.label_6.setStyleSheet(u"QLabel {\n"
"padding : 20px;\n"
"}")
        self.label_6.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/KELUAR.png"))
        self.label_6.setScaledContents(True)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 40, 302, 421))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget)
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

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(290, 70))
        self.label.setStyleSheet(u"QLabel {\n"
"padding : 20px;\n"
"\n"
"}")
        self.label.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Learning.png"))

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(290, 70))
        self.label_2.setStyleSheet(u"QLabel {\n"
"padding : 20px;\n"
"}")
        self.label_2.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Flashcards.png"))
        self.label_2.setScaledContents(False)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(290, 80))
        self.label_3.setStyleSheet(u"QLabel {\n"
"padding : 20px;\n"
"}")
        self.label_3.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/DRAWING BOARD.png"))

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(290, 80))
        self.label_4.setStyleSheet(u"QLabel {\n"
"padding : 20px;\n"
"}")
        self.label_4.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/MULTIPLE CHOICE.png"))

        self.verticalLayout.addWidget(self.label_4)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QSize(1920, 1080))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"    background-color: #EAEAEA;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.widget1 = QWidget(self.frame_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(90, 30, 921, 121))
        self.widget1.setMaximumSize(QSize(1920, 1080))
        self.widget1.setStyleSheet(u"QWidget {\n"
"    background-color: #E36B37;\n"
"    border: 1px solid #E36B37;  \n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.label_11 = QLabel(self.widget1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(710, 20, 161, 71))
        self.label_11.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Panduan.png"))
        self.widget2 = QWidget(self.widget1)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(50, 20, 581, 72))
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(self.widget2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(30, 16777215))
        self.label_8.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Backspace.png"))

        self.horizontalLayout_2.addWidget(self.label_8)

        self.label_9 = QLabel(self.widget2)
        self.label_9.setObjectName(u"label_9")
        font1 = QFont()
        font1.setFamilies([u"Jellee Roman"])
        font1.setPointSize(16)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"QLabel{\n"
"color:rgb(255, 199, 174)\n"
"};")

        self.horizontalLayout_2.addWidget(self.label_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label_10 = QLabel(self.widget2)
        self.label_10.setObjectName(u"label_10")
        font2 = QFont()
        font2.setFamilies([u"Jellee Roman"])
        font2.setPointSize(20)
        font2.setBold(False)
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"};")

        self.verticalLayout_2.addWidget(self.label_10)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(410, 650, 471, 321))
        self.label_7.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Island 2 (2).png"))
        self.label_7.setScaledContents(True)
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(150, 170, 701, 461))
        self.label_12.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Island anime.png"))
        self.label_12.setScaledContents(True)
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(420, 500, 141, 191))
        self.label_13.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"}")
        self.label_13.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Ladder.png"))
        self.label_13.setScaledContents(True)

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(380, 1080))
        self.frame_3.setStyleSheet(u"QFrame {\n"
"    background-color: #EAEAEA;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 20, 311, 43))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setSpacing(14)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Jepang = QLabel(self.layoutWidget)
        self.Jepang.setObjectName(u"Jepang")
        self.Jepang.setMaximumSize(QSize(100, 16777215))
        self.Jepang.setPixmap(QPixmap(u"../Documents/DuaHasa/Assets/Logo.png"))
        self.Jepang.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.Jepang)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.api = QLabel(self.layoutWidget)
        self.api.setObjectName(u"api")
        self.api.setPixmap(QPixmap(u"../Documents/DuaHasa/Assets/Streak.png"))
        self.api.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.api)

        self.angka = QLabel(self.layoutWidget)
        self.angka.setObjectName(u"angka")
        font3 = QFont()
        font3.setFamilies([u"Jellee"])
        font3.setPointSize(18)
        self.angka.setFont(font3)
        self.angka.setStyleSheet(u"QLabel {\n"
"	color: #C3C3C3;\n"
"}")

        self.horizontalLayout_3.addWidget(self.angka)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.segitiga = QLabel(self.layoutWidget)
        self.segitiga.setObjectName(u"segitiga")
        self.segitiga.setPixmap(QPixmap(u"../Documents/DuaHasa/Assets/Points.png"))
        self.segitiga.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.segitiga)

        self.angka_2 = QLabel(self.layoutWidget)
        self.angka_2.setObjectName(u"angka_2")
        self.angka_2.setFont(font3)
        self.angka_2.setStyleSheet(u"QLabel {\n"
"	color: #E16834;\n"
"}")

        self.horizontalLayout_5.addWidget(self.angka_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)

        self.Star = QLabel(self.layoutWidget)
        self.Star.setObjectName(u"Star")
        self.Star.setMaximumSize(QSize(200, 100))
        self.Star.setPixmap(QPixmap(u"../Documents/DuaHasa/Assets/Stars.png"))
        self.Star.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.Star)


        self.horizontalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"duahasa", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_11.setText("")
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TEXT SESI", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Menggunakan Frasa Dasar", None))
        self.label_7.setText("")
        self.label_12.setText("")
        self.label_13.setText("")
        self.Jepang.setText("")
        self.api.setText("")
        self.angka.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.segitiga.setText("")
        self.angka_2.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.Star.setText("")
    # retranslateUi

