# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FlashcardqkckYN.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup, QSequentialAnimationGroup)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter, QResizeEvent, QFontMetrics,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QToolButton, QWidget, QStyledItemDelegate, QVBoxLayout, QGraphicsOpacityEffect)

import sys

class EllipsisDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        option.displayAlignment = Qt.AlignLeft | Qt.AlignVCenter
        option.textElideMode = Qt.ElideRight
        super().paint(painter, option, index)

class AutoResizeLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.default_font_size = 36  # Ukuran font default
        self.minimum_font_size = 12  # Ukuran font minimum
        self.setWordWrap(True)
        self.setScaledContents(False)
        self.setStyleSheet("QLabel { background-color: transparent; color: white; }")
        self.updateFontSize()  # Set ukuran font saat inisialisasi

    def resizeEvent(self, event: QResizeEvent):
        super().resizeEvent(event)
        self.updateFontSize()

    def setText(self, text):
        super().setText(text)
        self.updateFontSize()

    def updateFontSize(self):
        font = self.font()
        text = self.text()
        current_font_size = self.default_font_size
        font.setPointSize(current_font_size)
        self.setFont(font)
        
        # Buat QFontMetrics dengan font saat ini
        metrics = QFontMetrics(font)
        
        # Periksa apakah teks muat di dalam label
        rect = metrics.boundingRect(0, 0, self.width(), self.height(), Qt.TextWordWrap, text)
        
        while (rect.height() > self.height() or rect.width() > self.width()) and current_font_size > self.minimum_font_size:
            current_font_size -= 1
            font.setPointSize(current_font_size)
            self.setFont(font)
            metrics = QFontMetrics(font)
            rect = metrics.boundingRect(0, 0, self.width(), self.height(), Qt.TextWordWrap, text)

        self.setFont(font)

class Flashcard(object):
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
        icon.addFile(u"Assets/Flashcards/Leftbar/Keluar.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.flashcard_active.setPixmap(QPixmap(u"Assets/Flashcards/Leftbar/Flashcards Active.png"))
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
        self.belajar.setPixmap(QPixmap(u"Assets/Flashcards/Leftbar/Learning.png"))
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
        self.pilihan_ganda.setPixmap(QPixmap(u"Assets/Flashcards/Leftbar/Multiple Choice.png"))

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

###############################################################################
######################## FLASHCARD POP UP SYSTEM ##############################
###############################################################################

        self.flashcardBgPopUp = QLabel(self.frame_2)
        self.flashcardBgPopUp.setObjectName(u"flashcardBgPopUp")
        self.flashcardBgPopUp.setGeometry(QRect(-20, -10, 1121, 1081))
        self.flashcardBgPopUp.setStyleSheet(u"QLabel {\n"
"    background-color: rgba(0, 0, 0, 0.5);\n"
"}")
        self.flashcardBgPopUp.setVisible(False)

        self.flashcardPopUp = QLabel(self.frame_2)
        self.flashcardPopUp.setObjectName(u"flashcardPopUp")
        self.flashcardPopUp.setGeometry(QRect(40, 130, 1011, 791))
        self.flashcardPopUp.setStyleSheet(u"QLabel {\n"
"    background-color: white;\n"
"    border-radius: 20px;\n"
"}")
        self.flashcardPopUp.setVisible(False)

        self.btnKembaliPopUp = QLabel(self.frame_2)
        self.btnKembaliPopUp.setObjectName(u"btnKembaliPopUp")
        self.btnKembaliPopUp.setGeometry(QRect(80, 160, 261, 51))
        self.btnKembaliPopUp.setPixmap(QPixmap(u"Assets\Flashcards\Middlebar\PopUp Kembali.png"))
        self.btnKembaliPopUp.setScaledContents(False)
        self.btnKembaliPopUp.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"}")
        self.btnKembaliPopUp.setCursor(QCursor(Qt.PointingHandCursor))

        self.btnKembaliPopUp.setVisible(False)

        self.labelFlashcardBaruPopUp = QLabel(self.frame_2)
        self.labelFlashcardBaruPopUp.setObjectName(u"labelFlashcardBaruPopUp")
        self.labelFlashcardBaruPopUp.setGeometry(QRect(680, 165, 350, 41))
        self.labelFlashcardBaruPopUp.setPixmap(QPixmap(u"Assets\Flashcards\Middlebar\FlashCard Baru.png"))
        self.labelFlashcardBaruPopUp.setScaledContents(False)
        self.labelFlashcardBaruPopUp.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"}")
        self.labelFlashcardBaruPopUp.setVisible(False)

        self.lineFlashcardPopUp = QLabel(self.frame_2)
        self.lineFlashcardPopUp.setObjectName(u"lineFlashcardPopUp")
        self.lineFlashcardPopUp.setGeometry(QRect(80, 250, 980, 41))
        self.lineFlashcardPopUp.setPixmap(QPixmap(u"Assets\Flashcards\Middlebar\PopUp Line.png"))
        self.lineFlashcardPopUp.setScaledContents(False)
        self.lineFlashcardPopUp.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"}")
        self.lineFlashcardPopUp.setVisible(False)

###############################################################################
############################ FLASHCARD SYSTEM #################################
###############################################################################

        self.Flashcard = QWidget(self.frame_2)
        self.Flashcard.setObjectName(u"Flashcard")
        self.Flashcard.setGeometry(QRect(160, 80, 731, 901))
        self.Flashcard.setStyleSheet(u"QLabel {\n"
"	border: 0px;\n"
"	color: #585858;\n"
"}")
        self.pertanyaan = AutoResizeLabel(self.Flashcard)
        self.pertanyaan.setObjectName(u"pertanyaan")
        self.pertanyaan.setGeometry(QRect(180, 90, 411, 111))
        self.pertanyaan.setMaximumSize(QSize(500, 200))

        font2 = QFont()
        font2.setFamilies([u"Jellee"])
        font2.setPointSize(36)
        self.pertanyaan.setFont(font2)
        self.pertanyaan.setCursor(QCursor(Qt.PointingHandCursor))

        self.background = QToolButton(self.Flashcard)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(89, 50, 581, 801))
        self.background.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"Assets/Flashcards/Middlebar/Background Flashcard 2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.background.setIcon(icon2)
        self.background.setIconSize(QSize(1000, 1000))
        self.background.setCursor(QCursor(Qt.PointingHandCursor))
        self.background.setStyleSheet(u"QToolButton#background {\n"
"	background: transparent;\n"
"}")
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
        self.image.setPixmap(QPixmap(u"Assets/Flashcards/Middlebar/image v2.png"))
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
        self.pertanyaan_2.setPixmap(QPixmap(u"Assets/Flashcards/Middlebar/Dekorasi.png"))
        self.pertanyaan_2.setScaledContents(True)
        self.pertanyaan_2.setWordWrap(True)
        self.pertanyaan_2.raise_()
        self.background.raise_()
        self.pertanyaan.raise_()
        self.flashcardBgPopUp.raise_()
        self.flashcardPopUp.raise_()
        self.btnKembaliPopUp.raise_()
        self.labelFlashcardBaruPopUp.raise_()
        self.lineFlashcardPopUp.raise_()
        self.image.raise_()
        self.jawaban.raise_()

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
        font4 = QFont()
        font4.setFamilies([u"Jellee Roman"])
        font4.setPointSize(18)
        self.header.setFont(font4)
        self.header.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.counter = QLabel(self.Progress)
        self.counter.setObjectName(u"counter")
        self.counter.setGeometry(QRect(290, 80, 61, 41))
        font5 = QFont()
        font5.setFamilies([u"Jellee Roman"])
        font5.setPointSize(20)
        self.counter.setFont(font5)
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
        self.header_2.setFont(font4)
        self.header_2.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.aturButton = QToolButton(self.Atur)
        self.aturButton.setObjectName(u"toolButton")
        self.aturButton.setGeometry(QRect(10, 70, 361, 71))
        self.aturButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.aturButton.setStyleSheet(u"QToolButton {\n"
"	background: transparent;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"Assets/Flashcards/Rightbar/Atur Button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.aturButton.setIcon(icon1)
        self.aturButton.setIconSize(QSize(1000, 1000))
        self.aturButton.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.Jepang.setPixmap(QPixmap(u"Assets/Flashcards/Rightbar/Logo Jepang.png"))
        self.Jepang.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.Jepang)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.api = QLabel(self.layoutWidget)
        self.api.setObjectName(u"api")
        self.api.setPixmap(QPixmap(u"Assets/Flashcards/Rightbar/Streak.png"))
        self.api.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.api)

        self.angka = QLabel(self.layoutWidget)
        self.angka.setObjectName(u"angka")
        font6 = QFont()
        font6.setFamilies([u"Jellee"])
        font6.setPointSize(18)
        self.angka.setFont(font6)
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
        self.segitiga.setPixmap(QPixmap(u"Assets/Flashcards/Rightbar/Points.png"))
        self.segitiga.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.segitiga)

        self.angka_2 = QLabel(self.layoutWidget)
        self.angka_2.setObjectName(u"angka_2")
        self.angka_2.setFont(font6)
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
        self.Star.setPixmap(QPixmap(u"Assets/Flashcards/Rightbar/Stars.png"))
        self.Star.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.Star)

        self.Stars_count = QLabel(self.layoutWidget)
        self.Stars_count.setObjectName(u"Stars_count")
        self.Stars_count.setFont(font5)
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
        self.header_3.setFont(font4)
        self.header_3.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.comboBox = QComboBox(self.Urutan)
        self.comboBox.addItem("Kartu 1 - Apa yang sedang dia lakukan?")
        self.comboBox.addItem("Kartu 2 - Mengapa dia melakukan itu?")
        self.comboBox.addItem("Kartu 3 - Bagaimana cara dia melakukannya?")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(15, 60, 341, 61))
        self.comboBox.setFont(font3)
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    color: #313131;\n"
"    background-color: white;\n"
"    border: 5px solid #CCCCCC;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    padding-right: 10px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(\"Assets/Flashcards/Rightbar/Icon Dropdown.png\");\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"QComboBox::down-arrow:on {\n"
"    image: url(\"Assets/Flashcards/Rightbar/Icon Dropdown 2.png\");\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    color: #585858;\n"
"    selection-background-color: blue;\n"
"    font-size: 2px;\n"
"    padding: 10px;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: lightblue;\n"
"    color: #313131;\n"
"    border: 0;\n"
"    font-size: 12px; /* Mengubah ukuran font saat dihover juga */\n"
"}\n")

        # Mengatur delegate untuk menampilkan elipsis pada teks yang panjang
        delegate = EllipsisDelegate(self.comboBox)
        self.comboBox.setItemDelegate(delegate)

        # Hubungkan sinyal currentIndexChanged dari comboBox ke metode updatePertanyaan
        self.comboBox.currentIndexChanged.connect(lambda: self.updatePertanyaan("combobox"))

        # Variabel untuk melacak status perubahan teks
        self.text_changed = False
        self.popup_changed = False

        # Membuat frame_4 dan menambahkannya ke layout
        self.frame_4 = QFrame(self.Flashcard)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(self.image.geometry().x(), self.image.geometry().y() + 200, self.image.geometry().width(), 200))  # Setel geometry
        self.frame_4.setStyleSheet(u"QFrame {\n"
"    background: transparent;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"    border: 0px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.hide()

        # Buat layout untuk frame_4
        self.frame_4_layout = QVBoxLayout(self.frame_4)
        self.frame_4_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_4_layout.setSpacing(0)

        # QLabel baru untuk menggantikan self.image saat ditekan
        self.jawaban_jepang = QLabel(self.frame_4)
        self.jawaban_jepang.setObjectName("jawaban_jepang")
        self.jawaban_jepang.setStyleSheet("background-color: transparent; color: white;")
        self.jawaban_jepang.setFont(QFont("Jellee", 30))
        self.jawaban_jepang.setAlignment(Qt.AlignCenter)
        self.jawaban_jepang.setText("彼は食べている")
        self.jawaban_jepang.setCursor(QCursor(Qt.PointingHandCursor))

        self.jawaban_latin = QLabel(self.frame_4)
        self.jawaban_latin.setObjectName("jawaban_latin")
        self.jawaban_latin.setStyleSheet("background-color: transparent; color: white;")
        self.jawaban_latin.setFont(QFont("Jellee", 30))
        self.jawaban_latin.setAlignment(Qt.AlignCenter)
        self.jawaban_latin.setText("Kare wa tabete iru")
        self.jawaban_latin.setCursor(QCursor(Qt.PointingHandCursor))

        # Tambahkan label ke layout
        self.frame_4_layout.addWidget(self.jawaban_jepang, alignment=Qt.AlignCenter)
        self.frame_4_layout.addWidget(self.jawaban_latin, alignment=Qt.AlignCenter)

        # Sembunyikan label saat inisialisasi
        self.jawaban_jepang.hide()
        self.jawaban_latin.hide()

        # Setup opacity effect for frame_4
        self.opacity_effect = QGraphicsOpacityEffect()
        self.frame_4.setGraphicsEffect(self.opacity_effect)
        self.opacity_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.opacity_animation.setDuration(500)
        self.opacity_animation.setEasingCurve(QEasingCurve.InOutQuad)

        # Menghubungkan saat flashcard di klik
        self.background.mousePressEvent = lambda event: self.updatePertanyaan("flashcard")
        self.pertanyaan.mousePressEvent = lambda event: self.updatePertanyaan("flashcard")
        self.image.mousePressEvent = lambda event: self.updatePertanyaan("flashcard")
        self.jawaban_jepang.mousePressEvent = lambda event: self.updatePertanyaan("flashcard")
        self.jawaban_latin.mousePressEvent = lambda event: self.updatePertanyaan("flashcard")
        self.aturButton.mousePressEvent = lambda event: self.popUp()

        self.header_3.raise_()

        self.horizontalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def updatePertanyaan(self, status):
        # Update dari comboBox
        selected_text = self.comboBox.currentText()
        result_text = selected_text.split(" - ", 1)[1]

        # Update dari flashcard
        if status == "flashcard" and not self.text_changed:
            result_text = "Jawaban"
            self.text_changed = True
            self.image.hide()
            self.frame_4.show()
            self.jawaban_jepang.show()
            self.jawaban_latin.show()
            # Start opacity animation
            self.opacity_animation.setStartValue(0)
            self.opacity_animation.setEndValue(1)
            self.opacity_animation.start()
        else:
            self.text_changed = False
            self.image.show()
            self.frame_4.hide()
            self.jawaban_jepang.hide()
            self.jawaban_latin.hide()
        self.pertanyaan.setText(result_text)

    def popUp(self):
        if self.popup_changed:
            self.flashcardPopUp.setVisible(False)
            self.flashcardBgPopUp.setVisible(False)
            self.btnKembaliPopUp.setVisible(False)
            self.labelFlashcardBaruPopUp.setVisible(False)
            self.lineFlashcardPopUp.setVisible(False)
            self.popup_changed = False
        else:
            self.flashcardPopUp.setVisible(True)
            self.flashcardBgPopUp.setVisible(True)
            self.btnKembaliPopUp.setVisible(True)
            self.labelFlashcardBaruPopUp.setVisible(True)
            self.lineFlashcardPopUp.setVisible(True)
            self.popup_changed = True

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
        self.header.setText(QCoreApplication.translate("MainWindow", u"Progress Flashcard Kamu", None))
        self.counter.setText(QCoreApplication.translate("MainWindow", u"3/10", None))
        self.header_2.setText(QCoreApplication.translate("MainWindow", u"Atur Flashcard Kamu", None))
        self.aturButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Jepang.setText("")
        self.api.setText("")
        self.angka.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.segitiga.setText("")
        self.angka_2.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.Star.setText("")
        self.Stars_count.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.header_3.setText(QCoreApplication.translate("MainWindow", u"Urutan Kartu", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Kartu 1 - Apa yang sedang dia lakukan?", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Kartu 2 - Kenapa kamu melakukan hal tersebut?", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Kartu 3 - Bagaimana cara dia melakukannya?", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Flashcard()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())