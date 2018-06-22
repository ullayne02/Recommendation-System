import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, Qt
from CollaborativeFiltering import CollaborativeFiltering
from ContentFiltering import ContentFiltering
import readDataframe

class Window(QTabWidget):
    def __init__(self):
        super(Window,self).__init__()
        animes = readDataframe.Animes()
        self.itemBased = WindowFiltering(CollaborativeFiltering(animes.animes,animes.rating))
        self.contentBased = WindowFiltering(ContentFiltering(animes.animes))
        self.addTab(self.itemBased,"Pessoas tambem assistiram")
        self.addTab(self.contentBased,"Porque voce assistiu")


class WindowFiltering(QWidget):
    def __init__(self,filter):
        super(WindowFiltering, self).__init__()
        self.k=10
        animes = readDataframe.Animes()
        self.f = filter

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
        anime_list = self.f.top_animes(self.k, item.text())
        for i in anime_list:
            self.listWidget2.addItem(i)



if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = Window()
    login = Login()
    signup = Signup()
    login.open_logged.connect(lambda: window.show())
    login.open_signup.connec(lambda: signup.show())
    window.open_login.connect(lambda: login.show())

    sys.exit(app.exec_())
    login.setWindowTitle('Anime Recommendation')
    login.setGeometry(500, 300, 300, 400)
    login.show()
    sys.exit(app.exec_())
