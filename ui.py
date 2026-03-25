import sys
import numpy as np
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFileDialog, QComboBox,
    QSlider, QTextEdit, QStatusBar, QSplitter,
    QMessageBox, QApplication, QProgressBar
)
from PySide6.QtCore import Qt, QThread, Signal, QPropertyAnimation, QEasingCurve, QRect, QTimer, QSize
from PySide6.QtGui import QPixmap, QFont, QDragEnterEvent, QDropEvent, QColor
import qtawesome as qta

import image_process
import ascii_process

# Enhanced Modern QSS stylesheets with better animations
STYLES = {
    "light": """
        QMainWindow {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                        stop:0 #f5f7fa, stop:1 #e8ecf1);
        }
        QWidget {
            background-color: #f5f7fa;
        }
        QTextEdit {
            background-color: #ffffff;
            color: #1a1a1a;
            font-family: 'Courier New', monospace;
            border: 2px solid #d4d9e0;
            border-radius: 10px;
            padding: 8px;
            selection-background-color: #007bff;
            selection-color: white;
        }
        QTextEdit:focus {
            border: 2px solid #007bff;
        }
        QPushButton {
            background-color: #007bff;
            border: none;
            border-radius: 8px;
            padding: 10px 18px;
            color: #ffffff;
            font-weight: bold;
            font-size: 11px;
            min-height: 32px;
            outline: none;
        }
        QPushButton:hover {
            background-color: #0056b3;
            border: 1px solid #003d82;
        }
        QPushButton:pressed {
            background-color: #003d82;
            border: 1px solid #001a4d;
        }
        QPushButton:disabled {
            background-color: #cccccc;
            color: #999999;
        }
        QSlider::groove:horizontal {
            height: 7px;
            background: #d4d9e0;
            border-radius: 4px;
        }
        QSlider::handle:horizontal {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                        stop:0 #007bff, stop:1 #0056b3);
            width: 18px;
            margin: -6px 0;
            border-radius: 9px;
            border: 1px solid #0056b3;
        }
        QSlider::handle:horizontal:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                        stop:0 #0056b3, stop:1 #003d82);
            border: 1px solid #003d82;
        }
        QComboBox {
            border: 2px solid #d4d9e0;
            border-radius: 8px;
            padding: 6px 12px;
            background: white;
            color: #1a1a1a;
            font-weight: 500;
            min-height: 28px;
        }
        QComboBox:hover {
            border: 2px solid #007bff;
            background: #f9fbff;
        }
        QComboBox:focus {
            border: 2px solid #007bff;
        }
        QComboBox::drop-down {
            border: none;
            background: transparent;
        }
        QComboBox QAbstractItemView {
            border: 2px solid #d4d9e0;
            border-radius: 6px;
            background-color: white;
            color: #1a1a1a;
            selection-background-color: #007bff;
            selection-color: white;
            padding: 3px;
        }
        QLabel {
            color: #1a1a1a;
            font-weight: 500;
        }
        QStatusBar {
            background: #e8ecf1;
            color: #1a1a1a;
            border-top: 1px solid #d4d9e0;
        }
        QProgressBar {
            border: 2px solid #d4d9e0;
            border-radius: 6px;
            background-color: #f0f0f0;
            text-align: center;
            color: #1a1a1a;
        }
        QProgressBar::chunk {
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                             stop:0 #007bff, stop:1 #0056b3);
            border-radius: 4px;
        }
    """,
    "dark": """
        QMainWindow {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                        stop:0 #1e1e1e, stop:1 #0d0d0d);
        }
        QWidget {
            background-color: #1e1e1e;
        }
        QTextEdit {
            background-color: #2a2a2a;
            color: #e0e0e0;
            font-family: 'Courier New', monospace;
            border: 2px solid #404040;
            border-radius: 10px;
            padding: 8px;
            selection-background-color: #0d9aff;
            selection-color: #000000;
        }
        QTextEdit:focus {
            border: 2px solid #0d9aff;
        }
        QPushButton {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                             stop:0 #0d9aff, stop:1 #006db3);
            border: none;
            border-radius: 8px;
            padding: 10px 18px;
            color: #ffffff;
            font-weight: bold;
            font-size: 11px;
            min-height: 32px;
            outline: none;
        }
        QPushButton:hover {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                             stop:0 #1cb3ff, stop:1 #0080d9);
            border: 1px solid #0080d9;
        }
        QPushButton:pressed {
            background-color: #005a99;
            border: 1px solid #004477;
        }
        QPushButton:disabled {
            background-color: #505050;
            color: #808080;
        }
        QSlider::groove:horizontal {
            height: 7px;
            background: #404040;
            border-radius: 4px;
        }
        QSlider::handle:horizontal {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                        stop:0 #0d9aff, stop:1 #006db3);
            width: 18px;
            margin: -6px 0;
            border-radius: 9px;
            border: 1px solid #006db3;
        }
        QSlider::handle:horizontal:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                        stop:0 #1cb3ff, stop:1 #0080d9);
            border: 1px solid #0080d9;
        }
        QComboBox {
            border: 2px solid #404040;
            border-radius: 8px;
            padding: 6px 12px;
            background: #2a2a2a;
            color: #e0e0e0;
            font-weight: 500;
            min-height: 28px;
        }
        QComboBox:hover {
            border: 2px solid #0d9aff;
            background: #333333;
        }
        QComboBox:focus {
            border: 2px solid #0d9aff;
        }
        QComboBox::drop-down {
            border: none;
            background: transparent;
        }
        QComboBox QAbstractItemView {
            border: 2px solid #404040;
            border-radius: 6px;
            background-color: #2a2a2a;
            color: #e0e0e0;
            selection-background-color: #0d9aff;
            selection-color: #000000;
            padding: 3px;
        }
        QLabel {
            color: #e0e0e0;
            font-weight: 500;
        }
        QStatusBar {
            background: #1a1a1a;
            color: #e0e0e0;
            border-top: 1px solid #404040;
        }
        QProgressBar {
            border: 2px solid #404040;
            border-radius: 6px;
            background-color: #303030;
            text-align: center;
            color: #e0e0e0;
        }
        QProgressBar::chunk {
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                             stop:0 #0d9aff, stop:1 #006db3);
            border-radius: 4px;
        }
    """,
    "cyberpunk": """
        QMainWindow {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                        stop:0 #0a0e27, stop:1 #050813);
        }
        QWidget {
            background-color: #0a0e27;
        }
        QTextEdit {
            background-color: #0d1b2a;
            color: #00ff00;
            font-family: 'Courier New', monospace;
            border: 2px solid #00ffff;
            border-radius: 10px;
            padding: 8px;
            selection-background-color: #ff00ff;
            selection-color: #00ff00;
        }
        QTextEdit:focus {
            border: 2px solid #ff00ff;
        }
        QPushButton {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                             stop:0 #00ffff, stop:1 #00ccaa);
            border: 2px solid #00ffff;
            border-radius: 8px;
            padding: 10px 18px;
            color: #000000;
            font-weight: bold;
            font-size: 11px;
            min-height: 32px;
            outline: none;
        }
        QPushButton:hover {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                             stop:0 #ff00ff, stop:1 #dd00ff);
            border: 2px solid #ff00ff;
            color: #00ff00;
        }
        QPushButton:pressed {
            background-color: #aa00cc;
            border: 2px solid #ffff00;
            color: #000000;
        }
        QPushButton:disabled {
            background-color: #333355;
            color: #666688;
            border: 2px solid #444466;
        }
        QSlider::groove:horizontal {
            height: 7px;
            background: #00ffff;
            border-radius: 4px;
            opacity: 50;
        }
        QSlider::handle:horizontal {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                        stop:0 #ff00ff, stop:1 #00ffff);
            width: 18px;
            margin: -6px 0;
            border-radius: 9px;
            border: 2px solid #ff00ff;
        }
        QSlider::handle:horizontal:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                        stop:0 #ff00ff, stop:1 #ffff00);
            border: 2px solid #ffff00;
        }
        QComboBox {
            border: 2px solid #00ffff;
            border-radius: 8px;
            padding: 6px 12px;
            background: #0d1b2a;
            color: #00ff00;
            font-weight: 500;
            min-height: 28px;
        }
        QComboBox:hover {
            border: 2px solid #ff00ff;
            color: #ff00ff;
            background: #1a2a3a;
        }
        QComboBox:focus {
            border: 2px solid #ffff00;
        }
        QComboBox::drop-down {
            border: none;
            background: transparent;
        }
        QComboBox QAbstractItemView {
            border: 2px solid #00ffff;
            border-radius: 6px;
            background-color: #0d1b2a;
            color: #00ff00;
            selection-background-color: #ff00ff;
            selection-color: #00ff00;
            padding: 3px;
        }
        QLabel {
            color: #00ff00;
            font-weight: 500;
        }
        QStatusBar {
            background: #050813;
            color: #00ffff;
            border-top: 2px solid #00ffff;
        }
        QProgressBar {
            border: 2px solid #00ffff;
            border-radius: 6px;
            background-color: #0d1b2a;
            text-align: center;
            color: #00ff00;
        }
        QProgressBar::chunk {
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                             stop:0 #ff00ff, stop:1 #00ffff);
            border-radius: 4px;
        }
    """
}

class WorkerThread(QThread):
    finished = Signal(str)
    error = Signal(str)
    progress = Signal(int, int)

    def __init__(self, image_array, char_set, density, brightness, contrast, width=None):
        super().__init__()
        self.image_array = image_array
        self.char_set = char_set
        self.density = density
        self.brightness = brightness
        self.contrast = contrast
        self.width = width

    def run(self):
        try:
            gray = self.image_array
            if self.width is not None:
                gray = image_process.resize_for_ascii(gray, width=self.width)

            def progress_callback(row, total):
                self.progress.emit(row, total)

            ascii_text = ascii_process.map_to_ascii(gray, self.char_set, self.density, progress_callback)
            self.finished.emit(ascii_text)
        except Exception as e:
            self.error.emit(str(e))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cypher Image to ASCII")
        self.setMinimumSize(900, 700)

        self.current_image = None
        self.current_gray = None
        self.current_ascii = ""
        self.worker = None

        self.setup_ui()
        self.setup_connections()
        self.apply_theme("dark")
        self.setAcceptDrops(True)

    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setSpacing(12)
        main_layout.setContentsMargins(16, 16, 16, 16)

        # Top bar with buttons (with solid background)
        top_bar_widget = QWidget()
        top_bar_widget.setStyleSheet("background-color: rgba(0, 0, 0, 10%); border-radius: 10px;")
        top_bar = QHBoxLayout(top_bar_widget)
        top_bar.setSpacing(10)
        top_bar.setContentsMargins(16, 10, 16, 10)
        
        self.btn_load = QPushButton("  Load Image")
        self.btn_load.setIcon(qta.icon('fa5s.folder-open', color='white'))
        self.btn_load.setIconSize(QSize(16, 16))
        self.btn_load.setCursor(Qt.PointingHandCursor)
        top_bar.addWidget(self.btn_load)

        self.btn_export = QPushButton("  Export ASCII")
        self.btn_export.setIcon(qta.icon('fa5s.download', color='white'))
        self.btn_export.setIconSize(QSize(16, 16))
        self.btn_export.setEnabled(False)
        self.btn_export.setCursor(Qt.PointingHandCursor)
        top_bar.addWidget(self.btn_export)

        self.btn_copy = QPushButton("  Copy to Clipboard")
        self.btn_copy.setIcon(qta.icon('fa5s.copy', color='white'))
        self.btn_copy.setIconSize(QSize(16, 16))
        self.btn_copy.setEnabled(False)
        self.btn_copy.setCursor(Qt.PointingHandCursor)
        top_bar.addWidget(self.btn_copy)

        top_bar.addStretch()

        # Theme selector
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["light", "dark", "cyberpunk"])
        self.theme_combo.setFixedWidth(100)
        theme_label = QLabel("🎨")
        top_bar.addWidget(theme_label)
        top_bar.addWidget(self.theme_combo)

        main_layout.addWidget(top_bar_widget)

        # Splitter for main content
        splitter = QSplitter(Qt.Horizontal)
        splitter.setHandleWidth(6)
        splitter.setStyleSheet("""
            QSplitter::handle {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                           stop:0 transparent, stop:0.5 #0d9aff, stop:1 transparent);
                border-radius: 3px;
                margin: 2px 0;
            }
            QSplitter::handle:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                           stop:0 transparent, stop:0.5 #ff00ff, stop:1 transparent);
            }
        """)

        # Image preview panel
        preview_widget = QWidget()
        preview_widget.setStyleSheet("background-color: rgba(0, 0, 0, 5%); border-radius: 10px;")
        preview_layout = QVBoxLayout(preview_widget)
        preview_layout.setSpacing(10)
        preview_layout.setContentsMargins(12, 12, 12, 12)
        
        preview_title = QLabel("📷 Image Preview")
        preview_title.setStyleSheet("font-weight: bold; font-size: 12px;")
        preview_layout.addWidget(preview_title)

        self.image_preview = QLabel()
        self.image_preview.setAlignment(Qt.AlignCenter)
        self.image_preview.setMinimumSize(300, 300)
        self.image_preview.setScaledContents(False)
        preview_layout.addWidget(self.image_preview)
        splitter.addWidget(preview_widget)

        # ASCII preview panel
        ascii_widget = QWidget()
        ascii_widget.setStyleSheet("background-color: rgba(0, 0, 0, 5%); border-radius: 10px;")
        ascii_layout = QVBoxLayout(ascii_widget)
        ascii_layout.setSpacing(10)
        ascii_layout.setContentsMargins(12, 12, 12, 12)
        
        ascii_title = QLabel("✨ ASCII Art Output")
        ascii_title.setStyleSheet("font-weight: bold; font-size: 12px;")
        ascii_layout.addWidget(ascii_title)

        self.ascii_preview = QTextEdit()
        self.ascii_preview.setFont(QFont("Courier New", 10))
        self.ascii_preview.setReadOnly(True)
        self.ascii_preview.setLineWrapMode(QTextEdit.NoWrap)
        ascii_layout.addWidget(self.ascii_preview)
        splitter.addWidget(ascii_widget)

        splitter.setSizes([400, 500])
        main_layout.addWidget(splitter)

        # Control panel
        control_panel_widget = QWidget()
        control_panel_widget.setStyleSheet("background-color: rgba(0, 0, 0, 10%); border-radius: 10px;")
        control_panel = QHBoxLayout(control_panel_widget)
        control_panel.setSpacing(15)
        control_panel.setContentsMargins(16, 12, 16, 12)

        # Character set selector
        control_panel.addWidget(QLabel("📝 Charset:"))
        self.char_set_combo = QComboBox()
        self.char_set_combo.addItems(list(ascii_process.CHAR_SETS.keys()))
        self.char_set_combo.setMinimumWidth(80)
        control_panel.addWidget(self.char_set_combo)

        # Density slider
        control_panel.addWidget(QLabel("🎨 Density:"))
        self.density_slider = QSlider(Qt.Horizontal)
        self.density_slider.setRange(10, 100)
        self.density_slider.setValue(100)
        self.density_slider.setFixedWidth(120)
        control_panel.addWidget(self.density_slider)
        self.density_label = QLabel("1.00")
        self.density_label.setFixedWidth(40)
        control_panel.addWidget(self.density_label)

        # Width slider
        control_panel.addWidget(QLabel("📏 Width:"))
        self.width_slider = QSlider(Qt.Horizontal)
        self.width_slider.setRange(40, 200)
        self.width_slider.setValue(80)
        self.width_slider.setFixedWidth(120)
        control_panel.addWidget(self.width_slider)
        self.width_label = QLabel("80")
        self.width_label.setFixedWidth(40)
        control_panel.addWidget(self.width_label)

        # Brightness slider
        control_panel.addWidget(QLabel("☀️ Bright:"))
        self.brightness_slider = QSlider(Qt.Horizontal)
        self.brightness_slider.setRange(0, 200)
        self.brightness_slider.setValue(100)
        self.brightness_slider.setFixedWidth(120)
        control_panel.addWidget(self.brightness_slider)
        self.brightness_label = QLabel("1.00")
        self.brightness_label.setFixedWidth(40)
        control_panel.addWidget(self.brightness_label)

        # Contrast slider
        control_panel.addWidget(QLabel("🔲 Contrast:"))
        self.contrast_slider = QSlider(Qt.Horizontal)
        self.contrast_slider.setRange(0, 200)
        self.contrast_slider.setValue(100)
        self.contrast_slider.setFixedWidth(120)
        control_panel.addWidget(self.contrast_slider)
        self.contrast_label = QLabel("1.00")
        self.contrast_label.setFixedWidth(40)
        control_panel.addWidget(self.contrast_label)

        control_panel.addStretch()
        main_layout.addWidget(control_panel_widget)

        # Status bar with progress
        self.statusBar = QStatusBar()
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setFixedWidth(200)
        self.statusBar.addPermanentWidget(self.progress_bar)
        self.setStatusBar(self.statusBar)

        # Update icons after all widgets are created
        self.update_icons()

        # Animate buttons
        for btn in [self.btn_load, self.btn_export, self.btn_copy]:
            self.animate_button(btn)

    def update_icons(self):
        """Update button icons based on current theme."""
        theme = self.theme_combo.currentText()
        if theme == "light":
            color = '#1a1a1a'
        elif theme == "cyberpunk":
            color = '#00ff00'
        else:  # dark
            color = '#ffffff'
        
        self.btn_load.setIcon(qta.icon('fa5s.folder-open', color=color))
        self.btn_export.setIcon(qta.icon('fa5s.download', color=color))
        self.btn_copy.setIcon(qta.icon('fa5s.copy', color=color))

    def animate_button(self, button):
        """Add smooth hover animation to a button using color changes and effects."""
        original_style = button.styleSheet()
        
        class ButtonAnimator:
            def __init__(self, btn):
                self.button = btn
                self.hover_animation = QPropertyAnimation(btn, b"styleSheet")
                self.unhover_animation = QPropertyAnimation(btn, b"styleSheet")
                
            def on_enter(self, event):
                """Handle mouse enter with smooth color transition."""
                self.button.setGraphicsEffect(None)
                self.button.setCursor(Qt.PointingHandCursor)
                # Just update cursor, style already handles hover
                
            def on_leave(self, event):
                """Handle mouse leave."""
                self.button.setCursor(Qt.PointingHandCursor)
                
        animator = ButtonAnimator(button)
        button.enterEvent = animator.on_enter
        button.leaveEvent = animator.on_leave

    def setup_connections(self):
        self.btn_load.clicked.connect(self.load_image)
        self.btn_export.clicked.connect(self.export_ascii)
        self.btn_copy.clicked.connect(self.copy_ascii)
        self.theme_combo.currentTextChanged.connect(self.apply_theme)

        self.density_slider.valueChanged.connect(self.update_density_label)
        self.brightness_slider.valueChanged.connect(self.update_brightness_label)
        self.contrast_slider.valueChanged.connect(self.update_contrast_label)
        self.width_slider.valueChanged.connect(self.update_width_label)

        self.char_set_combo.currentTextChanged.connect(self.queue_conversion)
        self.density_slider.valueChanged.connect(self.queue_conversion)
        self.brightness_slider.valueChanged.connect(self.queue_conversion)
        self.contrast_slider.valueChanged.connect(self.queue_conversion)
        self.width_slider.valueChanged.connect(self.queue_conversion)

    def update_density_label(self, value):
        self.density_label.setText(f"{value/100:.2f}")

    def update_brightness_label(self, value):
        self.brightness_label.setText(f"{value/100:.2f}")

    def update_contrast_label(self, value):
        self.contrast_label.setText(f"{value/100:.2f}")

    def update_width_label(self, value):
        self.width_label.setText(str(value))

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "",
            "Images (*.png *.jpg *.jpeg *.webp);;All Files (*)"
        )
        if file_path:
            self.process_image(file_path)

    def process_image(self, file_path):
        try:
            self.current_image = image_process.load_image(file_path, max_size=(800, 800))
            self.current_gray = image_process.preprocess_image(self.current_image, brightness=1.0, contrast=1.0)

            pixmap = QPixmap(file_path)
            scaled = pixmap.scaled(self.image_preview.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_preview.setPixmap(scaled)

            self.statusBar.showMessage(f"Loaded: {file_path} | Size: {self.current_gray.shape}")

            self.btn_export.setEnabled(True)
            self.btn_copy.setEnabled(True)

            self.queue_conversion()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load image:\n{e}")
            self.statusBar.showMessage("Error loading image")

    def queue_conversion(self):
        if self.current_gray is None:
            return

        if self.worker is not None and self.worker.isRunning():
            self.worker.terminate()
            self.worker.wait()

        char_set_name = self.char_set_combo.currentText()
        char_set = ascii_process.get_char_set(char_set_name)
        density = self.density_slider.value() / 100.0
        brightness = self.brightness_slider.value() / 100.0
        contrast = self.contrast_slider.value() / 100.0
        width = self.width_slider.value()

        self.worker = WorkerThread(self.current_gray, char_set, density, brightness, contrast, width)
        self.worker.finished.connect(self.on_conversion_finished)
        self.worker.error.connect(self.on_conversion_error)
        self.worker.progress.connect(self.update_progress)
        self.worker.start()

        self.statusBar.showMessage("Converting...")
        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, 0)  # indeterminate until we know total rows

    def update_progress(self, current, total):
        if total > 0:
            self.progress_bar.setRange(0, total)
            self.progress_bar.setValue(current)
            self.progress_bar.setFormat(f"Row {current}/{total}")

    def on_conversion_finished(self, ascii_text):
        self.current_ascii = ascii_text
        self.ascii_preview.setPlainText(ascii_text)
        self.statusBar.showMessage(f"Conversion done. {len(ascii_text.splitlines())} lines.")
        self.progress_bar.setVisible(False)
        self.worker = None

    def on_conversion_error(self, error_msg):
        QMessageBox.warning(self, "Conversion Error", error_msg)
        self.statusBar.showMessage("Conversion failed")
        self.progress_bar.setVisible(False)
        self.worker = None

    def export_ascii(self):
        if not self.current_ascii:
            return
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save ASCII Art", "",
            "Text Files (*.txt);;All Files (*)"
        )
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.current_ascii)
                self.statusBar.showMessage(f"Saved to {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Save Error", f"Could not save file:\n{e}")

    def copy_ascii(self):
        if self.current_ascii:
            clipboard = QApplication.clipboard()
            clipboard.setText(self.current_ascii)
            self.statusBar.showMessage("Copied to clipboard")

    def apply_theme(self, theme_name):
        """Apply selected theme with proper styling."""
        self.setStyleSheet(STYLES.get(theme_name, STYLES["dark"]))
        self.update_icons()  # Refresh icons with new theme colors
        
        # Update image preview border color and background
        if theme_name == "light":
            border_color = "#d4d9e0"
            bg_color = "#ffffff"
        elif theme_name == "cyberpunk":
            border_color = "#00ffff"
            bg_color = "#0d1b2a"
        else:  # dark
            border_color = "#404040"
            bg_color = "#2a2a2a"
        
        self.image_preview.setStyleSheet(f"""
            QLabel {{
                border: 2px solid {border_color};
                border-radius: 10px;
                background-color: {bg_color};
                padding: 5px;
            }}
        """)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            self.process_image(file_path)