# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashboardOVQQpq.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
    QMainWindow, QProgressBar, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)

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
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Left_bar = QFrame(self.centralwidget)
        self.Left_bar.setObjectName(u"Left_bar")
        self.Left_bar.setMaximumSize(QSize(404, 1080))
        self.Left_bar.setToolTipDuration(2)
        self.Left_bar.setAutoFillBackground(False)
        self.Left_bar.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px\n"
"}\n"
"")
        self.Left_bar.setFrameShape(QFrame.StyledPanel)
        self.Left_bar.setFrameShadow(QFrame.Raised)
        self.Next_button_island_6 = QToolButton(self.Left_bar)
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
        icon.addFile(u"../Documents/Project/DuaHasa/Assets/Dashboard/Left_bar/KELUAR.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Next_button_island_6.setIcon(icon)
        self.Next_button_island_6.setIconSize(QSize(1000, 1000))
        self.Next_button_island_6.setCheckable(False)
        self.Next_button_island_6.setAutoRepeat(False)
        self.Next_button_island_6.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Next_button_island_6.setAutoRaise(False)
        self.logo = QLabel(self.Left_bar)
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
        self.belajar = QLabel(self.Left_bar)
        self.belajar.setObjectName(u"belajar")
        self.belajar.setGeometry(QRect(19, 130, 340, 97))
        self.belajar.setMaximumSize(QSize(340, 100))
        self.belajar.setStyleSheet(u"QLabel {\n"
"padding : 20px;\n"
"\n"
"}")
        self.belajar.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Dashboard/Left_bar/Learning_active.png"))
        self.belajar.setScaledContents(False)
        self.flashcard = QLabel(self.Left_bar)
        self.flashcard.setObjectName(u"flashcard")
        self.flashcard.setGeometry(QRect(40, 220, 291, 60))
        self.flashcard.setMaximumSize(QSize(291, 60))
        self.flashcard.setStyleSheet(u"QLabel {\n"
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
        self.flashcard.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Dashboard/Left_bar/Flashcards.png"))
        self.flashcard.setScaledContents(False)
        self.pilihan_ganda = QLabel(self.Left_bar)
        self.pilihan_ganda.setObjectName(u"pilihan_ganda")
        self.pilihan_ganda.setGeometry(QRect(40, 290, 291, 60))
        self.pilihan_ganda.setMaximumSize(QSize(291, 60))
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
        self.pilihan_ganda.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Dashboard/Left_bar/MULTIPLE_CHOICE.png"))

        self.horizontalLayout.addWidget(self.Left_bar)

        self.Main_konten = QFrame(self.centralwidget)
        self.Main_konten.setObjectName(u"Main_konten")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main_konten.sizePolicy().hasHeightForWidth())
        self.Main_konten.setSizePolicy(sizePolicy)
        self.Main_konten.setMaximumSize(QSize(2000, 1080))
        self.Main_konten.setStyleSheet(u"QFrame {\n"
"    background-color: #EAEAEA;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}")
        self.Sesi = QWidget(self.Main_konten)
        self.Sesi.setObjectName(u"Sesi")
        self.Sesi.setGeometry(QRect(90, 30, 921, 121))
        self.Sesi.setMaximumSize(QSize(1920, 1080))
        self.Sesi.setAcceptDrops(False)
        self.Sesi.setStyleSheet(u"QWidget {\n"
"    background-color: #E36B37;\n"
"    border: 1px solid #E36B37;  \n"
"    border-radius: 20px;\n"
"}")
        self.layoutWidget = QWidget(self.Sesi)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 20, 581, 72))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Back_Button = QLabel(self.layoutWidget)
        self.Back_Button.setObjectName(u"Back_Button")
        self.Back_Button.setMaximumSize(QSize(30, 16777215))
        self.Back_Button.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Dashboard/Sesi/Backspace.png"))

        self.horizontalLayout_2.addWidget(self.Back_Button)

        self.Text_sesi = QLabel(self.layoutWidget)
        self.Text_sesi.setObjectName(u"Text_sesi")
        font2 = QFont()
        font2.setFamilies([u"Jellee Roman"])
        font2.setPointSize(16)
        self.Text_sesi.setFont(font2)
        self.Text_sesi.setStyleSheet(u"QLabel{\n"
"color:rgb(255, 199, 174)\n"
"};")

        self.horizontalLayout_2.addWidget(self.Text_sesi)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.Text_Pembelajaran = QLabel(self.layoutWidget)
        self.Text_Pembelajaran.setObjectName(u"Text_Pembelajaran")
        font3 = QFont()
        font3.setFamilies([u"Jellee Roman"])
        font3.setPointSize(20)
        font3.setBold(False)
        self.Text_Pembelajaran.setFont(font3)
        self.Text_Pembelajaran.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"};")

        self.verticalLayout_2.addWidget(self.Text_Pembelajaran)

        self.btn_panduan = QToolButton(self.Sesi)
        self.btn_panduan.setObjectName(u"btn_panduan")
        self.btn_panduan.setGeometry(QRect(700, 20, 181, 71))
        self.btn_panduan.setContextMenuPolicy(Qt.NoContextMenu)
        icon1 = QIcon()
        icon1.addFile(u"../Documents/Project/DuaHasa/Assets/Dashboard/Sesi/Panduan.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_panduan.setIcon(icon1)
        self.btn_panduan.setIconSize(QSize(1000, 1000))
        self.btn_panduan.setCheckable(True)
        self.Land_2 = QLabel(self.Main_konten)
        self.Land_2.setObjectName(u"Land_2")
        self.Land_2.setGeometry(QRect(410, 650, 471, 321))
        self.Land_2.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Dashboard/Island/Island_2.png"))
        self.Land_2.setScaledContents(True)
        self.Land_1 = QLabel(self.Main_konten)
        self.Land_1.setObjectName(u"Land_1")
        self.Land_1.setGeometry(QRect(150, 170, 701, 461))
        self.Land_1.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Dashboard/Island/Island_1.png"))
        self.Land_1.setScaledContents(True)
        self.Tangga = QLabel(self.Main_konten)
        self.Tangga.setObjectName(u"Tangga")
        self.Tangga.setGeometry(QRect(420, 500, 141, 191))
        self.Tangga.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"}")
        self.Tangga.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Dashboard/Island/Ladder.png"))
        self.Tangga.setScaledContents(True)
        self.Start_btn = QToolButton(self.Main_konten)
        self.Start_btn.setObjectName(u"Start_btn")
        self.Start_btn.setGeometry(QRect(560, 240, 181, 191))
        self.Start_btn.setMaximumSize(QSize(1000, 1000))
        self.Start_btn.setContextMenuPolicy(Qt.NoContextMenu)
        self.Start_btn.setAutoFillBackground(False)
        self.Start_btn.setStyleSheet(u"QToolButton {\n"
"    border: none;                  /* Menghilangkan border */\n"
"    background: transparent;       /* Membuat background transparan */\n"
"    padding: 0;                    /* Menghilangkan padding */\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../Documents/Project/DuaHasa/Assets/Dashboard/Island/Start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Start_btn.setIcon(icon2)
        self.Start_btn.setIconSize(QSize(500, 500))
        self.Start_btn.setCheckable(True)
        self.Start_btn.setAutoRepeat(False)
        self.Start_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Start_btn.setAutoRaise(False)
        self.Next_button_island = QToolButton(self.Main_konten)
        self.Next_button_island.setObjectName(u"Next_button_island")
        self.Next_button_island.setGeometry(QRect(490, 380, 71, 71))
        self.Next_button_island.setMaximumSize(QSize(100, 100))
        self.Next_button_island.setFont(font)
        self.Next_button_island.setContextMenuPolicy(Qt.NoContextMenu)
        self.Next_button_island.setAutoFillBackground(False)
        self.Next_button_island.setStyleSheet(u"QToolButton {\n"
"    border: none;                  /* Menghilangkan border */\n"
"    background: transparent;       /* Membuat background transparan */\n"
"    padding: 0;                    /* Menghilangkan padding */\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../Documents/Project/DuaHasa/Assets/Dashboard/Island/Next_Button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Next_button_island.setIcon(icon3)
        self.Next_button_island.setIconSize(QSize(200, 200))
        self.Next_button_island.setCheckable(False)
        self.Next_button_island.setAutoRepeat(False)
        self.Next_button_island.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Next_button_island.setAutoRaise(False)
        self.Next_button_island_2 = QToolButton(self.Main_konten)
        self.Next_button_island_2.setObjectName(u"Next_button_island_2")
        self.Next_button_island_2.setGeometry(QRect(390, 440, 70, 70))
        self.Next_button_island_2.setMaximumSize(QSize(70, 70))
        self.Next_button_island_2.setFont(font)
        self.Next_button_island_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.Next_button_island_2.setAutoFillBackground(False)
        self.Next_button_island_2.setStyleSheet(u"QToolButton {\n"
"    border: none;                  /* Menghilangkan border */\n"
"    background: transparent;       /* Membuat background transparan */\n"
"    padding: 0;                    /* Menghilangkan padding */\n"
"}\n"
"")
        self.Next_button_island_2.setIcon(icon3)
        self.Next_button_island_2.setIconSize(QSize(200, 200))
        self.Next_button_island_2.setCheckable(False)
        self.Next_button_island_2.setAutoRepeat(False)
        self.Next_button_island_2.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Next_button_island_2.setAutoRaise(False)
        self.Next_button_island_3 = QToolButton(self.Main_konten)
        self.Next_button_island_3.setObjectName(u"Next_button_island_3")
        self.Next_button_island_3.setGeometry(QRect(480, 700, 100, 80))
        self.Next_button_island_3.setMaximumSize(QSize(100, 100))
        self.Next_button_island_3.setFont(font)
        self.Next_button_island_3.setContextMenuPolicy(Qt.NoContextMenu)
        self.Next_button_island_3.setAutoFillBackground(False)
        self.Next_button_island_3.setStyleSheet(u"QToolButton {\n"
"    border: none;                  /* Menghilangkan border */\n"
"    background: transparent;       /* Membuat background transparan */\n"
"    padding: 0;                    /* Menghilangkan padding */\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"../Documents/Project/DuaHasa/Assets/Dashboard/Island/Chest.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Next_button_island_3.setIcon(icon4)
        self.Next_button_island_3.setIconSize(QSize(200, 200))
        self.Next_button_island_3.setCheckable(False)
        self.Next_button_island_3.setAutoRepeat(False)
        self.Next_button_island_3.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Next_button_island_3.setAutoRaise(False)
        self.Next_button_island_4 = QToolButton(self.Main_konten)
        self.Next_button_island_4.setObjectName(u"Next_button_island_4")
        self.Next_button_island_4.setGeometry(QRect(580, 780, 70, 70))
        self.Next_button_island_4.setMaximumSize(QSize(70, 70))
        self.Next_button_island_4.setFont(font)
        self.Next_button_island_4.setContextMenuPolicy(Qt.NoContextMenu)
        self.Next_button_island_4.setAutoFillBackground(False)
        self.Next_button_island_4.setStyleSheet(u"QToolButton {\n"
"    border: none;                  /* Menghilangkan border */\n"
"    background: transparent;       /* Membuat background transparan */\n"
"    padding: 0;                    /* Menghilangkan padding */\n"
"}\n"
"")
        self.Next_button_island_4.setIcon(icon3)
        self.Next_button_island_4.setIconSize(QSize(200, 200))
        self.Next_button_island_4.setCheckable(False)
        self.Next_button_island_4.setAutoRepeat(False)
        self.Next_button_island_4.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Next_button_island_4.setAutoRaise(False)
        self.Next_button_island_5 = QToolButton(self.Main_konten)
        self.Next_button_island_5.setObjectName(u"Next_button_island_5")
        self.Next_button_island_5.setGeometry(QRect(690, 810, 70, 70))
        self.Next_button_island_5.setMaximumSize(QSize(70, 70))
        self.Next_button_island_5.setFont(font)
        self.Next_button_island_5.setContextMenuPolicy(Qt.NoContextMenu)
        self.Next_button_island_5.setAutoFillBackground(False)
        self.Next_button_island_5.setStyleSheet(u"QToolButton {\n"
"    border: none;                  /* Menghilangkan border */\n"
"    background: transparent;       /* Membuat background transparan */\n"
"    padding: 0;                    /* Menghilangkan padding */\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"../Documents/Project/DuaHasa/Assets/Dashboard/Island/Finish_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Next_button_island_5.setIcon(icon5)
        self.Next_button_island_5.setIconSize(QSize(200, 200))
        self.Next_button_island_5.setCheckable(False)
        self.Next_button_island_5.setAutoRepeat(False)
        self.Next_button_island_5.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Next_button_island_5.setAutoRaise(False)
        self.Maskot_monyet_island = QLabel(self.Main_konten)
        self.Maskot_monyet_island.setObjectName(u"Maskot_monyet_island")
        self.Maskot_monyet_island.setGeometry(QRect(270, 200, 231, 211))
        self.Maskot_monyet_island.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;  /* Membuat background transparan */\n"
"    border: none;                   /* Menghilangkan border */\n"
"}\n"
"")
        self.Maskot_monyet_island.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Dashboard/Island/maskot_island.png"))
        self.Maskot_monyet_island.setScaledContents(True)
        self.RightBar = QWidget(self.Main_konten)
        self.RightBar.setObjectName(u"RightBar")
        self.RightBar.setGeometry(QRect(1090, 0, 400, 1062))
        self.RightBar.setMaximumSize(QSize(400, 1080))
        self.RightBar.setStyleSheet(u"QFrame {\n"
"    background-color: #EAEAEA;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}")
        self.Progres = QWidget(self.RightBar)
        self.Progres.setObjectName(u"Progres")
        self.Progres.setGeometry(QRect(10, 140, 381, 251))
        self.Progres.setStyleSheet(u"QWidget#Progres{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(204, 204, 204) ;\n"
"    border-radius: 20px;\n"
"}")
        self.Progress_belajar = QLabel(self.Progres)
        self.Progress_belajar.setObjectName(u"Progress_belajar")
        self.Progress_belajar.setGeometry(QRect(20, 20, 311, 31))
        font4 = QFont()
        font4.setFamilies([u"Jellee Roman"])
        font4.setPointSize(18)
        self.Progress_belajar.setFont(font4)
        self.Progress_belajar.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.progressBar = QProgressBar(self.Progres)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 90, 271, 21))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    background: #E0E0E0;\n"
"    border-radius: 10px;  /* Mengatur border radius lebih kecil */\n"
"    text-align: center;\n"
"    color: transparent;\n"
"    height: 8px;  /* Mengatur tinggi QProgressBar agar lebih slim */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #5AD2E2;\n"
"    border-radius: 10px;  /* Mengatur border radius untuk chunk */\n"
"    margin: 0px;  /* Mengatur margin untuk jarak antar chunk */\n"
"}")
        self.progressBar.setValue(24)
        self.Count_materi = QLabel(self.Progres)
        self.Count_materi.setObjectName(u"Count_materi")
        self.Count_materi.setGeometry(QRect(300, 80, 61, 41))
        self.Count_materi.setFont(font4)
        self.Count_materi.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.motivasi = QLabel(self.Progres)
        self.motivasi.setObjectName(u"motivasi")
        self.motivasi.setGeometry(QRect(30, 140, 311, 31))
        font5 = QFont()
        font5.setFamilies([u"Jellee Roman"])
        font5.setPointSize(13)
        self.motivasi.setFont(font5)
        self.motivasi.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.label_17 = QLabel(self.Progres)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(30, 180, 321, 51))
        self.label_17.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;  /* Membuat background transparan */\n"
"}\n"
"")
        self.label_17.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Dashboard/Right_bar/Button_Belajar.png"))
        self.label_17.setScaledContents(True)
        self.progressBar.raise_()
        self.label_17.raise_()
        self.Progress_belajar.raise_()
        self.motivasi.raise_()
        self.Count_materi.raise_()
        self.Iklan = QWidget(self.RightBar)
        self.Iklan.setObjectName(u"Iklan")
        self.Iklan.setGeometry(QRect(10, 420, 381, 231))
        self.Iklan.setStyleSheet(u"QWidget#Iklan{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(204, 204, 204) ;\n"
"    border-radius: 20px;\n"
"}")
        self.karakter = QLabel(self.Iklan)
        self.karakter.setObjectName(u"karakter")
        self.karakter.setGeometry(QRect(20, -30, 341, 271))
        font6 = QFont()
        font6.setPointSize(1)
        self.karakter.setFont(font6)
        self.karakter.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;  /* Membuat background transparan */\n"
"}\n"
"")
        self.karakter.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Dashboard/Right_bar/Card2.png"))
        self.karakter.setScaledContents(True)
        self.Profile = QWidget(self.RightBar)
        self.Profile.setObjectName(u"Profile")
        self.Profile.setGeometry(QRect(10, 680, 381, 151))
        self.Profile.setStyleSheet(u"QWidget#Profile{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(204, 204, 204) ;\n"
"    border-radius: 20px;\n"
"}")
        self.hd_iklan_2 = QLabel(self.Profile)
        self.hd_iklan_2.setObjectName(u"hd_iklan_2")
        self.hd_iklan_2.setGeometry(QRect(30, 20, 311, 31))
        self.hd_iklan_2.setFont(font4)
        self.hd_iklan_2.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.b_profile = QLabel(self.Profile)
        self.b_profile.setObjectName(u"b_profile")
        self.b_profile.setGeometry(QRect(40, 70, 311, 51))
        self.b_profile.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;  /* Membuat background transparan */\n"
"}\n"
"")
        self.b_profile.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Dashboard/Right_bar/Profile.png"))
        self.b_profile.setScaledContents(True)
        self.layoutWidget1 = QWidget(self.RightBar)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 20, 321, 44))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setSpacing(9)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Jepang = QLabel(self.layoutWidget1)
        self.Jepang.setObjectName(u"Jepang")
        self.Jepang.setMaximumSize(QSize(100, 16777215))
        self.Jepang.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Dashboard/Right_bar/bendera_jepang.png"))
        self.Jepang.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.Jepang)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.api = QLabel(self.layoutWidget1)
        self.api.setObjectName(u"api")
        self.api.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Streak.png"))
        self.api.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.api)

        self.angka = QLabel(self.layoutWidget1)
        self.angka.setObjectName(u"angka")
        font7 = QFont()
        font7.setFamilies([u"Jellee"])
        font7.setPointSize(18)
        self.angka.setFont(font7)
        self.angka.setStyleSheet(u"QLabel {\n"
"	color: #C3C3C3;\n"
"}")

        self.horizontalLayout_3.addWidget(self.angka)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.segitiga = QLabel(self.layoutWidget1)
        self.segitiga.setObjectName(u"segitiga")
        self.segitiga.setMinimumSize(QSize(40, 0))
        self.segitiga.setMaximumSize(QSize(40, 16777215))
        self.segitiga.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Points.png"))
        self.segitiga.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.segitiga)

        self.angka_2 = QLabel(self.layoutWidget1)
        self.angka_2.setObjectName(u"angka_2")
        self.angka_2.setFont(font7)
        self.angka_2.setStyleSheet(u"QLabel {\n"
"	color: #E16834;\n"
"}")

        self.horizontalLayout_5.addWidget(self.angka_2)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Star = QLabel(self.layoutWidget1)
        self.Star.setObjectName(u"Star")
        self.Star.setMaximumSize(QSize(200, 100))
        self.Star.setPixmap(QPixmap(u"../Documents/Project/DuaHasa/Assets/Dashboard/Right_bar/Star.png"))
        self.Star.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.Star)

        self.Stars_count = QLabel(self.layoutWidget1)
        self.Stars_count.setObjectName(u"Stars_count")
        font8 = QFont()
        font8.setFamilies([u"Jellee Roman"])
        font8.setPointSize(20)
        self.Stars_count.setFont(font8)
        self.Stars_count.setStyleSheet(u"QLabel#Stars_count{\n"
"color : rgb(85, 153, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.Stars_count)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)

        self.Pop_up_bacground_2 = QWidget(self.Main_konten)
        self.Pop_up_bacground_2.setObjectName(u"Pop_up_bacground_2")
        self.Pop_up_bacground_2.setGeometry(QRect(-1, -1, 1501, 1061))
        self.Pop_up_bacground_2.setStyleSheet(u" background-color: rgba(0, 0, 0, 128); /* Black background with 50% opacity */")
        self.Pop_up_mulai = QWidget(self.Pop_up_bacground_2)
        self.Pop_up_mulai.setObjectName(u"Pop_up_mulai")
        self.Pop_up_mulai.setEnabled(True)
        self.Pop_up_mulai.setGeometry(QRect(200, 120, 1141, 700))
        self.Pop_up_mulai.setMaximumSize(QSize(1142, 700))
        self.Pop_up_mulai.setStyleSheet(u" QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"            border-radius: 30px;        /* Border radius for rounded corners */\n"
"}")
        self.Kembali_popup_2 = QToolButton(self.Pop_up_mulai)
        self.Kembali_popup_2.setObjectName(u"Kembali_popup_2")
        self.Kembali_popup_2.setGeometry(QRect(40, 30, 151, 61))
        self.Kembali_popup_2.setContextMenuPolicy(Qt.NoContextMenu)
        icon8 = QIcon()
        icon8.addFile(u"../Documents/Project/DuaHasa/Assets/Dashboard/Kembali_popup_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Kembali_popup_2.setIcon(icon8)
        self.Kembali_popup_2.setIconSize(QSize(1000, 1000))
        self.Kembali_popup_2.setCheckable(True)
        self.Icon_popup_belajar = QToolButton(self.Pop_up_mulai)
        self.Icon_popup_belajar.setObjectName(u"Icon_popup_belajar")
        self.Icon_popup_belajar.setGeometry(QRect(440, 30, 401, 61))
        self.Icon_popup_belajar.setContextMenuPolicy(Qt.NoContextMenu)
        icon9 = QIcon()
        icon9.addFile(u"../Documents/Project/DuaHasa/Assets/Dashboard/Mulai_belajar_popup1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Icon_popup_belajar.setIcon(icon9)
        self.Icon_popup_belajar.setIconSize(QSize(1000, 1000))
        self.Flash_card_popup = QToolButton(self.Pop_up_mulai)
        self.Flash_card_popup.setObjectName(u"Flash_card_popup")
        self.Flash_card_popup.setGeometry(QRect(110, 120, 431, 481))
        self.Flash_card_popup.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u"../Documents/Project/DuaHasa/Assets/Dashboard/Flash_card_belajar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Flash_card_popup.setIcon(icon10)
        self.Flash_card_popup.setIconSize(QSize(1000, 1000))
        self.Pilihan_ganda_popup = QToolButton(self.Pop_up_mulai)
        self.Pilihan_ganda_popup.setObjectName(u"Pilihan_ganda_popup")
        self.Pilihan_ganda_popup.setGeometry(QRect(610, 120, 430, 481))
        self.Pilihan_ganda_popup.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u"../Documents/Project/DuaHasa/Assets/Dashboard/Pilihan_ganda_popup.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Pilihan_ganda_popup.setIcon(icon11)
        self.Pilihan_ganda_popup.setIconSize(QSize(1000, 1000))
        self.Sesi.raise_()
        self.Land_2.raise_()
        self.Land_1.raise_()
        self.Tangga.raise_()
        self.Next_button_island_4.raise_()
        self.Next_button_island.raise_()
        self.Next_button_island_3.raise_()
        self.Next_button_island_2.raise_()
        self.Next_button_island_5.raise_()
        self.Start_btn.raise_()
        self.Maskot_monyet_island.raise_()
        self.RightBar.raise_()
        self.Pop_up_bacground_2.raise_()

        self.horizontalLayout.addWidget(self.Main_konten)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Start_btn.toggled.connect(self.Pop_up_bacground_2.setVisible)
        self.Start_btn.toggled.connect(self.Pop_up_mulai.setVisible)
        self.Kembali_popup_2.toggled.connect(self.Pop_up_bacground_2.setHidden)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Next_button_island_6.setText("")
        self.logo.setText(QCoreApplication.translate("MainWindow", u"duahasa", None))
        self.belajar.setText("")
        self.flashcard.setText("")
        self.pilihan_ganda.setText("")
        self.Back_Button.setText("")
        self.Text_sesi.setText(QCoreApplication.translate("MainWindow", u"TEXT SESI", None))
        self.Text_Pembelajaran.setText(QCoreApplication.translate("MainWindow", u"Menggunakan Frasa Dasar", None))
        self.btn_panduan.setText("")
        self.Land_2.setText("")
        self.Land_1.setText("")
        self.Tangga.setText("")
        self.Start_btn.setText("")
        self.Next_button_island.setText("")
        self.Next_button_island_2.setText("")
        self.Next_button_island_3.setText("")
        self.Next_button_island_4.setText("")
        self.Next_button_island_5.setText("")
        self.Maskot_monyet_island.setText("")
        self.Progress_belajar.setText(QCoreApplication.translate("MainWindow", u"Progress belajar Kamu", None))
        self.Count_materi.setText(QCoreApplication.translate("MainWindow", u"3/10", None))
        self.motivasi.setText(QCoreApplication.translate("MainWindow", u"Ayo tingkatkan lagi belajarnya!", None))
        self.label_17.setText("")
        self.karakter.setText("")
        self.hd_iklan_2.setText(QCoreApplication.translate("MainWindow", u"Atur Profile Kamu!", None))
        self.b_profile.setText("")
        self.Jepang.setText("")
        self.api.setText("")
        self.angka.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.segitiga.setText("")
        self.angka_2.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.Star.setText("")
        self.Stars_count.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Kembali_popup_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Icon_popup_belajar.setText("")
        self.Flash_card_popup.setText("")
        self.Pilihan_ganda_popup.setText("")
    # retranslateUi

