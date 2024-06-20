from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QPropertyAnimation, QRect, QEasingCurve, QSequentialAnimationGroup, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter, QPainterPath,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QMainWindow, QProgressBar, QSizePolicy, QToolButton,
                               QVBoxLayout, QWidget)
from PySide6.QtMultimedia import QSoundEffect
import os
import sys

class InteractiveLabel(QLabel):
        clicked = Signal()

        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.setMouseTracking(True)
                self.is_hovered = False
                self.original_pixmap = None

        def setPixmap(self, pixmap):
                self.original_pixmap = pixmap
                super().setPixmap(pixmap)

        def mousePressEvent(self, event):
                self.clicked.emit()

        def enterEvent(self, event):
                self.is_hovered = True
                self.setCursor(QCursor(Qt.PointingHandCursor))
                self.update()

        def leaveEvent(self, event):
                self.is_hovered = False
                self.setCursor(QCursor(Qt.ArrowCursor))
                self.update()

        def paintEvent(self, event):
                painter = QPainter(self)
                if self.is_hovered and self.original_pixmap:
                        temp_pixmap = QPixmap(self.original_pixmap.size())
                        temp_pixmap.fill(Qt.transparent)
                        temp_painter = QPainter(temp_pixmap)
                        temp_painter.setOpacity(0.7)
                        temp_painter.drawPixmap(0, 0, self.original_pixmap)
                        temp_painter.end()
                        super().setPixmap(temp_pixmap)
                else:
                        super().setPixmap(self.original_pixmap)
                super().paintEvent(event)
                painter.end()

class CustomToolButton(QToolButton):
        def __init__(self, parent=None, normal="", pressed="", hover=""):
                super().__init__(parent)
                self.icon_normal = QIcon(normal)
                self.icon_hover = QIcon(hover)
                self.icon_pressed = QIcon(pressed)
                self.setIcon(self.icon_normal)
                self.setIconSize(QSize(200, 200))
                self.setCheckable(False)
                self.setAutoRepeat(False)
                self.setToolButtonStyle(Qt.ToolButtonIconOnly)
                self.setAutoRaise(False)
                self.setStyleSheet(u"QToolButton {\n"
                                        "    border: none;                  /* Menghilangkan border */\n"
                                        "    background: transparent;       /* Membuat background transparan */\n"
                                        "    padding: 0;                    /* Menghilangkan padding */\n"
                                        "    cursor: pointer;               /* Mengubah kursor menjadi pointer */\n"
                                        "}\n"
                                        "")

        def enterEvent(self, event):
                self.setCursor(QCursor(Qt.PointingHandCursor))
                self.setIcon(self.icon_hover)
                super().enterEvent(event)

        def leaveEvent(self, event):
                self.setCursor(QCursor(Qt.ArrowCursor))
                self.setIcon(self.icon_normal)
                super().leaveEvent(event)

        def mousePressEvent(self, event):
                if event.button() == Qt.LeftButton:
                        self.setIcon(self.icon_pressed)
                super().mousePressEvent(event)

        def mouseReleaseEvent(self, event):
                if event.button() == Qt.LeftButton:
                        self.setIcon(self.icon_hover)  # Mengembalikan ke ikon hover setelah klik
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
                # Di dalam metode setupUi
                self.Keluar_button = CustomToolButton(self.Left_bar, 
                                                                "Assets/Dashboard/Left_bar/KELUAR.png",
                                                                pressed="Assets/Dashboard/Left_bar/KELUAR PRESSED.png", 
                                                                hover="Assets/Dashboard/Left_bar/KELUAR.png")
                self.Keluar_button.setObjectName(u"Keluar_button")
                self.Keluar_button.setGeometry(QRect(30, 950, 321, 71))
                self.Keluar_button.setMaximumSize(QSize(1000, 1000))
                font = QFont()
                font.setKerning(True)
                self.Keluar_button.setFont(font)
                self.Keluar_button.setContextMenuPolicy(Qt.NoContextMenu)
                self.Keluar_button.setAutoFillBackground(False)
                self.Keluar_button.setStyleSheet(u"QToolButton {\n"
                "    border: none;                  /* Menghilangkan border */\n"
                "    background: transparent;       /* Membuat background transparan */\n"
                "    padding: 0;                    /* Menghilangkan padding */\n"
                "    cursor: pointer;               /* Mengubah kursor menjadi pointer */\n"
                "}\n"
                "")
                icon = QIcon()
                icon.addFile(u"Assets/Dashboard/Left_bar/KELUAR.png", QSize(), QIcon.Normal, QIcon.Off)
                self.Keluar_button.setIcon(icon)
                self.Keluar_button.setIconSize(QSize(1000, 1000))
                self.Keluar_button.setCheckable(False)
                self.Keluar_button.setAutoRepeat(False)
                self.Keluar_button.setToolButtonStyle(Qt.ToolButtonIconOnly)
                self.Keluar_button.setAutoRaise(False)


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
                self.belajar.setPixmap(QPixmap(u"Assets/Dashboard/Left_bar/Learning_active.png"))
                self.belajar.setScaledContents(False)

                #=============================================================
                #======================= Flashcard ===========================
                #=============================================================
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
                self.flashcard.setPixmap(QPixmap(u"Assets/Dashboard/Left_bar/Flashcards.png"))
                self.flashcard.setScaledContents(False)
                self.flashcard.setCursor(QCursor(Qt.PointingHandCursor))

                #=============================================================
                #======================= Multiple Choice =====================
                #=============================================================
                # Membuat instance dari InteractiveLabel
                self.pilihan_ganda = InteractiveLabel(self.Left_bar)
                self.pilihan_ganda.setObjectName("pilihan_ganda")
                self.pilihan_ganda.setGeometry(QRect(40, 290, 291, 60))
                self.pilihan_ganda.setMaximumSize(QSize(291, 60))

                # Menghubungkan sinyal klik
                self.pilihan_ganda.clicked.connect(self.gotoPG)

                # Menambahkan gaya dengan CSS
                self.pilihan_ganda.setStyleSheet("""
                QLabel {
                        padding: 10px;
                        border: 2px solid transparent;
                        border-radius: 15px;
                        background-color: transparent;
                }
                QLabel:hover {
                        border: 2px solid #2D8AE0;
                        background-color: rgba(211, 211, 211, 0.5);
                }
                """)

                # Mengatur gambar dan kursor
                self.pilihan_ganda.setPixmap(QPixmap("Assets/Dashboard/Left_bar/MULTIPLE_CHOICE.png"))
                self.pilihan_ganda.setCursor(QCursor(Qt.PointingHandCursor))

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
                        # Inisialisasi ShadowWidget
                self.Sesi = ShadowWidget(self.Main_konten)
                self.Sesi.setObjectName(u"Sesi")
                self.Sesi.setGeometry(QRect(90, 30, 921, 121))
                self.Sesi.setMaximumSize(QSize(1920, 1080))
                self.Sesi.setAcceptDrops(False)
                self.Sesi.setStyleSheet(u"QWidget {\n"
                "    background-color: #E36B37;\n"
                "    border: 1px solid #E36B37;  \n"
                "    border-radius: 20px;\n"
                "}")

                #=============================================================
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

                #=============================================================
                #======================= Panduan Button ======================
                #=============================================================
                self.btn_panduan = QToolButton(self.Sesi)
                self.btn_panduan.setObjectName(u"btn_panduan")
                self.btn_panduan.setGeometry(QRect(700, 20, 181, 71))
                self.btn_panduan.setContextMenuPolicy(Qt.NoContextMenu)
                icon1 = QIcon()
                icon1.addFile(u"Assets/Dashboard/Sesi/Panduan.png", QSize(), QIcon.Normal, QIcon.Off)
                self.btn_panduan.setIcon(icon1)
                self.btn_panduan.setIconSize(QSize(1000, 1000))
                self.btn_panduan.setCheckable(True)
                self.btn_panduan.setAutoRepeat(False)
                self.btn_panduan.setToolButtonStyle(Qt.ToolButtonIconOnly)
                self.btn_panduan.setCursor(QCursor(Qt.PointingHandCursor))

                #=============================================================
                #======================= Island ==============================
                #=============================================================
                self.Land_2 = QLabel(self.Main_konten)
                self.Land_2.setObjectName(u"Land_2")
                self.Land_2.setGeometry(QRect(410, 650, 471, 321))
                self.Land_2.setPixmap(QPixmap(u"Assets/Dashboard/Island/Island_2.png"))
                self.Land_2.setScaledContents(True)

                self.Land_1 = QLabel(self.Main_konten)
                self.Land_1.setObjectName(u"Land_1")
                self.Land_1.setGeometry(QRect(150, 170, 701, 461))
                self.Land_1.setPixmap(QPixmap(u"Assets/Dashboard/Island/Island_1.png"))
                self.Land_1.setScaledContents(True)
                self.Tangga = QLabel(self.Main_konten)
                self.Tangga.setObjectName(u"Tangga")
                self.Tangga.setGeometry(QRect(420, 500, 141, 191))
                self.Tangga.setStyleSheet(u"QLabel {\n"
                "    background-color: transparent;\n"
                "}")
                self.Tangga.setPixmap(QPixmap(u"Assets/Dashboard/Island/Ladder.png"))
                self.Tangga.setScaledContents(True)

                #=============================================================
                #======================= Start Button ========================
                #=============================================================
                self.Start_btn = CustomToolButton(self.Main_konten, 
                                                        "Assets/Dashboard/Island/Start.png",
                                                        pressed="Assets/Dashboard/Island/Start_Pressed.png", 
                                                        hover="Assets/Dashboard/Island/Start.png")
                self.Start_btn.setObjectName(u"Start_btn")
                self.Start_btn.setGeometry(QRect(560, 240, 181, 191))
                self.Start_btn.setMaximumSize(QSize(1000, 1000))
                self.Start_btn.setContextMenuPolicy(Qt.NoContextMenu)
                self.Start_btn.setAutoFillBackground(False)
                self.Start_btn.setStyleSheet(u"QToolButton {\n"
                                                "    border: none;                  /* Menghilangkan border */\n"
                                                "    background: transparent;       /* Membuat background transparan */\n"
                                                "    padding: 0;                    /* Menghilangkan padding */\n"
                                                "    cursor: pointer;               /* Mengubah kursor menjadi pointer */\n"
                                                "}\n"
                                                "")
                icon2 = QIcon()
                icon2.addFile(u"Assets/Dashboard/Island/Start.png", QSize(), QIcon.Normal, QIcon.Off)
                self.Start_btn.setIcon(icon2)
                self.Start_btn.setIconSize(QSize(500, 500))
                self.Start_btn.setCheckable(False)
                self.Start_btn.setAutoRepeat(False)
                self.Start_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
                self.Start_btn.setAutoRaise(False)

                #=============================================================
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
                icon3.addFile(u"Assets/Dashboard/Island/Next_Button.png", QSize(), QIcon.Normal, QIcon.Off)
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

                #=============================================================
                #======================= Chest Button ========================
                #=============================================================
                # Inisialisasi CustomToolButton
                self.Next_button_island_3 = CustomToolButton(self.Main_konten, 
                                                                "Assets/Dashboard/Island/Chest.png",
                                                                pressed="Assets/Dashboard/Island/Chest_Pressed.png", 
                                                                hover="Assets/Dashboard/Island/Chest.png")
                self.Next_button_island_3.setObjectName(u"Next_button_island_3")
                self.Next_button_island_3.setGeometry(QRect(480, 700, 100, 80))
                self.Next_button_island_3.setMaximumSize(QSize(100, 100))
                font = QFont()
                font.setKerning(True)
                self.Next_button_island_3.setFont(font)
                self.Next_button_island_3.setContextMenuPolicy(Qt.NoContextMenu)
                self.Next_button_island_3.setAutoFillBackground(False)
                self.Next_button_island_3.setStyleSheet(u"QToolButton {\n"
                "    border: none;                  /* Menghilangkan border */\n"
                "    background: transparent;       /* Membuat background transparan */\n"
                "    padding: 0;                    /* Menghilangkan padding */\n"
                "    cursor: pointer;               /* Mengubah kursor menjadi pointer */\n"
                "}\n"
                "")
                icon4 = QIcon()
                icon4.addFile(u"Assets/Dashboard/Island/Chest.png", QSize(), QIcon.Normal, QIcon.Off)
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
                icon5.addFile(u"Assets/Dashboard/Island/Finish_button.png", QSize(), QIcon.Normal, QIcon.Off)
                self.Next_button_island_5.setIcon(icon5)
                self.Next_button_island_5.setIconSize(QSize(200, 200))
                self.Next_button_island_5.setCheckable(False)
                self.Next_button_island_5.setAutoRepeat(False)
                self.Next_button_island_5.setToolButtonStyle(Qt.ToolButtonIconOnly)
                self.Next_button_island_5.setAutoRaise(False)

                #=============================================================
                #======================= Maskot Monyet ========================
                #=============================================================
                self.Maskot_monyet_island = QLabel(self.Main_konten)
                self.Maskot_monyet_island.setObjectName(u"Maskot_monyet_island")
                self.Maskot_monyet_island.setGeometry(QRect(270, 200, 231, 211))
                self.Maskot_monyet_island.setStyleSheet(u"QLabel {\n"
        "    background-color: transparent;  /* Membuat background transparan */\n"
        "    border: none;                   /* Menghilangkan border */\n"
        "}\n"
        "")
                self.Maskot_monyet_island.setPixmap(QPixmap(u"Assets/Dashboard/Island/maskot_island.png"))
                self.Maskot_monyet_island.setScaledContents(True)


                #=============================================================
                #======================= Right Bar ===========================
                #=============================================================

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
                "color: rgb(0, 0, 0);\n"  # Mengatur warna teks menjadi hitam
                "}")

                #=============================================================
                #======================= Progress Bar ========================
                #=============================================================
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

                #=============================================================
                #======================= Count Materi ========================
                #=============================================================
                self.Count_materi = QLabel(self.Progres)
                self.Count_materi.setObjectName(u"Count_materi")
                self.Count_materi.setGeometry(QRect(300, 80, 61, 41))
                self.Count_materi.setFont(font4)
                self.Count_materi.setStyleSheet(u"QLabel{\n"
                "background-color: rgb(255, 255, 255);\n"
                "color: rgb(0, 0, 0);\n"
                "}")
                #=============================================================
                #======================= Motivasi ============================
                #=============================================================
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

                #=============================================================
                #======================= Belajar Button ======================
                #=============================================================
                self.Belajar_button = CustomToolButton(self.Progres, 
                                                        "Assets/Dashboard/Right_bar/Button_Belajar.png",
                                                        pressed="Assets/Dashboard/Right_bar/Button_Belajar_Pressed.png",
                                                        hover="Assets/Dashboard/Right_bar/Button_Belajar.png")
                self.Belajar_button.setObjectName(u"Belajar_button")
                self.Belajar_button.setGeometry(QRect(30, 180, 321, 51))
                self.Belajar_button.setStyleSheet(u"QToolButton {\n"
                                                        "    background-color: transparent;  /* Membuat background transparan */\n"
                                                        "}\n"
                                                        "")
                self.Belajar_button.setIconSize(QSize(321, 51))
                self.Belajar_button.setCheckable(False)
                self.Belajar_button.setAutoRepeat(False)
                self.Belajar_button.setToolButtonStyle(Qt.ToolButtonIconOnly)
                self.Belajar_button.setAutoRaise(False)

                self.progressBar.raise_()
                self.Belajar_button.raise_()
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

                self.karakter.setPixmap(QPixmap(u"Assets/Dashboard/Right_bar/Card2.png"))
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
                "color: rgb(0, 0, 0);\n"
                "}")

                #=============================================================
                #======================= Profile Button ======================
                #=============================================================
                self.Profile_button = CustomToolButton(self.Profile, 
                                                "Assets/Dashboard/Right_bar/Profile.png",
                                                pressed="Assets/Dashboard/Right_bar/Profile_pressed.png", 
                                                hover="Assets/Dashboard/Right_bar/Profile.png")
                self.Profile_button.setObjectName(u"Profile_button")
                self.Profile_button.setGeometry(QRect(40, 70, 311, 51))
                self.Profile_button.setStyleSheet(u"QToolButton {\n"
                                                "    background-color: transparent;  /* Membuat background transparan */\n"
                                                "}\n"
                                                "")
                self.Profile_button.setIconSize(QSize(311, 51))
                self.Profile_button.setCheckable(False)
                self.Profile_button.setAutoRepeat(False)
                self.Profile_button.setToolButtonStyle(Qt.ToolButtonIconOnly)
                self.Profile_button.setAutoRaise(False)

                #=============================================================
                self.layoutWidget1 = QWidget(self.RightBar)
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
                self.horizontalLayout_5.setSpacing(0)
                self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
                self.segitiga = QLabel(self.layoutWidget1)
                self.segitiga.setObjectName(u"segitiga")
                self.segitiga.setMinimumSize(QSize(40, 0))
                self.segitiga.setMaximumSize(QSize(40, 16777215))
                self.segitiga.setPixmap(QPixmap(u"Assets/Points.png"))
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
                
                #=============================================================
                #===================== Pop Up Panduan ========================
                #=============================================================
                self.Pop_up_bacground = QWidget(self.Main_konten)
                self.Pop_up_bacground.setObjectName(u"Pop_up_bacground")
                self.Pop_up_bacground.setGeometry(QRect(-1, -1, 1501, 1061))
                self.Pop_up_bacground.setStyleSheet(u" background-color: rgba(0, 0, 0, 128); /* Black background with 50% opacity */")
                self.Pop_up_bacground.setVisible(False)

                self.panduan_pop_up = QWidget(self.Pop_up_bacground)
                self.panduan_pop_up.setObjectName(u"panduan_pop_up")
                self.panduan_pop_up.setGeometry(QRect(200, 120, 1141, 700))
                self.panduan_pop_up.setMaximumSize(QSize(1142, 700))
                self.panduan_pop_up.setStyleSheet(u" background-color: #E36B37;  /* Background color */\n"
        "            border-radius: 30px;        /* Border radius for rounded corners */")
                
                #=============================================================
                #======================= Kembali Button ======================
                #=============================================================
                self.Kembali = QToolButton(self.panduan_pop_up)
                self.Kembali.setObjectName(u"Kembali")
                self.Kembali.setGeometry(QRect(40, 10, 151, 61))
                self.Kembali.setContextMenuPolicy(Qt.NoContextMenu)
                icon6 = QIcon()
                icon6.addFile(u"Assets/Dashboard/Kembali.png", QSize(), QIcon.Normal, QIcon.Off)
                self.Kembali.setIcon(icon6)
                self.Kembali.setIconSize(QSize(1000, 1000))
                self.Kembali.setCheckable(True)
                self.Kembali.setAutoRepeat(False)
                self.Kembali.setToolButtonStyle(Qt.ToolButtonIconOnly)
                self.Kembali.setCursor(QCursor(Qt.PointingHandCursor))

                self.Line = QLabel(self.panduan_pop_up)
                self.Line.setObjectName(u"Line")
                self.Line.setGeometry(QRect(40, 70, 1051, 6))
                self.Line.setStyleSheet(u"QLabel{\n"
        "	background-color: rgb(146, 61, 24);\n"
        "	border-radius: 90px\n"
        "\n"
        "}")
                self.Judul_panduan = QLabel(self.panduan_pop_up)
                self.Judul_panduan.setObjectName(u"Judul_panduan")
                self.Judul_panduan.setGeometry(QRect(390, 110, 651, 61))
                font9 = QFont()
                font9.setFamilies([u"Jellee"])
                font9.setPointSize(36)
                self.Judul_panduan.setFont(font9)
                self.Judul_panduan.setStyleSheet(u"QLabel{\n"
        "color : rgb(255, 255, 255);\n"
        "	background-color: transparent;\n"
        "}")
                self.Maskot_panduan = QLabel(self.panduan_pop_up)
                self.Maskot_panduan.setObjectName(u"Maskot_panduan")
                self.Maskot_panduan.setGeometry(QRect(70, 80, 281, 301))
                self.Maskot_panduan.setPixmap(QPixmap(u"Assets/Dashboard/Maskot_popup.png"))
                self.Maskot_panduan.setScaledContents(True)
                self.Panduan = QLabel(self.panduan_pop_up)
                self.Panduan.setObjectName(u"Panduan")
                self.Panduan.setGeometry(QRect(390, 180, 531, 101))
                self.Panduan.setFont(font7)
                self.Panduan.setStyleSheet(u"QLabel{\n"
        "color : rgb(255, 255, 255);\n"
        "}")
                self.Panduan.setWordWrap(True)
                self.Widget_tip = QWidget(self.panduan_pop_up)
                self.Widget_tip.setObjectName(u"Widget_tip")
                self.Widget_tip.setGeometry(QRect(390, 290, 701, 171))
                self.Widget_tip.setStyleSheet(u"QWidget{\n"
        "	background-color: rgb(146, 61, 24);\n"
        "	border-radius: 20px;\n"
        "}")
                self.Label_tip = QLabel(self.Widget_tip)
                self.Label_tip.setObjectName(u"Label_tip")
                self.Label_tip.setGeometry(QRect(30, 20, 41, 21))
                font10 = QFont()
                font10.setFamilies([u"Jellee"])
                font10.setPointSize(15)
                self.Label_tip.setFont(font10)
                self.Label_tip.setStyleSheet(u"QLabel {\n"
        "\n"
        "	color: rgb(255, 103, 37);\n"
        "}")
                self.Tips = QLabel(self.Widget_tip)
                self.Tips.setObjectName(u"Tips")
                self.Tips.setGeometry(QRect(30, 50, 641, 101))
                self.Tips.setFont(font5)
                self.Tips.setStyleSheet(u"QLabel{\n"
        "color : rgb(255, 255, 255)\n"
        "}")
                self.Tips.setWordWrap(True)
                self.Kata_kunci = QLabel(self.panduan_pop_up)
                self.Kata_kunci.setObjectName(u"Kata_kunci")
                self.Kata_kunci.setGeometry(QRect(50, 410, 121, 31))
                font11 = QFont()
                font11.setFamilies([u"Jellee Roman"])
                font11.setPointSize(15)
                self.Kata_kunci.setFont(font11)
                self.Kata_kunci.setStyleSheet(u"QLabel {\n"
        "color : rgb(146, 61, 24)\n"
        "}")
                self.Isi_kata_kunci = QLabel(self.panduan_pop_up)
                self.Isi_kata_kunci.setObjectName(u"Isi_kata_kunci")
                self.Isi_kata_kunci.setGeometry(QRect(50, 450, 261, 51))
                self.Isi_kata_kunci.setFont(font8)
                self.Isi_kata_kunci.setStyleSheet(u"QLabel {\n"
        "color :rgb(255, 255, 255)\n"
        "}")
                
                #=============================================================
                #======================= Sound Button 1 ======================
                #=============================================================
                self.label_sound_1 = QLabel(self.panduan_pop_up)
                self.label_sound_1.setObjectName(u"label_sound_1")
                self.label_sound_1.setGeometry(QRect(40, 520, 331, 121))
                self.label_sound_1.setPixmap(QPixmap(u"Assets/Dashboard/Border_sound.png"))
                self.label_sound_1.setScaledContents(True)
                self.Button_sound_1 = QToolButton(self.panduan_pop_up)
                self.Button_sound_1.setObjectName(u"Button_sound_1")
                self.Button_sound_1.setGeometry(QRect(80, 530, 51, 51))
                self.Button_sound_1.setContextMenuPolicy(Qt.NoContextMenu)
                icon7 = QIcon()
                icon7.addFile(u"Assets/Dashboard/Button_sound.png", QSize(), QIcon.Normal, QIcon.Off)
                self.Button_sound_1.setIcon(icon7)
                self.Button_sound_1.setIconSize(QSize(1000, 1000))
                self.Button_sound_1.setCursor(QCursor(Qt.PointingHandCursor))

                # Set up sound effect 
                self.sound_effect_1 = QSoundEffect()
                self.sound_effect_1.setSource(QUrl.fromLocalFile("Assets/Dashboard/Sound_effect/Sushi_Kudasai.wav"))

                # Connect sound effect to button
                self.Button_sound_1.clicked.connect(self.sound_effect_1.play)

                self.Jepang_teks = QLabel(self.panduan_pop_up)
                self.Jepang_teks.setObjectName(u"Jepang_teks")
                self.Jepang_teks.setGeometry(QRect(150, 540, 201, 31))
                self.Jepang_teks.setFont(font8)
                self.Jepang_teks.setStyleSheet(u" QLabel {\n"
        "                color: rgb(255, 255, 255);\n"
        "                background-color: transparent;\n"
        "}")
                self.titik = QLabel(self.panduan_pop_up)
                self.titik.setObjectName(u"titik")
                self.titik.setGeometry(QRect(150, 560, 61, 21))
                font12 = QFont()
                font12.setPointSize(16)
                self.titik.setFont(font12)
                self.titik.setStyleSheet(u"QLabel{\n"
        "	color: rgb(146, 61, 24);\n"
        "	background-color: transparent ;\n"
        "}")
                self.titik_2 = QLabel(self.panduan_pop_up)
                self.titik_2.setObjectName(u"titik_2")
                self.titik_2.setGeometry(QRect(240, 560, 91, 21))
                font13 = QFont()
                font13.setPointSize(20)
                self.titik_2.setFont(font13)
                self.titik_2.setStyleSheet(u"QLabel{\n"
        "	color: rgb(146, 61, 24);\n"
        "	background-color: transparent ;\n"
        "}")
                self.label_romanji = QLabel(self.panduan_pop_up)
                self.label_romanji.setObjectName(u"label_romanji")
                self.label_romanji.setGeometry(QRect(140, 590, 201, 31))
                self.label_romanji.setFont(font4)
                self.label_romanji.setStyleSheet(u" QLabel {\n"
        "	           color: rgb(146, 61, 24);\n"
        "                background-color: transparent;\n"
        "}")
                
                #=============================================================
                #======================= Sound Button 2 ======================
                #=============================================================
                self.label_sound_2 = QLabel(self.panduan_pop_up)
                self.label_sound_2.setObjectName(u"label_sound_2")
                self.label_sound_2.setGeometry(QRect(430, 520, 311, 121))
                self.label_sound_2.setPixmap(QPixmap(u"Assets/Dashboard/Border_sound.png"))
                self.label_sound_2.setScaledContents(True)
                self.Button_sound_2 = QToolButton(self.panduan_pop_up)
                self.Button_sound_2.setObjectName(u"Button_sound_2")
                self.Button_sound_2.setGeometry(QRect(470, 530, 51, 51))
                self.Button_sound_2.setContextMenuPolicy(Qt.NoContextMenu)
                self.Button_sound_2.setIcon(icon7)
                self.Button_sound_2.setIconSize(QSize(1000, 1000))
                self.Button_sound_2.setCursor(QCursor(Qt.PointingHandCursor))

                # Set up sound effect
                self.sound_effect_2 = QSoundEffect()
                self.sound_effect_2.setSource(QUrl.fromLocalFile("Assets/Dashboard/Sound_effect/Mizu_desu.wav"))

                # Connect sound effect to button
                self.Button_sound_2.clicked.connect(self.sound_effect_2.play)


                self.Jepang_teks_2 = QLabel(self.panduan_pop_up)
                self.Jepang_teks_2.setObjectName(u"Jepang_teks_2")
                self.Jepang_teks_2.setGeometry(QRect(550, 540, 171, 31))
                self.Jepang_teks_2.setFont(font8)
                self.Jepang_teks_2.setStyleSheet(u" QLabel {\n"
        "                color: rgb(255, 255, 255);\n"
        "                background-color: transparent;\n"
        "}")
                self.titik_3 = QLabel(self.panduan_pop_up)
                self.titik_3.setObjectName(u"titik_3")
                self.titik_3.setGeometry(QRect(550, 560, 101, 21))
                self.titik_3.setFont(font12)
                self.titik_3.setStyleSheet(u"QLabel{\n"
        "	color: rgb(146, 61, 24);\n"
        "	background-color: transparent ;\n"
        "}")
                self.label_romanji_2 = QLabel(self.panduan_pop_up)
                self.label_romanji_2.setObjectName(u"label_romanji_2")
                self.label_romanji_2.setGeometry(QRect(550, 590, 181, 31))
                self.label_romanji_2.setFont(font4)
                self.label_romanji_2.setStyleSheet(u" QLabel {\n"
        "	           color: rgb(146, 61, 24);\n"
        "                background-color: transparent;\n"
        "}")
                
                #=============================================================
                #======================= Sound Button 3 ======================
                #=============================================================
                self.label_sound_3 = QLabel(self.panduan_pop_up)
                self.label_sound_3.setObjectName(u"label_sound_3")
                self.label_sound_3.setGeometry(QRect(770, 520, 331, 121))
                self.label_sound_3.setPixmap(QPixmap(u"Assets/Dashboard/Border_sound.png"))
                self.label_sound_3.setScaledContents(True)
                self.Button_sound_3 = QToolButton(self.panduan_pop_up)
                self.Button_sound_3.setObjectName(u"Button_sound_3")
                self.Button_sound_3.setGeometry(QRect(810, 530, 51, 51))
                self.Button_sound_3.setContextMenuPolicy(Qt.NoContextMenu)
                self.Button_sound_3.setIcon(icon7)
                self.Button_sound_3.setIconSize(QSize(1000, 1000))
                self.Button_sound_3.setCursor(QCursor(Qt.PointingHandCursor))

                # Set up sound effect
                self.sound_effect_3 = QSoundEffect()
                self.sound_effect_3.setSource(QUrl.fromLocalFile("Assets/Dashboard/Sound_effect/Ocha_kudasai.wav"))

                # Connect sound effect to button
                self.Button_sound_3.clicked.connect(self.sound_effect_3.play)

                self.Jepang_teks_3 = QLabel(self.panduan_pop_up)
                self.Jepang_teks_3.setObjectName(u"Jepang_teks_3")
                self.Jepang_teks_3.setGeometry(QRect(880, 540, 191, 31))
                self.Jepang_teks_3.setFont(font8)
                self.Jepang_teks_3.setStyleSheet(u" QLabel {\n"
        "                color: rgb(255, 255, 255);\n"
        "                background-color: transparent;\n"
        "}")
                self.titik_4 = QLabel(self.panduan_pop_up)
                self.titik_4.setObjectName(u"titik_4")
                self.titik_4.setGeometry(QRect(970, 560, 71, 21))
                self.titik_4.setFont(font12)
                self.titik_4.setStyleSheet(u"QLabel{\n"
        "	color: rgb(146, 61, 24);\n"
        "	background-color: transparent ;\n"
        "}")
                self.titik_5 = QLabel(self.panduan_pop_up)
                self.titik_5.setObjectName(u"titik_5")
                self.titik_5.setGeometry(QRect(880, 560, 71, 21))
                self.titik_5.setFont(font12)
                self.titik_5.setStyleSheet(u"QLabel{\n"
        "	color: rgb(146, 61, 24);\n"
        "	background-color: transparent ;\n"
        "}")
                self.label_romanji_3 = QLabel(self.panduan_pop_up)
                self.label_romanji_3.setObjectName(u"label_romanji_3")
                self.label_romanji_3.setGeometry(QRect(880, 590, 201, 31))
                self.label_romanji_3.setFont(font4)
                self.label_romanji_3.setStyleSheet(u" QLabel {\n"
        "	           color: rgb(146, 61, 24);\n"
        "                background-color: transparent;\n"
        "}")
                
                #=============================================================
                #======================= Pop up Mulai ========================
                #=============================================================
                self.Pop_up_mulai = QWidget(self.Pop_up_bacground)
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
                
                #=============================================================
                #======================= Sesi Raise ==========================
                #=============================================================
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
                self.Pop_up_bacground.raise_()


                self.horizontalLayout.addWidget(self.Main_konten)

                #=============================================================
                #======================= Fungsi_kode =========================
                #=============================================================

                #=============================================================
                #====================== Music Play ===========================
                #=============================================================
                        # Path to the music file
                music_file = "Assets/Dashboard/Sound/K.K.Slider_Dream_Animal_Crossing_New_Horizons_(OST).wav"

                # Check if the music file exists
                if not os.path.exists(music_file):
                        print(f"Error: Music file '{music_file}' does not exist")
                else:
                        print(f"Playing music file '{music_file}'")
                        self.sound_effect = QSoundEffect()
                        self.sound_effect.setSource(QUrl.fromLocalFile(music_file))
                        self.sound_effect.setLoopCount(-2)  # Infinite loop
                        self.sound_effect.setVolume(0.2)  # Set the volume (0.0 to 1.0)
                        self.sound_effect.play()

                #=============================================================
                #=================== Animasi Bounce Start ====================
                #=============================================================

                # Inisialisasi animasi
                self.bounce_animation = self.create_bounce_animation(self.Start_btn)

                # Hubungkan animasi dengan event tombol start
                self.Belajar_button.clicked.connect(self.bounce_animation.start)

                #=============================================================


                self.horizontalLayout.addWidget(self.Main_konten)

                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                self.btn_panduan.toggled.connect(self.panduan_pop_up.setVisible)
                self.btn_panduan.toggled.connect(self.Pop_up_bacground.setVisible)
                self.Kembali.toggled.connect(self.Pop_up_bacground.setHidden)
                self.Kembali.toggled.connect(self.panduan_pop_up.setHidden)

                QMetaObject.connectSlotsByName(MainWindow)

        # goto Left_bar pg
        def gotoPG(self):
                # Remove the current Left_bar if it exists
                if self.RightBar is not None:
                        self.RightBar.setParent(None)
                
                # Create a new Left_bar using the pagePG class
                self.page_pg = pagePG(self.centralwidget)
                self.page_pg.setupFrame()
                
                # Set the new Left_bar as the current Left_bar
                self.current_frame = self.page_pg.RightBar

        def retranslateUi(self, MainWindow):
                MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
                self.Keluar_button.setText("")
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
                self.Belajar_button.setText("")
                self.karakter.setText("")
                self.hd_iklan_2.setText(QCoreApplication.translate("MainWindow", u"Atur Profile Kamu!", None))
                self.Profile_button.setText("")
                self.Jepang.setText("")
                self.api.setText("")
                self.angka.setText(QCoreApplication.translate("MainWindow", u"0", None))
                self.segitiga.setText("")
                self.angka_2.setText(QCoreApplication.translate("MainWindow", u"500", None))
                self.Star.setText("")
                self.Stars_count.setText(QCoreApplication.translate("MainWindow", u"5", None))
                self.Kembali.setText(QCoreApplication.translate("MainWindow", u"...", None))
                self.Line.setText("")
                self.Judul_panduan.setText(QCoreApplication.translate("MainWindow", u"Unit 1 Panduan", None))
                self.Maskot_panduan.setText("")
                self.Panduan.setText(QCoreApplication.translate("MainWindow", u"Jelajahi kiat tata bahasa dan frasa kunci untuk unit ini", None))
                self.Label_tip.setText(QCoreApplication.translate("MainWindow", u"TIP", None))
                self.Tips.setText(QCoreApplication.translate("MainWindow", u"Bahasa Jepang memiliki tiga sistem penulisan. Dalam hiragana, yang dapat Anda gunakan untuk menulis sebagian besar kata dalam bahasa Jepang, setiap karakter mewakili suku kata", None))
                self.Kata_kunci.setText(QCoreApplication.translate("MainWindow", u"KATA KUNCI", None))
                self.Isi_kata_kunci.setText(QCoreApplication.translate("MainWindow", u"Pesan Makanan", None))
                self.label_sound_1.setText("")
                self.Button_sound_1.setText("")
                self.Jepang_teks.setText(QCoreApplication.translate("MainWindow", u"\u3059\u3057\u3001    \u304f\u3060\u3055\u3044\u3002", None))
                self.titik.setText(QCoreApplication.translate("MainWindow", u". . . . . . . .", None))
                self.titik_2.setText(QCoreApplication.translate("MainWindow", u". . . . . . . .", None))
                self.label_romanji.setText(QCoreApplication.translate("MainWindow", u"Sushi,   please.", None))
                self.label_sound_2.setText("")
                self.Button_sound_2.setText("")
                self.Jepang_teks_2.setText(QCoreApplication.translate("MainWindow", u"\u307f\u305a\u3067\u3059\u3002", None))
                self.titik_3.setText(QCoreApplication.translate("MainWindow", u". . . . . . . . .", None))
                self.label_romanji_2.setText(QCoreApplication.translate("MainWindow", u"It's water.", None))
                self.label_sound_3.setText("")
                self.Button_sound_3.setText("")
                self.Jepang_teks_3.setText(QCoreApplication.translate("MainWindow", u"\u304a\u3061\u3083   \u304f\u3060\u3055\u3044", None))
                self.titik_4.setText(QCoreApplication.translate("MainWindow", u". . . . . . . . .", None))
                self.titik_5.setText(QCoreApplication.translate("MainWindow", u". . . . . . . . .", None))
                self.label_romanji_3.setText(QCoreApplication.translate("MainWindow", u"Tea,       please.", None))
        # retranslateUi

        def create_bounce_animation(self, button):
                animation_group = QSequentialAnimationGroup()
                start_geometry = button.geometry()
                for i in range(10):
                        bounce_up = QPropertyAnimation(button, b"geometry")
                        bounce_up.setDuration(100 - i)
                        bounce_up.setStartValue(start_geometry)
                        bounce_up.setEndValue(QRect(start_geometry.x(), start_geometry.y() - 10, start_geometry.width(), start_geometry.height()))
                        bounce_up.setEasingCurve(QEasingCurve.OutBounce)

                        bounce_down = QPropertyAnimation(button, b"geometry")
                        bounce_down.setDuration(100 - i * 5)
                        bounce_down.setStartValue(QRect(start_geometry.x(), start_geometry.y() - 10, start_geometry.width(), start_geometry.height()))
                        bounce_down.setEndValue(start_geometry)
                        bounce_down.setEasingCurve(QEasingCurve.InBounce)

                        animation_group.addAnimation(bounce_up)
                        animation_group.addAnimation(bounce_down)
                return animation_group

        #=============================================================
        #======================= PopUp Panduan =======================
class pagePG(QFrame):
        def __init__(self, parent=None):
                super().__init__(parent)
                self.centralwidget = parent
        def setupFrame(self):
                font = QFont()
                font.setKerning(True)
                
                self.RightBar = QFrame(self.centralwidget)
                self.RightBar.setObjectName(u"RightBar")
                self.RightBar.setMaximumSize(QSize(400, 1080))
                self.RightBar.setStyleSheet(u"QFrame {\n"
        "    background-color: #EAEAEA;\n"
        "    padding: 0px;\n"
        "    margin: 0px;\n"
        "}")
                self.RightBar.setFrameShape(QFrame.StyledPanel)
                self.RightBar.setFrameShadow(QFrame.Raised)
                self.Progres = QWidget(self.RightBar)
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
                font2 = QFont()
                font2.setFamilies([u"Jellee Roman"])
                font2.setPointSize(16)
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
                icon5 = QIcon()
                icon5.addFile(u"Assets/PG/btn_atur.png", QSize(), QIcon.Normal, QIcon.Off)
                icon5.addFile(u"Assets/PG/btn_atur_pres.png", QSize(), QIcon.Selected, QIcon.On)
                self.Next_button_island_7.setIcon(icon5)
                self.Next_button_island_7.setIconSize(QSize(1000, 1000))
                self.Next_button_island_7.setCheckable(False)
                self.Next_button_island_7.setAutoRepeat(False)
                self.Next_button_island_7.setToolButtonStyle(Qt.ToolButtonIconOnly)
                self.Next_button_island_7.setAutoRaise(False)
                self.layoutWidget = QWidget(self.RightBar)
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
        #=============================================================

if __name__ == "__main__":
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = dashboard()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec())