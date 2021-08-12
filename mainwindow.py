# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets,QtGui,QtCore
from secondwindow import SecondWindow

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.mainwindow()
    def mainwindow(self):
        #Anasayfa yapısı
        self.second_window=QtWidgets.QStackedWidget()
        self.setStyleSheet("background: white;")
        self.setWindowTitle("Kerim Yildizoglu Tez")
        self.setWindowIcon(QtGui.QIcon('iimages/logo.jpg'))
        self.setMinimumSize(1200,900)
        self.setMaximumSize(1200,900)
        
        #logo
        self.logo=QtWidgets.QLabel(self)
        self.logo.setPixmap(QtGui.QPixmap("iimages/logo.jpg"))
        self.logo.setScaledContents(True)
        self.logo.resize(200,200)
        self.logo.move(500,0)
        
        #tez konusu
        self.tez_konusu=QtWidgets.QLabel(self)
        self.tez_konusu.setText("TEZ KONUSU: \nDERİN ÖĞRENME TABANLI BİLGİSAYARLI GÖRÜŞ \nİLE\nYÜZ TANIMA İLE DUYGU VE CİNSİYET TAHMİNİ")
        self.tez_konusu.setFont(QtGui.QFont("MS Shell Dlg 2", 25))
        self.tez_konusu.setAlignment(QtCore.Qt.AlignCenter)
        self.tez_konusu.resize(750,191)
        self.tez_konusu.move(230,200)
        
        #Programa geçiş butonu
        self.prog_gecis_buton=QtWidgets.QPushButton(self)
        self.prog_gecis_buton.setText("YÜZ TANIMLAMAYA\nBAŞLA")
        self.prog_gecis_buton.setStyleSheet("background-color:#c39435;color:#ffffff;border-radius:20px;border-style: solid;")
        self.prog_gecis_buton.setFont(QtGui.QFont("MS Shell Dlg 2", 12,QtGui.QFont.Bold))
        self.prog_gecis_buton.resize(191,120)
        self.prog_gecis_buton.move(510,400)
       
       
        
        self.prog_gecis_buton.clicked.connect(self.openWindow)
        
    def openWindow(self):
        self.hide()
        self.second=SecondWindow()
        self.second.show()
        
def main():
    app=QtWidgets.QApplication(sys.argv)
    main=MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
