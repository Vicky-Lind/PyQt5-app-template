import sys 
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Template')
        #self.setWindowIcon(QIcon('./assets/Template.png'))
        self.setGeometry(100, 100, 500, 300)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    appWindow = MainWindow()
    appWindow.show()
    sys.exit(app.exec())