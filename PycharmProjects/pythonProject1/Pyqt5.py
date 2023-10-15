import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.qtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QtWidget


class MainWindow(QMainWindow):
    count = 0

    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.mdi = QMddiArea()
        self.setCentralWidget(self.mdi)

        self.bar = self.menuBar()
        file = self.bar.addmenu('File')
        file.addAction("New")
        file.addAction("cascade")
        file.addAction("Tiled")
        file.addAction("Exit")
        file.triggered[QAction].connect(self.windowtion)
        self.setWindowTitle("MDI demo")

    def windowaction(self,q):
        if q.text() == "New":
            MainWindow.count = MainWindow.count + 1


def main():
   app = QApplication(sys.argv)
   ex = MainWindow()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()