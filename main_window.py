import os
import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from main import FilePathIterator


class DatasetViewer(QMainWindow):
    def __init__(self):
        """Конструктор класса."""
        super().__init__()
        self.setWindowTitle("Просмотр датасета.")
        self.resize(500, 500)
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.image_display = QLabel("Изображение отсуствует.")
        self.image_display.setAlignment(Qt.AlignCenter)
        self.btn_next_image = QPushButton("Следующие изображение.")
        self.btn_next_image.setEnabled(False)
        self.btn_open_folder = QPushButton("Выберите папку с фотками.")
        self.btn_next_image.clicked.connect(self.show_next_image)
        self.btn_open_folder.clicked.connect(self.open_dataset_folder)
        main_layout.addWidget(self.btn_open_folder)
        main_layout.addWidget(self.image_display)
        main_layout.addWidget(self.btn_next_image)
        self.file_iterator = None
        self.current_file = None

    def open_dataset_folder(self):
        """Получение image из папки датасета."""
        try:
            folder_path = QFileDialog.getExistingDirectory(
                self, "Выберите папку с датасетом."
            )
            if not folder_path:
                return

            script_dir = os.path.dirname(os.path.abspath(__file__))
            self.file_iterator = FilePathIterator(folder_path, script_dir)

            self.file_iterator.index = 0
            self.current_file = next(self.file_iterator)
            self.display_image(self.current_file)
            self.btn_next_image.setEnabled(True)
        except StopIteration:
            self.btn_next_image.setEnabled(False)
        except Exception as ex:
            print(f"Ошибка: {ex}")

    def display_image(self, file_path: str):
        """Отображение фоток."""
        pixmap = QPixmap(file_path)
        scaled_pixmap = pixmap.scaled(
            500,
            500,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.image_display.setPixmap(scaled_pixmap)
        self.image_display.setText("")

    def show_next_image(self):
        """Переход к следующему фото."""
        if self.file_iterator is None:
            return
        try:
            self.current_file = next(self.file_iterator)
            self.display_image(self.current_file)
        except StopIteration:
            self.btn_next_image.setEnabled(False)


def main():
    try:
        app = QApplication(sys.argv)
        viewer = DatasetViewer()
        viewer.show()
        sys.exit(app.exec())
    except Exception as ex:
        print("Ошибка: ", ex)


if __name__ == "__main__":
    main()
