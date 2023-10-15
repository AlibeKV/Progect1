try:
    import sys
    import typing
    from Pyqt5 import QtCore
    from Pyqt5.QtGui import *
    from Pyqt5.Qtcore import *
    from Pyqt5.QtWidjets import *
except ModuleNotFoundError:
    print('Не найдеен модуль')


class Window(QWidget):
    def __init__(self,parent=None):
        super(Window.self).__init__(parent)
        self.resize(640,480)
        self.setWindowTitle('First application')
        self.label = Qtlabel(self
        self.label.setText("Hello World")
        font = QFont()
        font.setFamily("Roboto")
        font.ssetPointSize(32)
        self.label.setFont(font)
        self.label.move(50,20)

def main():
    app = Qaapplication(sys.argv)
    execution = Window
    execution.show()
    sys.exit(app.exec_())