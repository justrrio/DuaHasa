# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FlashcardwVebnV.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QTextEdit, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMaximumSize(QSize(1920, 1200))
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #EAEAEA;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1920, 1200))
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
        self.frame.setToolTipDuration(2)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px\n"
"}\n"
"\n"
"QLabel {\n"
"	cursor: pointer;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Next_button_island_6 = QToolButton(self.frame)
        self.Next_button_island_6.setObjectName(u"Next_button_island_6")
        self.Next_button_island_6.setGeometry(QRect(30, 950, 321, 71))
        self.Next_button_island_6.setMaximumSize(QSize(1000, 1000))
        font = QFont()
        font.setKerning(True)
        self.Next_button_island_6.setFont(font)
        self.Next_button_island_6.setContextMenuPolicy(Qt.NoContextMenu)
        self.Next_button_island_6.setAutoFillBackground(False)
        self.Next_button_island_6.setStyleSheet(u"QToolButton {\n"
"    border: none;                  /* Menghilangkan border */\n"
"    background: transparent;       /* Membuat background transparan */\n"
"    padding: 0;                    /* Menghilangkan padding */\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"Leftbar/Keluar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Next_button_island_6.setIcon(icon)
        self.Next_button_island_6.setIconSize(QSize(1000, 1000))
        self.Next_button_island_6.setCheckable(False)
        self.Next_button_island_6.setAutoRepeat(False)
        self.Next_button_island_6.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Next_button_island_6.setAutoRaise(False)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(41, 41, 300, 90))
        self.logo.setMaximumSize(QSize(300, 90))
        font1 = QFont()
        font1.setFamilies([u"Auro"])
        font1.setPointSize(45)
        font1.setBold(True)
        self.logo.setFont(font1)
        self.logo.setStyleSheet(u"QLabel {\n"
"padding : 10px;\n"
"color: rgb(241, 72, 18)\n"
"}")
        self.logo.setScaledContents(True)
        self.flashcard_active = QLabel(self.frame)
        self.flashcard_active.setObjectName(u"flashcard_active")
        self.flashcard_active.setGeometry(QRect(20, 190, 340, 97))
        self.flashcard_active.setMaximumSize(QSize(340, 100))
        self.flashcard_active.setCursor(QCursor(Qt.PointingHandCursor))
        self.flashcard_active.setStyleSheet(u"QLabel {\n"
"padding : 20px;\n"
"\n"
"}")
        self.flashcard_active.setPixmap(QPixmap(u"Leftbar/Flashcards Active.png"))
        self.flashcard_active.setScaledContents(False)
        self.belajar = QLabel(self.frame)
        self.belajar.setObjectName(u"belajar")
        self.belajar.setGeometry(QRect(40, 130, 291, 60))
        self.belajar.setMaximumSize(QSize(291, 60))
        self.belajar.setCursor(QCursor(Qt.PointingHandCursor))
        self.belajar.setStyleSheet(u"QLabel {\n"
"    padding: 10px;                /* Padding dalam label */\n"
"    border: 2px solid transparent; /* Border default transparan */\n"
"    border-radius: 15px;          /* Border radius untuk sudut melengkung */\n"
"    background-color: transparent; /* Background transparan */\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    border: 2px solid #2D8AE0;    /* Warna border saat di-hover */\n"
"    background-color: rgba(211, 211, 211, 0.5); /* Background keabu-abuan dengan opasitas */\n"
"}\n"
"")
        self.belajar.setPixmap(QPixmap(u"Leftbar/Learning.png"))
        self.belajar.setScaledContents(False)
        self.pilihan_ganda = QLabel(self.frame)
        self.pilihan_ganda.setObjectName(u"pilihan_ganda")
        self.pilihan_ganda.setGeometry(QRect(40, 290, 291, 60))
        self.pilihan_ganda.setMaximumSize(QSize(291, 60))
        self.pilihan_ganda.setCursor(QCursor(Qt.PointingHandCursor))
        self.pilihan_ganda.setStyleSheet(u"QLabel {\n"
"    padding: 10px;                /* Padding dalam label */\n"
"    border: 2px solid transparent; /* Border default transparan */\n"
"    border-radius: 15px;          /* Border radius untuk sudut melengkung */\n"
"    background-color: transparent; /* Background transparan */\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    border: 2px solid #2D8AE0;    /* Warna border saat di-hover */\n"
"    background-color: rgba(211, 211, 211, 0.5); /* Background keabu-abuan dengan opasitas */\n"
"}\n"
"")
        self.pilihan_ganda.setPixmap(QPixmap(u"Leftbar/Multiple Choice.png"))

        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QSize(1098, 1080))
        self.frame_2.setMouseTracking(True)
        self.frame_2.setStyleSheet(u"QFrame {\n"
"    background-color: #EAEAEA;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QLabel {\n"
"	background-color: white;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.Flashcard = QWidget(self.frame_2)
        self.Flashcard.setObjectName(u"Flashcard")
        self.Flashcard.setGeometry(QRect(160, 80, 731, 901))
        self.Flashcard.setStyleSheet(u"QLabel {\n"
"	border: 0px;\n"
"	color: #585858;\n"
"}")
        self.pertanyaan = QLabel(self.Flashcard)
        self.pertanyaan.setObjectName(u"pertanyaan")
        self.pertanyaan.setGeometry(QRect(180, 90, 411, 111))
        self.pertanyaan.setMaximumSize(QSize(500, 200))
        font2 = QFont()
        font2.setFamilies([u"Jellee"])
        font2.setPointSize(36)
        self.pertanyaan.setFont(font2)
        self.pertanyaan.setCursor(QCursor(Qt.PointingHandCursor))
        self.pertanyaan.setStyleSheet(u"QLabel {\n"
"    background-color: transparent; /* Background transparan */\n"
"	color: white;\n"
"}")
        self.pertanyaan.setScaledContents(False)
        self.pertanyaan.setWordWrap(True)
        self.background = QLabel(self.Flashcard)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(89, 50, 581, 801))
        self.background.setCursor(QCursor(Qt.PointingHandCursor))
        self.background.setStyleSheet(u"QLabel#background {\n"
"	background: transparent;\n"
"}")
        self.background.setPixmap(QPixmap(u"Middlebar/Background Flashcard 1.png"))
        self.background.setScaledContents(True)
        self.image = QLabel(self.Flashcard)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(180, 220, 411, 481))
        self.image.setMaximumSize(QSize(500, 500))
        self.image.setFont(font2)
        self.image.setCursor(QCursor(Qt.PointingHandCursor))
        self.image.setStyleSheet(u"QLabel {\n"
"    background-color: transparent; /* Background transparan */\n"
"	color: white;\n"
"}")
        self.image.setPixmap(QPixmap(u"Middlebar/image v2.png"))
        self.image.setScaledContents(False)
        self.image.setWordWrap(True)
        self.jawaban = QLabel(self.Flashcard)
        self.jawaban.setObjectName(u"jawaban")
        self.jawaban.setGeometry(QRect(180, 700, 401, 111))
        self.jawaban.setMaximumSize(QSize(500, 200))
        font3 = QFont()
        font3.setFamilies([u"Jellee"])
        font3.setPointSize(20)
        self.jawaban.setFont(font3)
        self.jawaban.setCursor(QCursor(Qt.PointingHandCursor))
        self.jawaban.setStyleSheet(u"QLabel {\n"
"    background-color: transparent; /* Background transparan */\n"
"	color: #15387C;\n"
"}")
        self.jawaban.setScaledContents(False)
        self.jawaban.setWordWrap(True)
        self.pertanyaan_2 = QLabel(self.Flashcard)
        self.pertanyaan_2.setObjectName(u"pertanyaan_2")
        self.pertanyaan_2.setGeometry(QRect(40, 10, 681, 881))
        self.pertanyaan_2.setMaximumSize(QSize(16777215, 16777215))
        self.pertanyaan_2.setFont(font2)
        self.pertanyaan_2.setStyleSheet(u"QLabel {\n"
"    background-color: transparent; /* Background transparan */\n"
"	color: white;\n"
"}")
        self.pertanyaan_2.setPixmap(QPixmap(u"Middlebar/Dekorasi.png"))
        self.pertanyaan_2.setScaledContents(True)
        self.pertanyaan_2.setWordWrap(True)
        self.label_10 = QLabel(self.Flashcard)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(240, 750, 311, 41))
        font4 = QFont()
        font4.setFamilies([u"Jellee"])
        font4.setPointSize(22)
        self.label_10.setFont(font4)
        self.label_10.setPixmap(QPixmap(u"Middlebar/Tambah Flashcard.png"))
        self.pertanyaan_2.raise_()
        self.background.raise_()
        self.pertanyaan.raise_()
        self.image.raise_()
        self.jawaban.raise_()
        self.label_10.raise_()
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 130, 1011, 791))
        self.label.setPixmap(QPixmap(u"Middlebar/Background Atur.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 160, 261, 51))
        self.label_2.setPixmap(QPixmap(u"Middlebar/PopUp Kembali.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(670, 150, 350, 41))
        self.label_3.setPixmap(QPixmap(u"Middlebar/FlashCard Baru.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 250, 401, 461))
        self.label_4.setStyleSheet(u"QLabel {\n"
"\n"
"	background-color: blue;\n"
"	border-radius: 20px;\n"
"}")
        self.label_4.setScaledContents(True)
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(100, 270, 361, 71))
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"	color: red;\n"
"}")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(600, 250, 401, 461))
        self.label_5.setStyleSheet(u"QLabel {\n"
"\n"
"	background-color: blue;\n"
"	border-radius: 30px;\n"
"}")
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(620, 270, 331, 71))
        self.label_6.setFont(font3)
        self.label_6.setWordWrap(True)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(100, 650, 361, 31))
        font5 = QFont()
        font5.setFamilies([u"Jellee"])
        font5.setPointSize(18)
        self.label_7.setFont(font5)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(220, 740, 91, 31))
        self.label_8.setFont(font4)
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(730, 740, 131, 41))
        self.label_9.setFont(font4)
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(620, 650, 361, 31))
        self.label_11.setFont(font5)
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(100, 360, 361, 261))
        self.label_12.setPixmap(QPixmap(u"Middlebar/image v2.png"))
        self.label_12.setScaledContents(True)
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(620, 360, 361, 261))
        self.label_13.setPixmap(QPixmap(u"Middlebar/image v2.png"))
        self.label_13.setScaledContents(True)
        self.label.raise_()
        self.Flashcard.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_11.raise_()
        self.textEdit.raise_()
        self.label_12.raise_()
        self.label_13.raise_()

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(400, 1080))
        self.frame_3.setStyleSheet(u"QFrame {\n"
"    background-color: #EAEAEA;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.Progress = QWidget(self.frame_3)
        self.Progress.setObjectName(u"Progress")
        self.Progress.setGeometry(QRect(10, 100, 381, 161))
        self.Progress.setStyleSheet(u"QWidget#Progress{\n"
"	background-color: white !important;\n"
"	border: 3px solid rgb(204, 204, 204) ;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 0px;\n"
"	color: #585858;\n"
"}")
        self.header = QLabel(self.Progress)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(20, 20, 311, 31))
        font6 = QFont()
        font6.setFamilies([u"Jellee Roman"])
        font6.setPointSize(18)
        self.header.setFont(font6)
        self.header.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.counter = QLabel(self.Progress)
        self.counter.setObjectName(u"counter")
        self.counter.setGeometry(QRect(290, 80, 61, 41))
        font7 = QFont()
        font7.setFamilies([u"Jellee Roman"])
        font7.setPointSize(20)
        self.counter.setFont(font7)
        self.counter.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.progressBar = QProgressBar(self.Progress)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 80, 241, 41))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    background: #E0E0E0;\n"
"	border-radius: 20px;\n"
"    text-align: center;\n"
"	color: transparent;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #843DB0;\n"
"	border-radius: 18px;\n"
"	margin: 2px;\n"
"}\n"
"")
        self.progressBar.setValue(24)
        self.Atur = QWidget(self.frame_3)
        self.Atur.setObjectName(u"Atur")
        self.Atur.setGeometry(QRect(10, 480, 381, 151))
        self.Atur.setStyleSheet(u"QWidget#Atur{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(204, 204, 204) ;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 0px;\n"
"	color: #585858;\n"
"}")
        self.header_2 = QLabel(self.Atur)
        self.header_2.setObjectName(u"header_2")
        self.header_2.setGeometry(QRect(20, 20, 311, 31))
        self.header_2.setFont(font6)
        self.header_2.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.toolButton = QToolButton(self.Atur)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(10, 70, 361, 71))
        self.toolButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.toolButton.setStyleSheet(u"QToolButton {\n"
"	background: transparent;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"Rightbar/Atur Button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QSize(1000, 1000))
        self.pushButton = QPushButton(self.Atur)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 10, 75, 24))
        self.layoutWidget = QWidget(self.frame_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 20, 321, 44))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setSpacing(9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Jepang = QLabel(self.layoutWidget)
        self.Jepang.setObjectName(u"Jepang")
        self.Jepang.setMaximumSize(QSize(100, 16777215))
        self.Jepang.setPixmap(QPixmap(u"Rightbar/Logo Jepang.png"))
        self.Jepang.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.Jepang)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.api = QLabel(self.layoutWidget)
        self.api.setObjectName(u"api")
        self.api.setPixmap(QPixmap(u"Rightbar/Streak.png"))
        self.api.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.api)

        self.angka = QLabel(self.layoutWidget)
        self.angka.setObjectName(u"angka")
        self.angka.setFont(font5)
        self.angka.setStyleSheet(u"QLabel {\n"
"	color: #C3C3C3;\n"
"}")

        self.horizontalLayout_3.addWidget(self.angka)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.segitiga = QLabel(self.layoutWidget)
        self.segitiga.setObjectName(u"segitiga")
        self.segitiga.setMinimumSize(QSize(40, 0))
        self.segitiga.setMaximumSize(QSize(40, 16777215))
        self.segitiga.setPixmap(QPixmap(u"Rightbar/Points.png"))
        self.segitiga.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.segitiga)

        self.angka_2 = QLabel(self.layoutWidget)
        self.angka_2.setObjectName(u"angka_2")
        self.angka_2.setFont(font5)
        self.angka_2.setStyleSheet(u"QLabel {\n"
"	color: #E16834;\n"
"}")

        self.horizontalLayout_5.addWidget(self.angka_2)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Star = QLabel(self.layoutWidget)
        self.Star.setObjectName(u"Star")
        self.Star.setMaximumSize(QSize(200, 100))
        self.Star.setPixmap(QPixmap(u"Rightbar/Stars.png"))
        self.Star.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.Star)

        self.Stars_count = QLabel(self.layoutWidget)
        self.Stars_count.setObjectName(u"Stars_count")
        self.Stars_count.setFont(font7)
        self.Stars_count.setStyleSheet(u"QLabel#Stars_count{\n"
"color : rgb(85, 153, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.Stars_count)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)

        self.Urutan = QWidget(self.frame_3)
        self.Urutan.setObjectName(u"Urutan")
        self.Urutan.setGeometry(QRect(10, 290, 381, 151))
        self.Urutan.setStyleSheet(u"QWidget#Urutan{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(204, 204, 204) ;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 0px;\n"
"	color: #585858;\n"
"}")
        self.header_3 = QLabel(self.Urutan)
        self.header_3.setObjectName(u"header_3")
        self.header_3.setGeometry(QRect(20, 20, 311, 31))
        self.header_3.setFont(font6)
        self.header_3.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.dropdown = QPushButton(self.Urutan)
        self.dropdown.setObjectName(u"dropdown")
        self.dropdown.setGeometry(QRect(15, 60, 341, 61))
        self.dropdown.setFont(font3)
        self.dropdown.setCursor(QCursor(Qt.PointingHandCursor))
        self.dropdown.setStyleSheet(u"QPushButton {\n"
"	color: #313131;\n"
"	text-align: left;\n"
"	background-color: white;\n"
"	border: 5px solid #CCCCCC;\n"
"	border-radius: 15px;\n"
"	padding: 10px;\n"
"  	overflow: hidden;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"Rightbar/Icon Dropdown.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dropdown.setIcon(icon2)
        self.dropdown.setCheckable(True)
        self.dropdown.raise_()
        self.header_3.raise_()
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(30, 415, 341, 230))
        self.frame_4.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 0px;\n"
"	color: #585858;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: #313131;\n"
"	text-align: left;\n"
"	background-color: white;\n"
"	border: 0px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.urutan_2 = QPushButton(self.frame_4)
        self.urutan_2.setObjectName(u"urutan_2")
        self.urutan_2.setGeometry(QRect(20, 10, 301, 61))
        self.urutan_2.setFont(font3)
        self.urutan_2.setStyleSheet(u"")
        self.urutan_3 = QPushButton(self.frame_4)
        self.urutan_3.setObjectName(u"urutan_3")
        self.urutan_3.setGeometry(QRect(20, 60, 301, 61))
        self.urutan_3.setFont(font3)
        self.urutan_3.setStyleSheet(u"")
        self.urutan_4 = QPushButton(self.frame_4)
        self.urutan_4.setObjectName(u"urutan_4")
        self.urutan_4.setGeometry(QRect(20, 110, 301, 61))
        self.urutan_4.setFont(font3)
        self.urutan_4.setStyleSheet(u"")
        self.urutan_5 = QPushButton(self.frame_4)
        self.urutan_5.setObjectName(u"urutan_5")
        self.urutan_5.setGeometry(QRect(20, 160, 301, 61))
        self.urutan_5.setFont(font3)
        self.urutan_5.setStyleSheet(u"")
        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(-10, 680, 361, 71))
        self.comboBox.setFont(font3)
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"	color: #313131;\n"
"	text-align: left;\n"
"	background-color: white;\n"
"	border: 5px solid #CCCCCC;\n"
"	border-radius: 15px;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.dropdown.toggled.connect(self.frame_4.setHidden)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Next_button_island_6.setText("")
        self.logo.setText(QCoreApplication.translate("MainWindow", u"duahasa", None))
        self.flashcard_active.setText("")
        self.belajar.setText("")
        self.pilihan_ganda.setText("")
        self.pertanyaan.setText(QCoreApplication.translate("MainWindow", u"Apa yang sedang dia lakukan?", None))
        self.background.setText("")
        self.image.setText("")
        self.jawaban.setText(QCoreApplication.translate("MainWindow", u"Tekan untuk melihat jawaban", None))
        self.pertanyaan_2.setText("")
        self.label_10.setText("")
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ini adalh contoh</p></body></html>", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Apa nama buah di bawah ini?", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tekan untuk melihat jawaban", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Depan", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Belakang", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Tekan untuk melihat jawaban", None))
        self.label_12.setText("")
        self.label_13.setText("")
        self.header.setText(QCoreApplication.translate("MainWindow", u"Progress Flashcard Kamu", None))
        self.counter.setText(QCoreApplication.translate("MainWindow", u"3/10", None))
        self.header_2.setText(QCoreApplication.translate("MainWindow", u"Atur Flashcard Kamu", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Jepang.setText("")
        self.api.setText("")
        self.angka.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.segitiga.setText("")
        self.angka_2.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.Star.setText("")
        self.Stars_count.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.header_3.setText(QCoreApplication.translate("MainWindow", u"Urutan Kartu", None))
        self.dropdown.setText(QCoreApplication.translate("MainWindow", u"Kartu 1 - Apa yang sedang dia lakukan", None))
        self.urutan_2.setText(QCoreApplication.translate("MainWindow", u"Kartu 1 - Apa yang sedang dia lakukan", None))
        self.urutan_3.setText(QCoreApplication.translate("MainWindow", u"Kartu 1 - Apa yang sedang dia lakukan", None))
        self.urutan_4.setText(QCoreApplication.translate("MainWindow", u"Kartu 1 - Apa yang sedang dia lakukan", None))
        self.urutan_5.setText(QCoreApplication.translate("MainWindow", u"Kartu 1 - Apa yang sedang dia lakukan", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Kartu 1 - Apa yang sedang dia lakukan?", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Kartu 3 - Bagaimana cara dia melakukan hal tersebut?", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Kartu 2 - Kenapa kamu melakukan hal tersebut?", None))

    # retranslateUi

