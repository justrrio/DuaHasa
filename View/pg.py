# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PGvKfvFp.ui'
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
    QMainWindow, QSizePolicy, QToolButton, QWidget)

class Multiplechoice(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMaximumSize(QSize(1920, 1200))
        MainWindow.setCursor(QCursor(Qt.PointingHandCursor))
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
        icon.addFile(u"Assets/Dashboard/Left_bar/KELUAR.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.belajar = QLabel(self.frame)
        self.belajar.setObjectName(u"belajar")
        self.belajar.setGeometry(QRect(19, 130, 340, 97))
        self.belajar.setMaximumSize(QSize(340, 100))
        self.belajar.setStyleSheet(u"QLabel {\n"
"padding : 20px;\n"
"\n"
"}")
        self.belajar.setPixmap(QPixmap(u"Assets/Dashboard/Left_bar/Learning_active.png"))
        self.belajar.setScaledContents(False)
        self.flashcard = QLabel(self.frame)
        self.flashcard.setObjectName(u"flashcard")
        self.flashcard.setGeometry(QRect(40, 220, 291, 60))
        self.flashcard.setMaximumSize(QSize(291, 60))
        self.flashcard.setCursor(QCursor(Qt.ArrowCursor))
        self.flashcard.setStyleSheet(u"QLabel {\n"
"    padding: 10px;                /* Padding dalam label */\n"
"    border: 2px solid transparent; /* Border default transparan */\n"
"    border-radius: 15px;          /* Border radius untuk sudut melengkung */\n"
"    background-color: transparent; /* Background transparan */\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    border: 2px solid #2D8AE0;    /* Warna border saat di-hover */\n"
"\n"
"}\n"
"")
        self.flashcard.setPixmap(QPixmap(u"Assets/Dashboard/Left_bar/Flashcards.png"))
        self.flashcard.setScaledContents(False)
        self.pilihan_ganda = QLabel(self.frame)
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
"\n"
"}\n"
"")
        self.pilihan_ganda.setPixmap(QPixmap(u"Assets/Dashboard/Left_bar/MULTIPLE_CHOICE.png"))

        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QSize(1098, 1080))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"    background-color: #EAEAEA;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.Land_2 = QLabel(self.frame_2)
        self.Land_2.setObjectName(u"Land_2")
        self.Land_2.setGeometry(QRect(410, 650, 471, 321))
        self.Land_2.setPixmap(QPixmap(u"Documents/Project/DuaHasa/Assets/Island 2.png"))
        self.Land_2.setScaledContents(True)
        self.PGFR = QWidget(self.frame_2)
        self.PGFR.setObjectName(u"PGFR")
        self.PGFR.setGeometry(QRect(20, 20, 1031, 921))
        self.PGFR.setAutoFillBackground(False)
        self.PGFR.setStyleSheet(u"QWidget#PGFR{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(204, 204, 204) ;\n"
"border-radius: 20px;\\n\n"
"}")
        self.label_22 = QLabel(self.PGFR)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 20, 321, 31))
        font2 = QFont()
        font2.setFamilies([u"Jellee Roman"])
        font2.setPointSize(16)
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"QLabel{\n"
"color: #585858;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.Jepang_4 = QLabel(self.PGFR)
        self.Jepang_4.setObjectName(u"Jepang_4")
        self.Jepang_4.setGeometry(QRect(20, 60, 269, 285))
        self.Jepang_4.setMinimumSize(QSize(269, 285))
        self.Jepang_4.setMaximumSize(QSize(128, 137))
        self.Jepang_4.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.Jepang_4.setPixmap(QPixmap(u"Assets/PG/monkey.png"))
        self.Jepang_4.setScaledContents(True)
        self.Jepang_5 = QLabel(self.PGFR)
        self.Jepang_5.setObjectName(u"Jepang_5")
        self.Jepang_5.setGeometry(QRect(250, 100, 200, 50))
        self.Jepang_5.setMinimumSize(QSize(50, 50))
        self.Jepang_5.setMaximumSize(QSize(900, 900))
        self.Jepang_5.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.Jepang_5.setPixmap(QPixmap(u"Assets/PG/sl.png"))
        self.Jepang_5.setScaledContents(True)
        self.Jepang_6 = QLabel(self.PGFR)
        self.Jepang_6.setObjectName(u"Jepang_6")
        self.Jepang_6.setGeometry(QRect(30, 360, 950, 3))
        self.Jepang_6.setMinimumSize(QSize(430, 2))
        self.Jepang_6.setMaximumSize(QSize(1000, 137))
        self.Jepang_6.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.Jepang_6.setPixmap(QPixmap(u"Assets/PG/l1.png"))
        self.Jepang_6.setScaledContents(True)
        self.Jepang_7 = QLabel(self.PGFR)
        self.Jepang_7.setObjectName(u"Jepang_7")
        self.Jepang_7.setGeometry(QRect(30, 500, 950, 3))
        self.Jepang_7.setMinimumSize(QSize(430, 2))
        self.Jepang_7.setMaximumSize(QSize(1000, 137))
        self.Jepang_7.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.Jepang_7.setPixmap(QPixmap(u"Assets/PG/l1.png"))
        self.Jepang_7.setScaledContents(True)
        self.Jepang_8 = QLabel(self.PGFR)
        self.Jepang_8.setObjectName(u"Jepang_8")
        self.Jepang_8.setGeometry(QRect(260, 560, 126, 53))
        self.Jepang_8.setMinimumSize(QSize(126, 53))
        self.Jepang_8.setMaximumSize(QSize(126, 53))
        self.Jepang_8.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.Jepang_8.setPixmap(QPixmap(u"Assets/PG/e1.png"))
        self.Jepang_8.setScaledContents(True)
        self.Jepang_9 = QLabel(self.PGFR)
        self.Jepang_9.setObjectName(u"Jepang_9")
        self.Jepang_9.setGeometry(QRect(490, 560, 60, 54))
        self.Jepang_9.setMinimumSize(QSize(60, 54))
        self.Jepang_9.setMaximumSize(QSize(60, 54))
        self.Jepang_9.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.Jepang_9.setPixmap(QPixmap(u"Assets/PG/e2.png"))
        self.Jepang_9.setScaledContents(True)
        self.Jepang_10 = QLabel(self.PGFR)
        self.Jepang_10.setObjectName(u"Jepang_10")
        self.Jepang_10.setGeometry(QRect(640, 560, 104, 54))
        self.Jepang_10.setMinimumSize(QSize(104, 54))
        self.Jepang_10.setMaximumSize(QSize(60, 54))
        self.Jepang_10.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.Jepang_10.setPixmap(QPixmap(u"Assets/PG/e3.png"))
        self.Jepang_10.setScaledContents(True)
        self.Jepang_11 = QLabel(self.PGFR)
        self.Jepang_11.setObjectName(u"Jepang_11")
        self.Jepang_11.setGeometry(QRect(360, 670, 60, 54))
        self.Jepang_11.setMinimumSize(QSize(60, 54))
        self.Jepang_11.setMaximumSize(QSize(60, 54))
        self.Jepang_11.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.Jepang_11.setPixmap(QPixmap(u"Assets/PG/e5.png"))
        self.Jepang_11.setScaledContents(True)
        self.Jepang_12 = QLabel(self.PGFR)
        self.Jepang_12.setObjectName(u"Jepang_12")
        self.Jepang_12.setGeometry(QRect(540, 660, 126, 53))
        self.Jepang_12.setMinimumSize(QSize(126, 53))
        self.Jepang_12.setMaximumSize(QSize(126, 53))
        self.Jepang_12.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.Jepang_12.setPixmap(QPixmap(u"Assets/PG/e1.png"))
        self.Jepang_12.setScaledContents(True)
        self.Next_button_island_9 = QToolButton(self.PGFR)
        self.Next_button_island_9.setObjectName(u"Next_button_island_9")
        self.Next_button_island_9.setGeometry(QRect(220, 550, 211, 81))
        self.Next_button_island_9.setMaximumSize(QSize(1000, 1000))
        self.Next_button_island_9.setFont(font)
        self.Next_button_island_9.setContextMenuPolicy(Qt.NoContextMenu)
        self.Next_button_island_9.setAutoFillBackground(False)
        self.Next_button_island_9.setStyleSheet(u"QToolButton {\n"
"    border: none;                  /* Menghilangkan border */\n"
"    background: transparent;       /* Membuat background transparan */\n"
"    padding: 0;                    /* Menghilangkan padding */\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"Assets/PG/1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Next_button_island_9.setIcon(icon1)
        self.Next_button_island_9.setIconSize(QSize(1000, 1000))
        self.Next_button_island_9.setCheckable(True)
        self.Next_button_island_9.setAutoRepeat(False)
        self.Next_button_island_9.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Next_button_island_9.setAutoRaise(False)
        self.Next_button_island_10 = QToolButton(self.PGFR)
        self.Next_button_island_10.setObjectName(u"Next_button_island_10")
        self.Next_button_island_10.setGeometry(QRect(320, 650, 141, 91))
        self.Next_button_island_10.setMaximumSize(QSize(1000, 1000))
        self.Next_button_island_10.setFont(font)
        self.Next_button_island_10.setContextMenuPolicy(Qt.NoContextMenu)
        self.Next_button_island_10.setAutoFillBackground(False)
        self.Next_button_island_10.setStyleSheet(u"QToolButton {\n"
"    border: none;                  /* Menghilangkan border */\n"
"    background: transparent;       /* Membuat background transparan */\n"
"    padding: 0;                    /* Menghilangkan padding */\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"Assets/PG/2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Next_button_island_10.setIcon(icon2)
        self.Next_button_island_10.setIconSize(QSize(1000, 1000))
        self.Next_button_island_10.setCheckable(True)
        self.Next_button_island_10.setAutoRepeat(False)
        self.Next_button_island_10.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Next_button_island_10.setAutoRaise(False)
        self.Next_button_island_11 = QToolButton(self.PGFR)
        self.Next_button_island_11.setObjectName(u"Next_button_island_11")
        self.Next_button_island_11.setGeometry(QRect(420, 550, 191, 81))
        self.Next_button_island_11.setMaximumSize(QSize(1000, 1000))
        self.Next_button_island_11.setFont(font)
        self.Next_button_island_11.setContextMenuPolicy(Qt.NoContextMenu)
        self.Next_button_island_11.setAutoFillBackground(False)
        self.Next_button_island_11.setStyleSheet(u"QToolButton {\n"
"    border: none;                  /* Menghilangkan border */\n"
"    background: transparent;       /* Membuat background transparan */\n"
"    padding: 0;                    /* Menghilangkan padding */\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"Assets/PG/3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Next_button_island_11.setIcon(icon3)
        self.Next_button_island_11.setIconSize(QSize(1000, 1000))
        self.Next_button_island_11.setCheckable(True)
        self.Next_button_island_11.setAutoRepeat(False)
        self.Next_button_island_11.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Next_button_island_11.setAutoRaise(False)
        self.Next_button_island_12 = QToolButton(self.PGFR)
        self.Next_button_island_12.setObjectName(u"Next_button_island_12")
        self.Next_button_island_12.setGeometry(QRect(500, 650, 201, 81))
        self.Next_button_island_12.setMaximumSize(QSize(1000, 1000))
        self.Next_button_island_12.setFont(font)
        self.Next_button_island_12.setContextMenuPolicy(Qt.NoContextMenu)
        self.Next_button_island_12.setAutoFillBackground(False)
        self.Next_button_island_12.setStyleSheet(u"QToolButton {\n"
"    border: none;                  /* Menghilangkan border */\n"
"    background: transparent;       /* Membuat background transparan */\n"
"    padding: 0;                    /* Menghilangkan padding */\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"Assets/PG/4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Next_button_island_12.setIcon(icon4)
        self.Next_button_island_12.setIconSize(QSize(1000, 1000))
        self.Next_button_island_12.setCheckable(True)
        self.Next_button_island_12.setAutoRepeat(False)
        self.Next_button_island_12.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Next_button_island_12.setAutoRaise(False)
        self.Next_button_island_13 = QToolButton(self.PGFR)
        self.Next_button_island_13.setObjectName(u"Next_button_island_13")
        self.Next_button_island_13.setGeometry(QRect(560, 550, 271, 81))
        self.Next_button_island_13.setMaximumSize(QSize(1000, 1000))
        self.Next_button_island_13.setFont(font)
        self.Next_button_island_13.setContextMenuPolicy(Qt.NoContextMenu)
        self.Next_button_island_13.setAutoFillBackground(False)
        self.Next_button_island_13.setStyleSheet(u"QToolButton {\n"
"    border: none;                  /* Menghilangkan border */\n"
"    background: transparent;       /* Membuat background transparan */\n"
"    padding: 0;                    /* Menghilangkan padding */\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"Assets/PG/5.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Next_button_island_13.setIcon(icon5)
        self.Next_button_island_13.setIconSize(QSize(1000, 1000))
        self.Next_button_island_13.setCheckable(True)
        self.Next_button_island_13.setAutoRepeat(False)
        self.Next_button_island_13.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Next_button_island_13.setAutoRaise(False)
        self.Jawaban_1 = QToolButton(self.PGFR)
        self.Jawaban_1.setObjectName(u"Jawaban_1")
        self.Jawaban_1.setGeometry(QRect(20, 390, 211, 81))
        self.Jawaban_1.setMaximumSize(QSize(1000, 1000))
        self.Jawaban_1.setFont(font)
        self.Jawaban_1.setContextMenuPolicy(Qt.NoContextMenu)
        self.Jawaban_1.setAutoFillBackground(False)
        self.Jawaban_1.setStyleSheet(u"QToolButton {\n"
"    border: none;                  /* Menghilangkan border */\n"
"    background: transparent;       /* Membuat background transparan */\n"
"    padding: 0;                    /* Menghilangkan padding */\n"
"}\n"
"")
        self.Jawaban_1.setIcon(icon1)
        self.Jawaban_1.setIconSize(QSize(1000, 1000))
        self.Jawaban_1.setCheckable(False)
        self.Jawaban_1.setAutoRepeat(False)
        self.Jawaban_1.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Jawaban_1.setAutoRaise(False)
        self.Jawaban_1.setVisible(False)
        self.Jawaban_2 = QToolButton(self.PGFR)
        self.Jawaban_2.setObjectName(u"Jawaban_2")
        self.Jawaban_2.setGeometry(QRect(260, 390, 141, 91))
        self.Jawaban_2.setMaximumSize(QSize(1000, 1000))
        self.Jawaban_2.setFont(font)
        self.Jawaban_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.Jawaban_2.setAutoFillBackground(False)
        self.Jawaban_2.setStyleSheet(u"QToolButton {\n"
"    border: none;                  /* Menghilangkan border */\n"
"    background: transparent;       /* Membuat background transparan */\n"
"    padding: 0;                    /* Menghilangkan padding */\n"
"}\n"
"")
        self.Jawaban_2.setIcon(icon2)
        self.Jawaban_2.setIconSize(QSize(1000, 1000))
        self.Jawaban_2.setCheckable(False)
        self.Jawaban_2.setAutoRepeat(False)
        self.Jawaban_2.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Jawaban_2.setAutoRaise(False)
        self.Jawaban_2.setVisible(False)
        self.Jawaban_5 = QToolButton(self.PGFR)
        self.Jawaban_5.setObjectName(u"Jawaban_5")
        self.Jawaban_5.setGeometry(QRect(780, 390, 201, 81))
        self.Jawaban_5.setMaximumSize(QSize(1000, 1000))
        self.Jawaban_5.setFont(font)
        self.Jawaban_5.setContextMenuPolicy(Qt.NoContextMenu)
        self.Jawaban_5.setAutoFillBackground(False)
        self.Jawaban_5.setStyleSheet(u"QToolButton {\n"
"    border: none;                  /* Menghilangkan border */\n"
"    background: transparent;       /* Membuat background transparan */\n"
"    padding: 0;                    /* Menghilangkan padding */\n"
"}\n"
"")
        self.Jawaban_5.setIcon(icon4)
        self.Jawaban_5.setIconSize(QSize(1000, 1000))
        self.Jawaban_5.setCheckable(False)
        self.Jawaban_5.setAutoRepeat(False)
        self.Jawaban_5.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Jawaban_5.setAutoRaise(False)
        self.Jawaban_5.setVisible(False)
        self.Jawaban_3 = QToolButton(self.PGFR)
        self.Jawaban_3.setObjectName(u"Jawaban_3")
        self.Jawaban_3.setGeometry(QRect(370, 390, 271, 81))
        self.Jawaban_3.setMaximumSize(QSize(1000, 1000))
        self.Jawaban_3.setFont(font)
        self.Jawaban_3.setContextMenuPolicy(Qt.NoContextMenu)
        self.Jawaban_3.setAutoFillBackground(False)
        self.Jawaban_3.setStyleSheet(u"QToolButton {\n"
"    border: none;                  /* Menghilangkan border */\n"
"    background: transparent;       /* Membuat background transparan */\n"
"    padding: 0;                    /* Menghilangkan padding */\n"
"}\n"
"")
        self.Jawaban_3.setIcon(icon5)
        self.Jawaban_3.setIconSize(QSize(1000, 1000))
        self.Jawaban_3.setCheckable(False)
        self.Jawaban_3.setAutoRepeat(False)
        self.Jawaban_3.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Jawaban_3.setAutoRaise(False)
        self.Jawaban_3.setVisible(False)
        self.Jawaban_4 = QToolButton(self.PGFR)
        self.Jawaban_4.setObjectName(u"Jawaban_4")
        self.Jawaban_4.setGeometry(QRect(600, 390, 191, 81))
        self.Jawaban_4.setMaximumSize(QSize(1000, 1000))
        self.Jawaban_4.setFont(font)
        self.Jawaban_4.setContextMenuPolicy(Qt.NoContextMenu)
        self.Jawaban_4.setAutoFillBackground(False)
        self.Jawaban_4.setStyleSheet(u"QToolButton {\n"
"    border: none;                  /* Menghilangkan border */\n"
"    background: transparent;       /* Membuat background transparan */\n"
"    padding: 0;                    /* Menghilangkan padding */\n"
"}\n"
"")
        self.Jawaban_4.setIcon(icon3)
        self.Jawaban_4.setIconSize(QSize(1000, 1000))
        self.Jawaban_4.setCheckable(False)
        self.Jawaban_4.setAutoRepeat(False)
        self.Jawaban_4.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Jawaban_4.setAutoRaise(False)
        self.Jawaban_4.setVisible(False)

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
        self.Progres = QWidget(self.frame_3)
        self.Progres.setObjectName(u"Progres")
        self.Progres.setGeometry(QRect(10, 90, 381, 361))
        self.Progres.setStyleSheet(u"QWidget#Progres{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(204, 204, 204) ;\n"
"    border-radius: 20px;\n"
"}")
        self.label_14 = QLabel(self.Progres)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 20, 321, 31))
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"QLabel{\n"
"color: #585858;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.label_15 = QLabel(self.Progres)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(300, 82, 61, 41))
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"QLabel{\n"
"color: #585858;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.label_16 = QLabel(self.Progres)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 150, 321, 31))
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"QLabel{\n"
"color: #585858;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.PBar = QLabel(self.Progres)
        self.PBar.setObjectName(u"PBar")
        self.PBar.setGeometry(QRect(20, 90, 260, 25))
        self.PBar.setMinimumSize(QSize(260, 0))
        self.PBar.setMaximumSize(QSize(100, 999999))
        self.PBar.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.PBar.setPixmap(QPixmap(u"Assets/PG/ProgressBar.png"))
        self.PBar.setScaledContents(True)
        self.label_17 = QLabel(self.Progres)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(170, 180, 161, 101))
        font3 = QFont()
        font3.setFamilies([u"Jellee Roman"])
        font3.setPointSize(12)
        self.label_17.setFont(font3)
        self.label_17.setStyleSheet(u"QLabel{\n"
"color: #585858;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.Jepang_2 = QLabel(self.Progres)
        self.Jepang_2.setObjectName(u"Jepang_2")
        self.Jepang_2.setGeometry(QRect(20, 190, 128, 137))
        self.Jepang_2.setMinimumSize(QSize(128, 137))
        self.Jepang_2.setMaximumSize(QSize(128, 137))
        self.Jepang_2.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.Jepang_2.setPixmap(QPixmap(u"Assets/PG/monkey.png"))
        self.Jepang_2.setScaledContents(True)
        self.Next_button_island_7 = QToolButton(self.Progres)
        self.Next_button_island_7.setObjectName(u"Next_button_island_7")
        self.Next_button_island_7.setGeometry(QRect(140, 290, 191, 31))
        self.Next_button_island_7.setMaximumSize(QSize(1000, 1000))
        self.Next_button_island_7.setFont(font)
        self.Next_button_island_7.setContextMenuPolicy(Qt.NoContextMenu)
        self.Next_button_island_7.setAutoFillBackground(False)
        self.Next_button_island_7.setStyleSheet(u"QToolButton {\n"
"    border: none;                  /* Menghilangkan border */\n"
"    background: transparent;       /* Membuat background transparan */\n"
"    padding: 0;                    /* Menghilangkan padding */\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"Assets/PG/btn_atur.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u"Assets/PG/btn_atur_pres.png", QSize(), QIcon.Selected, QIcon.On)
        self.Next_button_island_7.setIcon(icon6)
        self.Next_button_island_7.setIconSize(QSize(1000, 1000))
        self.Next_button_island_7.setCheckable(False)
        self.Next_button_island_7.setAutoRepeat(False)
        self.Next_button_island_7.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Next_button_island_7.setAutoRaise(False)
        self.layoutWidget = QWidget(self.frame_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 20, 321, 44))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setSpacing(9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Jepang = QLabel(self.layoutWidget)
        self.Jepang.setObjectName(u"Jepang")
        self.Jepang.setMaximumSize(QSize(100, 100))
        self.Jepang.setPixmap(QPixmap(u"Assets/Dashboard/Right_bar/bendera_jepang.png"))
        self.Jepang.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.Jepang)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.api = QLabel(self.layoutWidget)
        self.api.setObjectName(u"api")
        self.api.setPixmap(QPixmap(u"Assets/Dashboard/Right_bar/Streak.png"))
        self.api.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.api)

        self.angka = QLabel(self.layoutWidget)
        self.angka.setObjectName(u"angka")
        font4 = QFont()
        font4.setFamilies([u"Jellee Roman"])
        font4.setPointSize(18)
        self.angka.setFont(font4)
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
        self.segitiga.setPixmap(QPixmap(u"Assets/Dashboard/Right_bar/Points.png"))
        self.segitiga.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.segitiga)

        self.angka_2 = QLabel(self.layoutWidget)
        self.angka_2.setObjectName(u"angka_2")
        self.angka_2.setFont(font4)
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
        self.Star.setPixmap(QPixmap(u"Assets/Dashboard/Right_bar/Star.png"))
        self.Star.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.Star)

        self.Stars_count = QLabel(self.layoutWidget)
        self.Stars_count.setObjectName(u"Stars_count")
        font5 = QFont()
        font5.setFamilies([u"Jellee Roman"])
        font5.setPointSize(20)
        self.Stars_count.setFont(font5)
        self.Stars_count.setStyleSheet(u"QLabel#Stars_count{\n"
"color : rgb(85, 153, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.Stars_count)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)


        self.horizontalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Next_button_island_9.toggled.connect(self.Jawaban_1.setVisible)
        self.Next_button_island_9.toggled.connect(self.Next_button_island_9.setHidden)
        self.Next_button_island_10.toggled.connect(self.Jawaban_2.setVisible)
        self.Next_button_island_10.toggled.connect(self.Next_button_island_10.setHidden)
        self.Next_button_island_13.toggled.connect(self.Jawaban_3.setVisible)
        self.Next_button_island_13.toggled.connect(self.Next_button_island_13.setHidden)
        self.Next_button_island_11.toggled.connect(self.Jawaban_4.setVisible)
        self.Next_button_island_11.toggled.connect(self.Next_button_island_11.setHidden)
        self.Next_button_island_12.toggled.connect(self.Jawaban_5.setVisible)
        self.Next_button_island_12.toggled.connect(self.Next_button_island_12.setHidden)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Next_button_island_6.setText("")
        self.logo.setText(QCoreApplication.translate("MainWindow", u"duahasa", None))
        self.belajar.setText("")
        self.flashcard.setText("")
        self.pilihan_ganda.setText("")
        self.Land_2.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Ubah ke Bahasa Jepang!", None))
        self.Jepang_4.setText("")
        self.Jepang_5.setText("")
        self.Jepang_6.setText("")
        self.Jepang_7.setText("")
        self.Jepang_8.setText("")
        self.Jepang_9.setText("")
        self.Jepang_10.setText("")
        self.Jepang_11.setText("")
        self.Jepang_12.setText("")
        self.Next_button_island_9.setText("")
        self.Next_button_island_10.setText("")
        self.Next_button_island_11.setText("")
        self.Next_button_island_12.setText("")
        self.Next_button_island_13.setText("")
        self.Jawaban_1.setText("")
        self.Jawaban_2.setText("")
        self.Jawaban_5.setText("")
        self.Jawaban_3.setText("")
        self.Jawaban_4.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Progress Pilihan Ganda Kamu!", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"6/10", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Atur Pilihan Ganda Kamu!", None))
        self.PBar.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Kamu bisa\n"
"menambahkan hal\n"
"yang ingin kamu\n"
"pelajari di sini", None))
        self.Jepang_2.setText("")
        self.Next_button_island_7.setText("")
        self.Jepang.setText("")
        self.api.setText("")
        self.angka.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.segitiga.setText("")
        self.angka_2.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.Star.setText("")
        self.Stars_count.setText(QCoreApplication.translate("MainWindow", u"5", None))
    # retranslateUi

