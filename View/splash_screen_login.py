import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from splash_screen_register import SplashScreenRegister

#================================================#
#           -- SPLASH SCREEN LOGIN --            #
#================================================#
class SplashScreenLogin:
    ## -- Colors -- ##
    bg_win = "#FFFFFF" # background window
    bg_cnt = "#EAE7E7" # background content area
    fg_cnt = "#FFFFFF" # foreground content area
    fg_hdr = "#FF4949" # foreground header
    fg_swt = "#E32D2D" # foreground switch
    fg_btn = "#FF3939" # foreground button
    bg_btn = "#DB2A2A" # background button
    fg_op_1 = "#5FAFF9" # foreground optional 1 (facebook)
    fg_op_2 = "#FF3939" # foreground optional 2 (google)
    
    # Init Function
    def __init__(self):
        super().__init__()
        #-- Window Preferences --#
        flags = Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint # window title status
        w_width = 884 # width
        w_height = 490 # height

        # Hide window title and set transparent background
        self.setWindowFlags(flags)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(w_width, w_height)
        self.oldPos = self.pos()

        #-- Content --#
        '> Main Container: Including all'
        maincon_w = w_width
        maincon_h = w_height

        # main container initiation
        self.mainContainer = QWidget(self)
        self.mainContainer.setStyleSheet(f"background-color: {self.bg_win}; border-radius:30px;")
        self.mainContainer.setGeometry(0, 0,maincon_w, maincon_h)

        '> Header Container: Duahasa Logo & Two Switches "Masuk" and "Daftar"'
        hcon_w = maincon_w
        hcon_h = 80

        # header container initiation
        self.hcon = QWidget(self.mainContainer)
        self.hcon.setGeometry(0, 0, hcon_w, hcon_h)
        self.hconLayout = QHBoxLayout(self.hcon)
        self.hconLayout.setContentsMargins(10, 20, 10, 10)

        # logo
        logo_path = "assets/logo.png"
        logo_label = QLabel(self.hcon)
        pixmap = QPixmap(logo_path).scaled(167, 44, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(pixmap)
        self.hconLayout.addWidget(logo_label)
        self.hconLayout.addSpacing(200)   
        
        # button masuk (active)
        btn_m_path = "assets/masuk.png"
        button_masuk = QPushButton(self.hcon)
        button_masuk.setFixedSize(150, 33)
        pixmap = QPixmap(btn_m_path).scaled(150, 33, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        button_masuk.setIcon(pixmap)
        button_masuk.setIconSize(pixmap.size())
        self.hconLayout.addWidget(button_masuk)
        self.hconLayout.addSpacing(-10)
       

        # button daftar (inactive)
        btn_d_path = "assets/daftar.png"
        button_daftar = QPushButton(self.hcon)
        button_daftar.setFixedSize(142, 33)
        pixmap = QPixmap(btn_d_path).scaled(150, 33, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        button_daftar.setIcon(pixmap)
        button_daftar.setIconSize(pixmap.size())
        self.hconLayout.addWidget(button_daftar)
        
        # goto daftar when pressed
        button_daftar.clicked.connect(self.gotoRegister)

        # Button exit
        btn_x_path = "assets/exit.png"
        button_exit = QPushButton(self.hcon)
        button_exit.setFixedSize(32, 32)
        pixmap = QPixmap(btn_x_path).scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        button_exit.setIcon(pixmap)
        button_exit.setIconSize(pixmap.size())
        button_exit.move(w_width-45, 12)
        button_exit.clicked.connect(self.close)

        # Character
        img_path = "assets/character.png"
        img_label = QLabel(self.mainContainer)
        pixmap = QPixmap(img_path).scaled(330, 330, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        img_label.setPixmap(pixmap)
        img_label.move(90, 100)

        # Container 1
        self.fieldContainer = QWidget(self)
        self.fieldContainer.setStyleSheet(f"background-color: {self.bg_cnt}; border-radius:20px;")
        self.fieldContainer.setGeometry(0, 0, 450, 380)
        self.fieldContainer.move(410, 90)

        # Container 2
        self.contentContainer = QWidget(self)
        self.contentContainer.setStyleSheet(f"background-color: {self.bg_win}; border-radius:15px;")
        self.contentContainer.setGeometry(0, 0, 438, 360)
        self.contentContainer.move(416, 95)
    
        # Polygon
        polypath = "assets/poly.png"
        polylabel = QLabel(self.mainContainer)
        pixmap = QPixmap(polypath).scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        polylabel.setPixmap(pixmap)
        polylabel.move(550, 70)

        self.hconLayout.setAlignment(Qt.AlignCenter) 

        # Load Font
        QFontDatabase.addApplicationFont("assets/Jelle-Roman.otf")

        # Header text
        font_size = 20
        font = "Jellee"
        self.greet_lbl = QLabel("Selamat Datang Kembali!", self.contentContainer)
        QFont(font, font_size).setLetterSpacing(QFont.PercentageSpacing, 109) 
        self.greet_lbl.setFont(QFont(font, font_size))
        self.greet_lbl.setStyleSheet(f"color: {self.fg_hdr};")
        self.greet_lbl.move(55, 15)

        # email or username field
        contentFont = QFont(font, font_size - 5)
        self.usernameField = QWidget(self.contentContainer)
        self.usernameField.setStyleSheet(f"background-color: {self.bg_win}; border-radius: 10px; padding: 10px;")
        self.usernameField.setGeometry(0, 0, 322, 50)
        self.usernameField.move(60, 70)

        # email or username input
        username_input_width = self.usernameField.width()  # Get the width of the usernameField
        username_input_height = self.usernameField.height()  # Get the height of the usernameField

        self.usernameInput = QLineEdit(self.usernameField)
        self.usernameInput.setFixedSize(username_input_width, username_input_height)
        self.usernameInput.setStyleSheet(f"border-radius: 20px; border: 3px solid {self.bg_cnt}; color: #929292;")
        self.usernameInput.setFont(QFont(font, font_size - 5))
        self.usernameInput.setPlaceholderText("Email atau username")

        # Password field
        self.passwordField = QWidget(self.contentContainer)
        self.passwordField.setStyleSheet(f"background-color: {self.bg_win}; border-radius: 10px; padding: 10px;")
        self.passwordField.setGeometry(0, 0, 322, 50)
        self.passwordField.move(60, 140)

        # Password input
        password_input_width = self.passwordField.width()  # Get the width of the passwordField
        password_input_height = self.passwordField.height()  # Get the height of the passwordField

        self.passwordInput = QLineEdit(self.passwordField)
        self.passwordInput.setFixedSize(password_input_width, password_input_height)
        self.passwordInput.setStyleSheet(f"border-radius: 20px; border: 3px solid {self.bg_cnt}; color: #929292;")
        self.passwordInput.setFont(contentFont)
        self.passwordInput.setPlaceholderText("Password")

        # Lupa Password button
        self.lupaPassBtn = QPushButton("LUPA?", self.contentContainer)
        self.lupaPassBtn.setFont(contentFont)
        self.lupaPassBtn.setStyleSheet("color: #DEDEDE;")
        self.lupaPassBtn.setGeometry(290, 145, 85, 40)

        # Masuk Button
        self.masuk_bg = QWidget(self.contentContainer)
        self.masuk_bg.setStyleSheet(f"background-color: {self.bg_btn};")
        self.masuk_bg.setGeometry(0, 0, 322, 40)
        self.masuk_bg.move(60, 217)

        self.masuk_btn = QPushButton("MASUK", self.contentContainer)
        self.masuk_btn.setFont(QFont(font, font_size - 8))
        self.masuk_btn.setStyleSheet(f"background-color: {self.fg_btn}; color: white;")
        self.masuk_btn.setGeometry(0, 0, 322, 40)
        self.masuk_btn.move(60, 210)

        # Separator
        img_path = "assets/separator.png"
        img_label = QLabel(self.contentContainer)
        pixmap = QPixmap(img_path).scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        img_label.setPixmap(pixmap)
        img_label.move(70, 270)

        # Facebook Button
        self.fb_btn = QPushButton(self.contentContainer)
        self.fb_btn.setIcon(QIcon("assets/facebook.png"))
        self.fb_btn.setGeometry(85, 285, 140, 50)
        self.fb_btn.setIconSize(QSize(130, 130))
        
        # Google Button
        self.ggl_btn = QPushButton(self.contentContainer)
        self.ggl_btn.setIcon(QIcon("assets/google.png"))
        self.ggl_btn.setGeometry(225, 285, 140, 50)
        self.ggl_btn.setIconSize(QSize(130, 130))

        # TOS info
        img_path = "assets/terms.png"
        img_label = QLabel(self.contentContainer)
        pixmap = QPixmap(img_path).scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        img_label.setPixmap(pixmap)
        img_label.move(140, 340)

    # show second window
    def gotoRegister(self):
        self.second_window = SplashScreenRegister()
        self.second_window.show()
        self.hide()

    # Click (to Drag) window Function
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPosition().toPoint()
    
    # Drag (to Draggable) window Function
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # Calculate the mouse position relative to the main window
            global_pos = event.globalPosition().toPoint()
            relative_pos = self.mapFromGlobal(global_pos)

            # Check if the mouse is within the bounds of the header container
            header_rect = self.hcon.geometry()
            if header_rect.contains(relative_pos):
                delta = global_pos - self.oldPos
                self.move(self.pos() + delta)
                self.oldPos = global_pos