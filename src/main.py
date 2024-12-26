import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont
from PIL import Image

class ImageToPdfApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image to PDF Converter")
        self.setGeometry(300, 300, 600, 400)

        layout = QVBoxLayout()

        self.label = QLabel("Select an image to convert to PDF", self)
        self.label.setAlignment(Qt.AlignCenter)

        self.select_button = QPushButton("Select Image", self)
        self.convert_button = QPushButton("Convert to PDF", self)
        self.convert_button.setEnabled(False)

        layout.addWidget(self.label)
        layout.addWidget(self.select_button)
        layout.addWidget(self.convert_button)

        self.setLayout(layout)

        self.select_button.clicked.connect(self.select_image)
        self.convert_button.clicked.connect(self.convert_to_pdf)

        self.image_path = None

        self.setStyleSheet("""
            QWidget {
                background-color: #F0F8FF;
            }
            QPushButton {
                background-color: #66CDAA;
                border-radius: 5px;
                padding: 10px;
                color: white;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #20B2AA;
            }
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #4682B4;
            }
        """)

    def resizeEvent(self, event):
        size = self.size()
        font_size = int(size.width() * 0.05)
        self.label.setFont(QFont("Arial", font_size))
        self.select_button.setFont(QFont("Arial", font_size))
        self.convert_button.setFont(QFont("Arial", font_size))
        super().resizeEvent(event)

    def select_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.xpm *.jpg *.bmp)", options=options)

        if file_path:
            self.image_path = file_path
            self.label.setText(f"Selected: {file_path}")
            self.convert_button.setEnabled(True)

    def convert_to_pdf(self):
        if self.image_path:
            try:
                image = Image.open(self.image_path)
                save_path, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf)")
                
                if save_path:
                    image.save(save_path, "PDF")
                    self.label.setText(f"PDF saved successfully: {save_path}")
                else:
                    self.label.setText("Save operation cancelled.")
                
            except Exception as e:
                self.label.setText(f"Error: {str(e)}")
        else:
            self.label.setText("No image selected!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageToPdfApp()
    window.show()
    sys.exit(app.exec_())
