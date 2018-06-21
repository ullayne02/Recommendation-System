import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, Qt
from CollaborativeFiltering import CollaborativeFiltering
import readDataframe


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.k=10
        animes = readDataframe.Animes()
        self.cf = CollaborativeFiltering(animes.animes,animes.rating)

        self.listWidget = QListWidget()
        self.listWidget.resize(300,120)

        self.listWidget2 = QListWidget()
        self.listWidget2.resize(300,120)

        for i in animes.get_k_animes(50):
            self.listWidget.addItem(str(i))


        self.listWidget.itemClicked.connect(self.Clicked)

        layout = QHBoxLayout(self)
        layout.addWidget(self.listWidget)
        layout.addWidget(self.listWidget2)

    def Clicked(self,item):
        self.listWidget2.clear()
        anime_list = self.cf.top_animes(self.k, item.text())
        for i in anime_list:
            self.listWidget2.addItem(i)

    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.setWindowTitle('Anime Recommendation')
    window.setGeometry(500, 300, 300, 400)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
