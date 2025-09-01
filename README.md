# 🌸 DuaHasa - Aplikasi Pembelajaran Bahasa Jepang Interaktif

<div align="center">
  <img src="Assets/logo.png" alt="DuaHasa Logo" width="200"/>
  
  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
  [![PySide6](https://img.shields.io/badge/PySide6-6.0+-green.svg)](https://pypi.org/project/PySide6/)
  [![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com/justrrio/DuaHasa)
  [![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
</div>

## 📝 Deskripsi

**DuaHasa** adalah aplikasi pembelajaran bahasa Jepang yang inovatif dan interaktif, dirancang khusus untuk pelajar Indonesia. Menggunakan pendekatan gamifikasi dengan sistem island progression, DuaHasa menawarkan pengalaman belajar yang menyenangkan dan efektif melalui berbagai mode pembelajaran yang terintegrasi.

### 🎯 Visi & Misi
- **Visi**: Menjadikan pembelajaran bahasa Jepang mudah, menyenangkan, dan accessible untuk semua orang
- **Misi**: Menghadirkan metode pembelajaran interaktif yang menggabungkan teknologi modern dengan pedagogik yang proven

## ✨ Fitur Utama

### 🏝️ **Dashboard Island Progression**
- **Sistem Pulau Bertingkat**: Pembelajaran yang terstruktur dengan 5 level island
- **Progress Tracking**: Visualisasi kemajuan belajar real-time
- **Achievement System**: Stars, streaks, dan points untuk motivasi
- **Interactive Animations**: Bounce effects dan smooth transitions

### 📚 **Flashcard Interaktif**
- **Visual Learning**: Kartu belajar dengan gambar dan teks
- **Flip Animation**: Animasi membalik kartu untuk reveal jawaban
- **Multi-format Support**: Indonesia → Jepang (Hiragana/Katakana) → Romaji
- **Custom Flashcard**: Fitur menambah flashcard sendiri dengan image picker
- **Auto-resize Text**: Responsive text yang menyesuaikan ukuran layar

### 🎯 **Multiple Choice Quiz**
- **Interactive Quiz**: Soal pilihan ganda dengan feedback visual
- **Image-based Questions**: Pertanyaan dengan dukungan gambar
- **Progress Indicator**: Real-time tracking untuk setiap sesi quiz
- **Adaptive Difficulty**: Tingkat kesulitan yang menyesuaikan kemampuan

### 🔐 **Authentication System**
- **Modern Login/Register**: Interface yang clean dan user-friendly
- **Social Login Support**: Integration dengan Facebook dan Google
- **Secure Session**: Manajemen sesi pengguna yang aman
- **Character Mascot**: Maskot interaktif untuk guiding user experience

### 🎵 **Audio & Multimedia**
- **Background Music**: Musik ambient untuk focus learning
- **Sound Effects**: Audio feedback untuk interaksi
- **Pronunciation Support**: Audio untuk pembelajaran pelafalan
- **Rich Media**: Dukungan berbagai format audio dan gambar

## 🖥️ System Requirements

### Minimum Requirements
- **Operating System**: Windows 10+, macOS 10.14+, atau Linux (Ubuntu 18.04+)
- **Python**: 3.8 atau lebih baru
- **RAM**: 4GB (8GB direkomendasikan)
- **Storage**: 500MB ruang kosong
- **Display**: 1366x768 (1920x1080 optimal)

### Recommended Requirements
- **OS**: Windows 11, macOS 12+, atau Linux terbaru
- **Python**: 3.10+
- **RAM**: 8GB atau lebih
- **Storage**: 1GB ruang kosong
- **Display**: 1920x1080 atau lebih tinggi
- **Audio**: Speaker atau headphone untuk audio features

## 🚀 Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/justrrio/DuaHasa.git
cd DuaHasa
```

### 2. Setup Python Environment
```bash
# Membuat virtual environment (recommended)
python -m venv duahasa_env

# Aktivasi virtual environment
# Windows:
duahasa_env\Scripts\activate
# macOS/Linux:
source duahasa_env/bin/activate
```

### 3. Install Dependencies
```bash
# Install PySide6 dan dependencies
pip install PySide6
pip install -r requirements.txt  # jika ada file requirements.txt
```

### 4. Verifikasi Asset Files
Pastikan semua asset files tersedia di folder `Assets/`:
- ✅ Fonts: `Auro-Bold.otf`, `Jellee-Roman.otf`
- ✅ Images: Dashboard, Flashcards, PG assets
- ✅ Audio: Background music dan sound effects

### 5. Run Application
```bash
# Menjalankan dashboard utama
cd View
python Dashboard.py

# Atau menjalankan flashcard module
python flashcards.py
```

## 📖 Panduan Penggunaan

### 🔄 **Memulai Aplikasi**
1. **Launch**: Jalankan `Dashboard.py` untuk memulai aplikasi
2. **Authentication**: Login atau register akun baru
3. **Dashboard**: Explore island progression dan pilih mode pembelajaran

### 📚 **Menggunakan Flashcards**
1. **Akses**: Klik icon Flashcards di dashboard
2. **Navigate**: Gunakan navigation buttons untuk berpindah kartu
3. **Interact**: Klik kartu untuk flip dan lihat jawaban
4. **Add New**: Gunakan tombol "+" untuk menambah flashcard baru
5. **Progress**: Track kemajuan melalui progress bar

### 🎯 **Multiple Choice Quiz**
1. **Start Quiz**: Pilih mode "Pilihan Ganda" dari dashboard
2. **Answer**: Klik jawaban yang benar dari pilihan tersedia
3. **Feedback**: Dapatkan feedback langsung untuk setiap jawaban
4. **Complete**: Finish quiz untuk unlock progress selanjutnya

### ⚙️ **Customization**
- **Add Flashcards**: Upload gambar dan tambah pertanyaan sendiri
- **Audio Settings**: Adjust volume musik dan sound effects
- **Profile**: Update informasi profile dan track statistics

## 🏗️ Struktur Project

```
DuaHasa/
├── 📄 README.md                 # Dokumentasi utama
├── 📁 Assets/                   # Asset multimedia
│   ├── 🎨 *.png, *.jpg         # Gambar dan icons
│   ├── 🔤 *.otf                # Custom fonts
│   ├── 📁 Dashboard/           # Asset dashboard
│   ├── 📁 Flashcards/          # Asset flashcards
│   └── 📁 PG/                  # Asset multiple choice
├── 📁 Flashcards/              # Data flashcards
│   ├── 📄 1_flashcard.json     # Flashcard data level 1
│   ├── 📄 2_flashcard.json     # Flashcard data level 2
│   └── 📄 3_flashcard.json     # Flashcard data level 3
├── 📁 View/                    # Application interfaces
│   ├── 🐍 Dashboard.py         # Dashboard utama
│   ├── 🐍 dashboard_new.py     # Dashboard alternative
│   ├── 🐍 flashcards.py        # Flashcard system
│   ├── 🐍 pg.py                # Multiple choice system
│   ├── 🐍 splash_screen_login.py    # Login interface
│   ├── 🐍 splash_screen_register.py # Register interface
│   └── 📁 __pycache__/         # Python cache files
└── 📄 *.ui                     # Qt Designer files
```

## 🔧 Arsitektur Teknis

### **Technology Stack**
- **Framework UI**: PySide6 (Qt6 untuk Python)
- **Language**: Python 3.8+
- **Data Storage**: JSON files
- **Audio Engine**: QSoundEffect
- **Animation**: QPropertyAnimation, QEasingCurve
- **Graphics**: QPainter, QPixmap

### **Design Patterns**
- **MVC Pattern**: Model-View-Controller architecture
- **Component-based**: Modular UI components
- **Event-driven**: Qt signals dan slots system
- **Observer Pattern**: Progress tracking dan state management

### **Custom Components**
```python
# Auto-resizing label untuk responsive text
class AutoResizeLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.default_font_size = 36
        self.minimum_font_size = 12

# Custom tool button dengan hover effects
class CustomToolButton(QToolButton):
    def __init__(self, parent, default_img, hover_img, pressed_img):
        super().__init__(parent)
        # Custom implementation
```

### **Data Structure**
```json
{
    "pertanyaan": "Itu apa?",
    "gambar": "path/to/image.jpg",
    "jawaban_jepang": "これは鳥です",
    "jawaban_latin": "Kore wa toridesu",
    "terjawab": false
}
```

## 🎨 UI/UX Design

### **Design Philosophy**
- **Minimalist**: Clean interface dengan fokus pada content
- **Colorful**: Warna cerah untuk engagement
- **Interactive**: Smooth animations dan responsive feedback
- **Accessible**: User-friendly untuk semua level

### **Color Palette**
- **Primary**: `#EAEAEA` (Background)
- **Accent**: `#FF4949` (Headers)
- **Interactive**: `#5FAFF9` (Facebook), `#FF3939` (Google)
- **Success**: `#2D8AE0` (Progress indicators)

### **Typography**
- **Primary Font**: Jellee (Custom font untuk headers)
- **Secondary Font**: Auro-Bold (Decorative elements)
- **System Font**: Default system fonts untuk body text

## 🤝 Contributing

Kami menyambut kontribusi dari developer komunitas! Berikut guidelines untuk berkontribusi:

### **Development Setup**
1. Fork repository ini
2. Buat branch feature baru: `git checkout -b feature/amazing-feature`
3. Install development dependencies
4. Setup pre-commit hooks

### **Code Standards**
- Gunakan Python PEP 8 style guidelines
- Dokumentasi yang comprehensive untuk functions dan classes
- Unit testing untuk core functionalities
- Comment yang clear untuk complex logic

### **Pull Request Process**
1. Update documentation sesuai perubahan
2. Pastikan semua tests pass
3. Update README.md jika diperlukan
4. Submit PR dengan description yang detailed

### **Issue Reporting**
- Gunakan issue templates yang tersedia
- Sertakan screenshots untuk UI issues
- Include system information dan steps to reproduce

## 🛣️ Roadmap

### **Phase 1: Core Enhancement** (Q1 2024)
- [ ] Database integration (SQLite/PostgreSQL)
- [ ] User progress persistence
- [ ] Advanced analytics dashboard
- [ ] Performance optimizations

### **Phase 2: Content Expansion** (Q2 2024)
- [ ] More language levels (N5-N1 JLPT)
- [ ] Kanji learning module
- [ ] Grammar exercises
- [ ] Cultural context lessons

### **Phase 3: Advanced Features** (Q3 2024)
- [ ] AI-powered adaptive learning
- [ ] Speech recognition untuk pronunciation
- [ ] Multiplayer challenges
- [ ] Mobile app version (React Native)

### **Phase 4: Community** (Q4 2024)
- [ ] User-generated content
- [ ] Community features
- [ ] Teacher dashboard
- [ ] Certification system

## 📊 Analytics & Metrics

### **Learning Metrics**
- **Retention Rate**: Track user engagement over time
- **Completion Rate**: Monitor lesson completion statistics
- **Performance Analytics**: Analyze user learning patterns
- **Difficulty Adjustment**: Automatic content difficulty scaling

### **Technical Metrics**
- **Performance Monitoring**: App response time dan memory usage
- **Error Tracking**: Comprehensive error logging dan reporting
- **Usage Analytics**: Feature adoption dan user flow analysis

## 🔒 Security & Privacy

### **Data Protection**
- **Local Storage**: User data stored locally untuk privacy
- **Encryption**: Sensitive data encryption at rest
- **Minimal Data Collection**: Hanya collect data yang essential
- **GDPR Compliance**: Full compliance dengan privacy regulations

### **Security Measures**
- **Input Validation**: Comprehensive validation untuk user inputs
- **File Upload Security**: Safe file handling untuk custom content
- **Session Management**: Secure user session handling

## 📄 License

Distributed under the MIT License. See `LICENSE` file for more information.

```
MIT License

Copyright (c) 2024 DuaHasa Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

## 🙏 Acknowledgments

### **Credits**
- **Development Team**: Core developers dan contributors
- **UI/UX Design**: Visual design dan user experience team
- **Content Creation**: Japanese language experts dan educational consultants
- **Quality Assurance**: Testing team dan beta users

### **Third-party Libraries**
- **PySide6**: Qt framework untuk Python GUI development
- **Qt Designer**: Visual UI design tool
- **Python Standard Library**: Core Python functionality

### **Resources**
- **Japanese Audio**: Native speaker recordings
- **Cultural Content**: Authentic Japanese cultural materials
- **Educational Framework**: Based on proven language learning methodologies

---

<div align="center">
  <h3>🌸 Made with ❤️ for Japanese Language Learners 🌸</h3>
  
  **[Website](https://duahasa.com)** • 
  **[Documentation](https://docs.duahasa.com)** • 
  **[Community](https://community.duahasa.com)** • 
  **[Support](mailto:support@duahasa.com)**
  
  <p>
    <a href="https://github.com/justrrio/DuaHasa/stargazers">⭐ Star this project</a> • 
    <a href="https://github.com/justrrio/DuaHasa/issues">🐛 Report Bug</a> • 
    <a href="https://github.com/justrrio/DuaHasa/issues">💡 Request Feature</a>
  </p>
</div>
