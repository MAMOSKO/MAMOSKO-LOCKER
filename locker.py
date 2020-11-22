#-*-coding:utf-8-*-
from os import startfile,getenv
from sys import argv,exit as sysexit
import keys

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QWidget, QPushButton,QMainWindow,QAction,QFileDialog
try:
    class Pencere(QWidget):
        def __init__(self):
            super().__init__()

            self.init_ui()
        def init_ui(self):
            self.hata = QLineEdit()
            self.hata.setPlaceholderText("Hatalar Burada Gösterilecek")
            self.hata.setStyleSheet("QLineEdit"
                                    "{"
                                    "color:white;"
                                    "background-color:grey;"
                                    "border:none;"
                                    "}")

            self.yazı_alanı = QTextEdit()
            self.yazı_alanı.setPlaceholderText("Şifrelemek istediğiniz metni buraya girin...")
            self.yazı_alanı.setStyleSheet("QTextEdit"
                                          "{"
                                          "border:1px solid blue;"
                                          "color:white;"
                                          "background-color:grey;"
                                          "border-radius:10px;"
                                          "}")

            self.bgimage = QLabel(self)
            self.bgimage.setPixmap(QPixmap("bgimage.png"))
            self.bgimage.setGeometry(QRect(0, 0, 800, 400))
            self.bgimage.setScaledContents(True)
            self.şifrele = QPushButton("Şifrele")
            self.şifrele.setStyleSheet("QPushButton"
                                       "{"
                                       "color:white;"
                                       "background-color:grey;"
                                       "height:20px;"
                                       "border:1px solid blue;"
                                       "}"
                                       "QPushButton:hover"
                                       "{"
                                       "color:blue;"
                                       "}")
            self.şifreçöz = QPushButton("Şifreyi Çöz")
            self.şifreçöz.setStyleSheet("QPushButton"
                                       "{"
                                       "color:white;"
                                       "background-color:grey;"
                                       "height:20px;"
                                       "border:1px solid blue;"
                                       "}"
                                        "QPushButton:hover"
                                        "{"
                                        "color:blue;"
                                        "}"
                                        )
            self.yazı_alanı2 = QTextEdit()
            self.yazı_alanı2.setPlaceholderText("Şifresini çözmek istediğiniz metni buraya girin...")
            self.yazı_alanı2.setStyleSheet("QTextEdit"
                                          "{"
                                          "border:1px solid blue;"
                                          "color:white;"
                                          "background-color:grey;"
                                          "border-radius:10px;"
                                          "}")
            self.setGeometry(400, 100, 800, 400)

            self.setFixedSize(800, 400)
            self.bgimage.move(0, 0)
            v_box = QVBoxLayout()
            h_box = QHBoxLayout()
            h_box.addWidget(self.yazı_alanı)
            v_box.addWidget(self.şifrele)
            v_box.addWidget((self.hata))
            v_box.addWidget(self.şifreçöz)

            h_box.addLayout(v_box)

            h_box.addWidget(self.yazı_alanı2)
            self.setLayout(h_box)

            self.şifrele.clicked.connect(self.click)
            self.şifreçöz.clicked.connect(self.click)


        def click(self):

            sender = self.sender()
            y = self.yazı_alanı.toPlainText()
            y2 = self.yazı_alanı2.toPlainText()
            u = len(y)
            u2 = len(y2)
            s = 0
            ş = list()
            if sender.text() == "Şifrele":
                while s != u:
                    try:
                        ş.append(keys.şifres[y[s]])
                    except NameError:
                        ş = list()
                        self.hata.setText("Anahtarlar dahil edilmemiş!")
                        break
                    except:
                        ş = list()
                        self.hata.setText("Şifrelenemeyen bir Sembol Kullandınız    {" + y[s] + "}")
                        break
                    s += 1
                şifre1 = ""

                if len(ş) == 0:
                    pass
                else:
                    self.hata.clear()
                for i in ş:
                    şifre1 = şifre1 + i

                if len(ş) != 0:
                    self.yazı_alanı2.setText(şifre1)
                    self.yazı_alanı.clear()


            elif sender.text() == "Şifreyi Çöz":
                while s != u2:
                    try:
                        ş.append(keys.şifreç[y2[s]])

                    except:
                        ş = list()
                        self.hata.setText("Yanlış Şifre    {" + y2[s] + "}")
                        break
                    s += 1

                    if len(ş) == 0:
                        pass
                    else:
                        self.hata.clear()
                şifre1 = ""
                for i in ş:
                    şifre1 = şifre1 + i

                if len(ş) != 0:
                    self.yazı_alanı.setText(şifre1)
                    self.yazı_alanı2.clear()
    class Menu(QMainWindow):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("MAMOSKO LOCKER")
            self.pencere=Pencere()
            self.setFixedSize(800, 421)
            self.setCentralWidget(self.pencere)
            self.menu()
        def menu(self):
            menu=self.menuBar()
            dosya=menu.addMenu("Dosya")
            kaydet=menu.addMenu("Kaydet")
            dosya_şifrele=QAction("Dosyadan Şifrele",self)
            dosya_şifreçöz=QAction("Dosyadan Şifre Çöz",self)
            kaydet_yazı=QAction("Metni Kaydet",self)
            kaydet_şifre=QAction("Şifreyi Kaydet",self)
            dosya_şifrele.setShortcut("Ctrl+o")
            dosya_şifreçöz.setShortcut("Ctrl+e")
            kaydet_yazı.setShortcut("Ctrl+s")
            kaydet_şifre.setShortcut("Ctrl+shift+s")
            dosya.addAction(dosya_şifrele)
            dosya.addAction(dosya_şifreçöz)
            kaydet.addAction(kaydet_yazı)
            kaydet.addAction(kaydet_şifre)

            dosya.triggered.connect(self.dosyaf)
            kaydet.triggered.connect(self.dosyak)

            self.show()
        def dosyaf(self,action):
            if action.text()=="Dosyadan Şifrele":
                self.dosyaad=QFileDialog.getOpenFileName(self,"Dosya Aç",getenv("Desktop"))
                try:
                    dosya=open(self.dosyaad[0],encoding="UTF-8")
                    oku=dosya.read()
                    dosya.close()
                    self.pencere.yazı_alanı.setText(oku)
                    self.pencere.hata.clear()
                except:
                    self.pencere.hata.setText("Dosya Açılırken Hata Oluştu")

            else:
                self.dosyaad = QFileDialog.getOpenFileName(self, "Dosya Aç", getenv("Desktop"))
                try:
                    dosya = open(self.dosyaad[0],encoding="UTF-8")
                    oku = dosya.read()
                    dosya.close()
                    self.pencere.yazı_alanı2.setText(oku)
                    self.pencere.hata.clear()
                except:
                    self.pencere.hata.setText("Dosya Açılırken Hata Oluştu")
        def dosyak(self,action):
            if action.text()=="Metni Kaydet":
                try:
                    dosyaad = QFileDialog.getSaveFileName(self, "Dosyayı Kaydet", getenv("Desktop"))

                    if dosyaad[0]=='':
                        self.pencere.hata.setText("Lütfen Geçerli Bir Konum Seçin")
                    else:
                        file=open(dosyaad[0],"w",encoding="UTF-8")
                        file.write(self.pencere.yazı_alanı.toPlainText())
                        file.close()
                        self.pencere.hata.clear()
                except:
                    self.pencere.hata.setText("Dosya Kaydedilemedi")
            else:
                try:
                    dosyaad = QFileDialog.getSaveFileName(self, "Dosyayı Kaydet", getenv("Desktop"))
                    if dosyaad[0]=='':
                        self.pencere.hata.setText("Lütfen Geçerli Bir Konum Seçin")
                    else:
                        file=open(dosyaad[0],"w",encoding="UTF-8")
                        file.write(self.pencere.yazı_alanı2.toPlainText())
                        file.close()
                        self.pencere.hata.clear()
                except:
                    self.pencere.hata.setText("Dosya Kaydedilemedi")
    try:
        file = open("licance", "r")
        l = file.read()
        file.close()
        if l == "Licance.514":
            ooo = 1
            app = QApplication(argv)
            pencere = Menu()
            sysexit(app.exec_())
        else:
            startfile("key.py")
            exit()
    except FileNotFoundError:
        startfile("key.py")
        exit()
except:
    pass