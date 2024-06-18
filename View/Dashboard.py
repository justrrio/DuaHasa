from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,QPainterPath,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)

import sys

class CustomToolButton(QToolButton):
    def __init__(self, parent=None, normal=None, hover=None, pressed=None):
        super().__init__(parent)
        self.setObjectName("Next_button_island_6")
        self.setGeometry(30, 950, 321, 71)
        self.setMaximumSize(1000, 1000)
        font = QFont()
        font.setKerning(True)
        self.setFont(font)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setAutoFillBackground(False)
        self.setStyleSheet("QToolButton {\n"
                           "    border: none;                  /* Menghilangkan border */\n"
                           "    background: transparent;       /* Membuat background transparan */\n"
                           "    padding: 0;                    /* Menghilangkan padding */\n"
                           "}\n")
        self.icon_normal = QIcon(normal)
        self.icon_hover = QIcon(hover)
        self.icon_pressed = QIcon(pressed)
        self.setIcon(self.icon_normal)
        self.setIconSize(QSize(1000, 1000))
        self.setCheckable(False)
        self.setAutoRepeat(False)
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.setAutoRaise(False)

    def enterEvent(self, event):
        self.setIcon(self.icon_hover)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setIcon(self.icon_normal)
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setIcon(self.icon_pressed)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setIcon(self.icon_hover)  # Mengembalikan ke ikon hover setelah klik
            # Jalankan fungsi tambahan di sini jika diperlukan
        super().mouseReleaseEvent(event)

class ShadowWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Sesi")
        self.setGeometry(QRect(90, 30, 921, 121))
        self.setMaximumSize(QSize(1920, 1080))
        self.setAcceptDrops(False)
        self.setStyleSheet("""
            QWidget {
                background-color: #E36B37;
                border: 1px solid #E36B37;
                border-radius: 20px;
            }
        """)

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = self.rect()
        
        # Menggambar bayangan
        shadow_path = QPainterPath()
        shadow_path.addRoundedRect(rect.adjusted(5, 5, -5, -5), 20, 20)
        painter.fillPath(shadow_path, QColor(0, 0, 0, 50))
        
        # Menggambar konten asli
        content_path = QPainterPath()
        content_path.addRoundedRect(rect.adjusted(0, 0, -10, -10), 20, 20)
        painter.fillPath(content_path, self.palette().window().color())

class dashboard(object):
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
"")
        # Di dalam metode setupUi
        self.Next_button_island_6 = CustomToolButton(self.frame, "Assets/Dashboard/Left_bar/KELUAR.png",
                                                     "Assets/Dashboard/Left_bar/KELUAR_Hover.png",
                                                     "Assets/Dashboard/Left_bar/KELUAR PRESSED.png")
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
        self.flashcard.setPixmap(QPixmap(u"Assets/Dashboard/Left_bar/Flashcards.png"))
        self.flashcard.setScaledContents(False)
        self.drawing_board = QLabel(self.frame)
        self.drawing_board.setObjectName(u"drawing_board")
        self.drawing_board.setGeometry(QRect(40, 290, 291, 60))
        self.drawing_board.setMaximumSize(QSize(291, 60))
        self.drawing_board.setStyleSheet(u"QLabel {\n"
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
        self.drawing_board.setPixmap(QPixmap(u"Assets/Dashboard/Left_bar/MULTIPLE_CHOICE.png"))

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
         # Inisialisasi ShadowWidget
        self.Sesi = ShadowWidget(self.frame_2)
        self.Sesi.setObjectName(u"Sesi")
        self.Sesi.setGeometry(QRect(90, 30, 921, 121))
        self.Sesi.setMaximumSize(QSize(1920, 1080))
        self.Sesi.setAcceptDrops(False)
        self.Sesi.setStyleSheet(u"QWidget {\n"
        "    background-color: #E36B37;\n"
        "    border: 1px solid #E36B37;  \n"
        "    border-radius: 20px;\n"
        "}")


        self.Panduan_btn = QLabel(self.Sesi)
        self.Panduan_btn.setObjectName(u"Panduan_btn")
        self.Panduan_btn.setGeometry(QRect(710, 20, 161, 71))
        self.Panduan_btn.setPixmap(QPixmap(u"Assets/Dashboard/Sesi/Panduan.png"))
        self.layoutWidget = QWidget(self.Sesi)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 20, 581, 72))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Back_Button = QLabel(self.layoutWidget)
        self.Back_Button.setObjectName(u"Back_Button")
        self.Back_Button.setMaximumSize(QSize(30, 16777215))
        self.Back_Button.setPixmap(QPixmap(u"Assets/Dashboard/Sesi/Backspace.png"))

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

        self.Land_2 = QLabel(self.frame_2)
        self.Land_2.setObjectName(u"Land_2")
        self.Land_2.setGeometry(QRect(410, 650, 471, 321))
        self.Land_2.setPixmap(QPixmap(u"Assets/Dashboard/Island/Island_2.png"))
        self.Land_2.setScaledContents(True)
        self.Land_1 = QLabel(self.frame_2)
        self.Land_1.setObjectName(u"Land_1")
        self.Land_1.setGeometry(QRect(150, 170, 701, 461))
        self.Land_1.setPixmap(QPixmap(u"Assets/Dashboard/Island/Island_1.png"))
        self.Land_1.setScaledContents(True)
        self.Tangga = QLabel(self.frame_2)
        self.Tangga.setObjectName(u"Tangga")
        self.Tangga.setGeometry(QRect(420, 500, 141, 191))
        self.Tangga.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"}")
        self.Tangga.setPixmap(QPixmap(u"Assets/Dashboard/Island/Ladder.png"))
        self.Tangga.setScaledContents(True)
        self.Start_btn = QToolButton(self.frame_2)
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
        icon1 = QIcon()
        icon1.addFile(u"Assets/Dashboard/Island/Start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Start_btn.setIcon(icon1)
        self.Start_btn.setIconSize(QSize(500, 500))
        self.Start_btn.setCheckable(False)
        self.Start_btn.setAutoRepeat(False)
        self.Start_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Start_btn.setAutoRaise(False)
        self.Next_button_island = QToolButton(self.frame_2)
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
        icon2 = QIcon()
        icon2.addFile(u"Assets/Dashboard/Island/Next_Button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Next_button_island.setIcon(icon2)
        self.Next_button_island.setIconSize(QSize(200, 200))
        self.Next_button_island.setCheckable(False)
        self.Next_button_island.setAutoRepeat(False)
        self.Next_button_island.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Next_button_island.setAutoRaise(False)
        self.Next_button_island_2 = QToolButton(self.frame_2)
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
        self.Next_button_island_2.setIcon(icon2)
        self.Next_button_island_2.setIconSize(QSize(200, 200))
        self.Next_button_island_2.setCheckable(False)
        self.Next_button_island_2.setAutoRepeat(False)
        self.Next_button_island_2.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Next_button_island_2.setAutoRaise(False)
        self.Next_button_island_3 = QToolButton(self.frame_2)
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
        icon3 = QIcon()
        icon3.addFile(u"Assets/Dashboard/Island/Chest.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Next_button_island_3.setIcon(icon3)
        self.Next_button_island_3.setIconSize(QSize(200, 200))
        self.Next_button_island_3.setCheckable(False)
        self.Next_button_island_3.setAutoRepeat(False)
        self.Next_button_island_3.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Next_button_island_3.setAutoRaise(False)
        self.Next_button_island_4 = QToolButton(self.frame_2)
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
        self.Next_button_island_4.setIcon(icon2)
        self.Next_button_island_4.setIconSize(QSize(200, 200))
        self.Next_button_island_4.setCheckable(False)
        self.Next_button_island_4.setAutoRepeat(False)
        self.Next_button_island_4.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Next_button_island_4.setAutoRaise(False)
        self.Next_button_island_5 = QToolButton(self.frame_2)
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
        icon4 = QIcon()
        icon4.addFile(u"Assets/Dashboard/Island/Finish_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Next_button_island_5.setIcon(icon4)
        self.Next_button_island_5.setIconSize(QSize(200, 200))
        self.Next_button_island_5.setCheckable(False)
        self.Next_button_island_5.setAutoRepeat(False)
        self.Next_button_island_5.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Next_button_island_5.setAutoRaise(False)
        self.Maskot_monyet_island = QLabel(self.frame_2)
        self.Maskot_monyet_island.setObjectName(u"Maskot_monyet_island")
        self.Maskot_monyet_island.setGeometry(QRect(270, 200, 231, 211))
        self.Maskot_monyet_island.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;  /* Membuat background transparan */\n"
"    border: none;                   /* Menghilangkan border */\n"
"}\n"
"")
        self.Maskot_monyet_island.setPixmap(QPixmap(u"Assets/Dashboard/Island/maskot_island.png"))
        self.Maskot_monyet_island.setScaledContents(True)
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
"color: rgb(0, 0, 0);\n"  # Mengatur warna teks menjadi hitam
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
"color: rgb(0, 0, 0);\n"
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
"color: rgb(0, 0, 0);\n"
"}")
        self.label_17 = QLabel(self.Progres)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(30, 180, 321, 51))
        self.label_17.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;  /* Membuat background transparan */\n"
"}\n"
"")
        self.label_17.setPixmap(QPixmap(u"Assets/Dashboard/Right_bar/Button_Belajar.png"))
        self.progressBar.raise_()
        self.label_17.raise_()
        self.Progress_belajar.raise_()
        self.motivasi.raise_()
        self.Count_materi.raise_()
        self.Iklan = QWidget(self.frame_3)
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
        self.karakter.setPixmap(QPixmap(u"Assets/Dashboard/Right_bar/Card2.png"))
        self.karakter.setScaledContents(True)
        self.Profile = QWidget(self.frame_3)
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
"color: rgb(0, 0, 0);\n"
"}")
        self.b_profile = QLabel(self.Profile)
        self.b_profile.setObjectName(u"b_profile")
        self.b_profile.setGeometry(QRect(40, 70, 311, 51))
        self.b_profile.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;  /* Membuat background transparan */\n"
"}\n"
"")
        self.b_profile.setPixmap(QPixmap(u"Assets/Dashboard/Right_bar/Profile.png"))
        self.b_profile.setScaledContents(True)
        self.layoutWidget1 = QWidget(self.frame_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 20, 321, 44))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setSpacing(9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Jepang = QLabel(self.layoutWidget1)
        self.Jepang.setObjectName(u"Jepang")
        self.Jepang.setMaximumSize(QSize(100, 16777215))
        self.Jepang.setPixmap(QPixmap(u"Assets/Dashboard/Right_bar/bendera_jepang.png"))
        self.Jepang.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.Jepang)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.api = QLabel(self.layoutWidget1)
        self.api.setObjectName(u"api")
        self.api.setPixmap(QPixmap(u"Assets/Dashboard/Right_bar/Streak.png"))
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
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.segitiga = QLabel(self.layoutWidget1)
        self.segitiga.setObjectName(u"segitiga")
        self.segitiga.setMinimumSize(QSize(40, 0))
        self.segitiga.setMaximumSize(QSize(40, 16777215))
        self.segitiga.setPixmap(QPixmap(u"Assets/Dashboard/Right_bar/Points.png"))
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
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Star = QLabel(self.layoutWidget1)
        self.Star.setObjectName(u"Star")
        self.Star.setMaximumSize(QSize(200, 100))
        self.Star.setPixmap(QPixmap(u"Assets/Dashboard/Right_bar/Star.png"))
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


        self.horizontalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DuaHasa", None))
        self.Next_button_island_6.setText("")
        self.logo.setText(QCoreApplication.translate("MainWindow", u"duahasa", None))
        self.belajar.setText("")
        self.flashcard.setText("")
        self.drawing_board.setText("")
        self.Panduan_btn.setText("")
        self.Back_Button.setText("")
        self.Text_sesi.setText(QCoreApplication.translate("MainWindow", u"TEXT SESI", None))
        self.Text_Pembelajaran.setText(QCoreApplication.translate("MainWindow", u"Menggunakan Frasa Dasar", None))
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
        self.Progress_belajar.setText(QCoreApplication.translate("MainWindow", u"Progress Belajar Kamu", None))
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
    # retranslateUi

if __name__ == "__main__":
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = dashboard()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec())