import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *
from functools import partial
from random import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtMultimedia import *


class Fenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.is_initialized = False
        self.grid = QGridLayout()
        names = [str(i) for i in range(100)]
        posi = [(i, j) for i in range(10) for j in range(10)]
        self.minedict = {}
        for name in names:
            self.minedict[str(name)] = 0
        missing_mines = 10
        while missing_mines > 0:
            k = randint(0, 99)
            if self.minedict[str(k)] == 0:
                self.minedict[str(k)] = 1
                missing_mines -= 1
        self.bombdict = {}
        for name in names:
            self.bombdict[str(name)] = 0
        for i in range(0, 100):
            if i != 99:
                if self.minedict[str(i+1)] == 1:
                    if not (i-9) % 10 == 0:
                        self.bombdict[str(i)] += 1
            if i != 0:
                if self.minedict[str(i-1)] == 1:
                    if not i % 10 == 0:
                        self.bombdict[str(i)] += 1
            if i > 10:
                if self.minedict[str(i-11)] == 1:
                    if not i % 10 == 0:
                        self.bombdict[str(i)] += 1
            if i < 89:
                if self.minedict[str(i+11)] == 1:
                    if not (i-9) % 10 == 0:
                        self.bombdict[str(i)] += 1
            if i >= 9:
                if self.minedict[str(i - 9)] == 1:
                    if not (i-9) % 10 == 0:
                        self.bombdict[str(i)] += 1
            if i < 91:
                if self.minedict[str(i+9)] == 1:
                    if not i % 10 == 0:
                        self.bombdict[str(i)] += 1
            if i >= 10:
                if self.minedict[str(i - 10)] == 1:
                    self.bombdict[str(i)] += 1
            if i < 90:
                if self.minedict[str(i+10)] == 1:
                    self.bombdict[str(i)] += 1
            
        for pos, name in zip(posi, names):
            button = QPushButton(" ")
            button.setToolTip(name)
            button.setCheckable(True)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            button.clicked.connect(partial(self.checkd, name))
            self.grid.addWidget(button, *pos)
        self.grid.setSpacing(0)
        self.setLayout(self.grid)
        self.setGeometry(300, 100, 300, 300)
        self.setWindowTitle("Catsweeper")
        self.setWindowIcon(QIcon("CrazyLeonie.jpg"))
        self.show()

    def show_all(self):
        names = [str(i) for i in range(100)]
        for name in names:
            self.grid.itemAt(int(name)).widget().setText(str(self.bombdict[str(name)]))
            self.grid.itemAt(int(name)).widget().setFont(QFont("Arial", 11))
            c = ["blue", "green", "red", "grey", "purple", "turquoise", "violet", "brown", "orange"]
            n = 1
            for i in c:
                if self.bombdict[str(name)] == n:
                    self.grid.itemAt(int(name)).widget().setStyleSheet("color: %s" % (i))
                n += 1
            if self.bombdict[str(name)] == 0:
                self.grid.itemAt(int(name)).widget().setText(" ")

    def checkd(self, name):
        if not self.is_initialized:
            self.is_initialized = True
        print(name)
        print(self.minedict)
        print(sum(self.minedict.values()))
        #print(self.minedict.values.sum())
        self.grid.itemAt(int(name)).widget().setEnabled(False)
        #self.grid.itemAt(int(name)).widget().setText(str(self.bombdict[str(name)]))
        if self.minedict[str(name)] != 1:
            self.grid.itemAt(int(name)).widget().setText(str(self.bombdict[str(name)]))
            self.grid.itemAt(int(name)).widget().setFont(QFont("Arial", 11))
            c = ["blue", "green", "red", "grey", "purple", "turquoise", "violet", "brown", "orange"]
            n = 1
            for i in c:
                if self.bombdict[str(name)] == n:
                    self.setStyleSheet("color: %s" % (i))
                n += 1
            if self.bombdict[str(name)] == 0:
                self.setText(" ")

        if self.minedict[str(name)] == 1:
            self.setEnabled(False)
            for i in range(100):
                if self.minedict[str(i)] == 1:
                    self.grid.itemAt(int(str(i))).widget().setIcon(QIcon("CrazyLeonie.jpg"))
            self.show_all()
           # msc = QUrl.fromLocalFile("./salamisound-6959369-katze-miaut-kurz-eher.mp3")
           # content = QMediaContent(msc)
           # player = QMediaPlayer()
           # player.setMedia(content)
           # player.setvolume(4)
           # player.play()

            print("You wasted an innocent cat!")


app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec_())