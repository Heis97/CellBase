#from socket import *
import socket
import sys
import time
import serial
import random
import json
from datetime import datetime,date,time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget,QTableWidget, QPushButton,QComboBox, QLineEdit,QTextEdit,
    QInputDialog, QApplication, QMainWindow, QGridLayout, QWidget, QTableWidgetItem)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QBrush, QColor, QPainter, QPen, QPolygon,QKeyEvent
from PyQt5.QtCore import (pyqtProperty, pyqtSignal, pyqtSlot, QPoint, QSize,
        Qt, QTime, QTimer)
namep=""
namec=""
named=0
nameg=0
namek=0
selk=[]
kletki=[[[[]]]]
a=[]
b=[]
c=[]


d=[]
for i3 in range(2):
    c=[]
    for i2 in range(4):
        b=[]
        for i1 in range(10):
            a=[]
            for i in range(81):
                a.append(['','','',''])           
            b.append(a)
        c.append(b)
    d.append(c)

file='base.json'
kletki=d
with open("base.json", "w", encoding="utf-8") as file:
    json.dump(kletki, file)
ppls=[]
cellsline=[]
d=str(datetime.now())
d1=d.split(' ')
d2=d1[0].split('-')
datas=str(d2[2])+'.'+str(d2[1])+'.'+str(d2[0])
for i in range(2):
    kletki.append([])
    for i1 in range(4):
        kletki[i].append([])
        for i2 in range(10):
            kletki[i][i1].append([])
            for i3 in range(81):
                kletki[i][i1][i2].append([res[i][i1][i2][i3][0],res[i][i1][i2][i3][1],res[i][i1][i2][i3][2],res[i][i1][i2][i3][3]])
                if ppls.count(res[i][i1][i2][i3][3])==0 and res[i][i1][i2][i3][3]!='':
                    ppls.append(res[i][i1][i2][i3][3])
                if cellsline.count(res[i][i1][i2][i3][0])==0 and res[i][i1][i2][i3][0]!='':
                    cellsline.append(res[i][i1][i2][i3][0])
class PassWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setWindowTitle("Kletki")
        self.resize(400, 300)
        self.Win2 = None
        self.build()
    def build(self):
        self.but1 = QtWidgets.QPushButton('Вход', self)
        self.but1.setGeometry(QtCore.QRect(130, 240, 120, 40))
        self.but1.clicked.connect(self.vhod)

        self.lin = QtWidgets.QLineEdit(self)
        self.lin.setGeometry(QtCore.QRect(170, 120, 160, 20))
        
        combo = QComboBox(self)
        combo.addItems(ppls)
        combo.move(170, 60)
        combo.activated[str].connect(self.fcombo)
        
    def vhod(self):
        if not self.Win2:
            self.Win2 = MainWindow(self)

        self.Win2.show()
    def fcombo(self,text):
        global namep
        namep=text
        self.lin.setText(text)
class CustomTableWidget(QTableWidget):
 
    # переопределяем keyPressEvent
    def keyPressEvent(self, e: QKeyEvent) -> None:
        if e.key() == Qt.Key_Enter:
            print("Key enter was pressed")
        elif e.key() == Qt.Key_Return:
            print("Key return was pressed")
class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setWindowTitle("Kletki")
        self.resize(1000, 700)
        self.Win2 = None
        self.build()
    def build(self):
        self.but1 = QtWidgets.QPushButton('Найти', self)
        self.but1.setGeometry(QtCore.QRect(400, 80, 120, 20))
        self.but1.clicked.connect(self.ffind)
        self.but2 = QtWidgets.QPushButton('Карта', self)
        self.but2.setGeometry(QtCore.QRect(560, 80, 120, 20))
        self.but2.clicked.connect(self.fmap)
        
        self.lin = QtWidgets.QLineEdit(self)
        self.lin.setGeometry(QtCore.QRect(100, 80, 260, 20))
        combo1 = QComboBox(self)
        combo1.addItems(cellsline)
        combo1.move(100, 28)
        combo1.activated[str].connect(self.fcombo)
        self.table = CustomTableWidget(self)
        self.table.setGeometry(QtCore.QRect(100, 140, 620, 400))
        self.table.setColumnCount(4)  
         
        # Установить заголовки таблицы
        self.table.setHorizontalHeaderLabels(["Пассаж", "Дата", "Человек","Расположение"])
 
        # Установить подсказки для заголовков
        self.table.horizontalHeaderItem(0).setToolTip("Пассаж")
        self.table.horizontalHeaderItem(1).setToolTip("Дата")
        self.table.horizontalHeaderItem(2).setToolTip("Человек")
        self.table.horizontalHeaderItem(3).setToolTip("Расположение")
 
        # Установите выравнивание к заголовкам
        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(3).setTextAlignment(Qt.AlignLeft)
        
        # заполните первую строку
        #table.setItem(0, 0, self.createItem("Text in column 1", Qt.ItemIsSelectable))
        #table.setItem(0, 1, self.createItem("Text in column 2", Qt.ItemIsSelectable))
        #table.setItem(0, 2, self.createItem("Text in column 3", Qt.ItemIsSelectable))
        #вычислить номера коробок с этой линией, вывести номера ячеек в этой коробке с этой линией
        
        self.table.setRowCount(0) 
        #for i in range(9):
            #table.setItem(0, 0, self.createItem("Text in column 1", Qt.ItemIsSelectable))
            
 
        # изменить размер столбца по содержимому
        self.table.resizeColumnsToContents()
        self.table.doubleClicked.connect(self.on_click)
        self.table.itemSelectionChanged.connect(self.activ)
        self.table.setSortingEnabled(True)
    def createItem(self, text, flags):
        tableWidgetItem = QTableWidgetItem(text)
        tableWidgetItem.setFlags(flags)
        return tableWidgetItem
    
    def ffind(self):
        self.fcombo(self.lin.text())
    def fmap(self):
        if not self.Win2:
            self.Win2 = MapWindow(self)
        self.Win2.show()
    def fcombo(self,text):
        global namec
        namec=text
        self.table.setRowCount(0)
        k=0
        k1=0
        listk=[]
        listk1=[]
        listk2=[]
        listk3=[]
        listk4=[]
        for i in range(2):
            for i1 in range(4):
                for i2 in range(10):
                    k=0
                    listk=[]
                    for i3 in range(81):
                        if kletki[i][i1][i2][i3][0].count(namec)>0:
                            k+=1
                            listk.append([i,i1,i2,i3])
                    if k!=0:    
                        k1+=1
                        listk1.append(listk)
                #if len(listk1)!=0:    
                    #listk1.append(listk)
        #print(str(listk1))
        
        #sort data-----------------------------------------------------------
        left=0
        right=len(listk1)-1
        while left <= right:
            
            for i in range(left, right, +1):
                datai=kletki[listk1[i][0][0]][listk1[i][0][1]][listk1[i][0][2]][listk1[i][0][3]][2]
                datai=datai.split('.')
                datais=int(datai[0])+(int(datai[1])-1)*30+int(datai[2])*360
                datai1=kletki[listk1[i+1][0][0]][listk1[i+1][0][1]][listk1[i+1][0][2]][listk1[i+1][0][3]][2]
                datai1=datai1.split('.')
                datai1s=int(datai1[0])+(int(datai1[1])-1)*30+int(datai1[2])*360
                if datais < datai1s:
                    listk1[i], listk1[i + 1] = listk1[i + 1], listk1[i]
            right -= 1

            for i in range(right, left, -1):
                datai=kletki[listk1[i][0][0]][listk1[i][0][1]][listk1[i][0][2]][listk1[i][0][3]][2]
                datai=datai.split('.')
                datais=int(datai[0])+(int(datai[1])-1)*30+int(datai[2])*360
                datai2=kletki[listk1[i-1][0][0]][listk1[i-1][0][1]][listk1[i-1][0][2]][listk1[i-1][0][3]][2]
                datai2=datai2.split('.')
                datai2s=int(datai2[0])+(int(datai2[1])-1)*30+int(datai2[2])*360
                if datai2s < datais:
                    listk1[i], listk1[i - 1] = listk1[i - 1], listk1[i]
            left += 1
            #end--------------------------------------------------------
       
        '''for i in range(1,len(listk1)):
            if kletki[listk3[-1][0][0]][listk3[-1][0][1]][listk3[-1][0][2]][listk3[-1][0][3]][1]<=kletki[listk1[i][0][0]][listk1[i][0][1]][listk1[i][0][2]][listk1[i][0][3]][1]:
                listk3.append(listk1[i])
                
            else:
                listk4=[listk1[i]]
                listk4.extend(listk3)
                listk3=listk4
        #[1,2].extend([3,4])
        listk1=listk3'''
        self.table.setRowCount(k1)
        for i in range(len(listk1)):
            yach=""
            for i1 in range(len(listk1[i])):
                selk.append(listk1[i][i1][3])
                yach+=" "+str(listk1[i][i1][3]+1)+","
            self.table.setItem(i, 0, self.createItem(kletki[listk1[i][0][0]][listk1[i][0][1]][listk1[i][0][2]][listk1[i][0][3]][1], Qt.ItemIsSelectable | Qt.ItemIsEnabled ))
            self.table.setItem(i, 1, self.createItem(kletki[listk1[i][0][0]][listk1[i][0][1]][listk1[i][0][2]][listk1[i][0][3]][2], Qt.ItemIsSelectable | Qt.ItemIsEnabled ))
            self.table.setItem(i, 2, self.createItem(kletki[listk1[i][0][0]][listk1[i][0][1]][listk1[i][0][2]][listk1[i][0][3]][3], Qt.ItemIsSelectable | Qt.ItemIsEnabled ))
            self.table.setItem(i, 3, self.createItem('Дюар '+str(listk1[i][0][0]+1)+',Гнездо '+str(listk1[i][0][1]+1)+',Коробка '+str(listk1[i][0][2]+1)+',Ячейки: '+yach, Qt.ItemIsSelectable | Qt.ItemIsEnabled ))
            self.listk1=listk1
            self.listk1[i][0].append(selk)
            #print(str(i))
                #table.setItem(i, 4, self.createItem("Text in column 1", Qt.ItemIsSelectable))
        
        self.table.resizeColumnsToContents()
    def on_click(self):
        for currentQTableWidgetItem in self.table.selectedItems():
            #print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
            global named
            named=self.listk1[currentQTableWidgetItem.row()][0][0]
            global nameg
            nameg=self.listk1[currentQTableWidgetItem.row()][0][1]
            global namek
            namek=self.listk1[currentQTableWidgetItem.row()][0][2]
        self.Win2=None
        self.Win2 = MapWindow(self)
        self.Win2.show()
    def activ(self):
        pass
        #for currentQTableWidgetItem in self.table.selectedItems():
            #for i in range(3):
                #self.table.item(currentQTableWidgetItem.row(),i).

class MapWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setWindowTitle("Kletki")
        self.resize(1000, 600)
        self.Win2 = None
        self.build()
    def build(self):
        dcomb = QComboBox(self)
        dcomb.addItems(['1','2'])
        dcomb.move(10, 10)
        dcomb.setCurrentIndex(named)
        dcomb.activated[str].connect(self.fdcomb)
        gcomb = QComboBox(self)
        gcomb.addItems(['1','2','3','4'])
        gcomb.move(40, 10)
        gcomb.activated[str].connect(self.fgcomb)
        gcomb.setCurrentIndex(nameg)

        kcomb = QComboBox(self)
        kcomb.addItems(['1','2','3','4','5','6','7','8','9','10'])
        kcomb.move(70, 10)
        kcomb.activated[str].connect(self.fkcomb)
        kcomb.setCurrentIndex(namek)
        self.bsel=[]
        
        self.but=[]
        self.select=[]
        for i in range(2):
            self.select.append([])
            for i1 in range(4):
                self.select[i].append([])
                for i2 in range(10):
                    self.select[i][i1].append([])
                    for i3 in range(81):
                        self.select[i][i1][i2].append(0)
                    
        #print(self.select)
        self.selected=[]
        for i in range (1,100):
            self.but+=[0]
            self.bsel+=[0]
        bsize=30
        a=[]
        b=[]
        c=[]
        for i in range(2):                
            self.selected.append([[[],[],[],[],[],[],[],[],[],[]],
                                  [[],[],[],[],[],[],[],[],[],[]],
                                  [[],[],[],[],[],[],[],[],[],[]],
                                  [[],[],[],[],[],[],[],[],[],[]]])
        
        i2=1
        for i in range (1,10):
            for i1 in range (1,10):
                self.but[i2] = QtWidgets.QPushButton(str(i2), self)
                self.but[i2].setGeometry(QtCore.QRect(30+i1*bsize, 30+i*bsize, bsize, bsize))
                self.but[i2].clicked.connect(self.pbut)
                i2+=1
        self.risov()
        for i in range (1,10):
            self.label = QtWidgets.QLabel(self)
            self.label.setGeometry(QtCore.QRect(43+i*bsize, 40, 20, 20))
            self.label.setText(str(i))

        for i in range (1,10):
            self.label = QtWidgets.QLabel(self)
            self.label.setGeometry(QtCore.QRect(43, 36+i*bsize, 20, 20))
            self.label.setText(str(i))
        self.but1 = QtWidgets.QPushButton('Редактировать', self)
        self.but1.setGeometry(QtCore.QRect(830, 240, 120, 40))
        self.but1.clicked.connect(self.fred)
        

        self.but2 = QtWidgets.QPushButton('Удалить', self)
        self.but2.setGeometry(QtCore.QRect(830, 280, 120, 40))
        self.but2.clicked.connect(self.fdel)


        self.label1 = QtWidgets.QLabel(self)
        self.label1.setGeometry(QtCore.QRect(430, 10, 330, 40))
        self.label1.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.label1.setText('')

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setGeometry(QtCore.QRect(430, 50, 330, 40))
        self.label2.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.label2.setText('')
        
        self.label3 = QtWidgets.QLabel(self)
        self.label3.setGeometry(QtCore.QRect(430, 90, 330, 40))
        self.label3.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.label3.setText('')

        self.label4 = QtWidgets.QLabel(self)
        self.label4.setGeometry(QtCore.QRect(430, 140, 330, 40))
        self.label4.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.label4.setText('')

        self.label5 = QtWidgets.QLabel(self)
        self.label5.setGeometry(QtCore.QRect(430, 390, 530, 400))
        self.label5.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.label5.setText('')

        self.lin1 = QtWidgets.QLineEdit(self)
        self.lin1.setGeometry(QtCore.QRect(70, 380, 60, 20))

        self.lin2 = QtWidgets.QLineEdit(self)
        self.lin2.setGeometry(QtCore.QRect(70, 420, 60, 20))

        self.lin3 = QtWidgets.QLineEdit(self)
        self.lin3.setGeometry(QtCore.QRect(70, 460, 60, 20))

        self.lin4 = QtWidgets.QLineEdit(self)
        self.lin4.setGeometry(QtCore.QRect(70, 500, 60, 20))
        
        self.label1.setWordWrap(True)
        self.label2.setWordWrap(True)
        self.label3.setWordWrap(True)
        self.label4.setWordWrap(True)

        self.textEdit_2 = QtWidgets.QTextEdit(self)
        self.textEdit_2.setGeometry(QtCore.QRect(430, 200, 350, 200))
        self.textEdit_2.setObjectName("textEdit_2")

    def pbut(self):
        but=self.sender()
        i=int(but.text())-1
        self.label1.setText('Линия: ' +str(kletki[named][nameg][namek][i][0]))
        self.label2.setText('Пассаж: '+str(kletki[named][nameg][namek][i][1]))
        self.label3.setText('Дата: '  +str(kletki[named][nameg][namek][i][2]))
        self.label4.setText('Имя: '   +str(kletki[named][nameg][namek][i][3]))

        ###--------------------board
        if self.select[named][nameg][namek][i]==1:
            self.select[named][nameg][namek][i]=0
            self.selected[named][nameg][namek].remove(i+1)
            self.label1.setText('')
            self.label2.setText('')
            self.label3.setText('')
            self.label4.setText('')
            
        else:
            self.select[named][nameg][namek][i]=1
            self.selected[named][nameg][namek].append(i+1)
            #------------
        self.lsel=''
        for i in range(2):
            for i1 in range(4):
                for i2 in range(10):
                    if len(self.selected[i][i1][i2])>0:
                        self.lsel+='Дюар '+str(i+1)+',Гнездо '+str(i1+1)+',Коробка '+str(i2+1)+': \n'
                    for i3 in range(81):
                        if self.selected[i][i1][i2].count(i3+1)>0:
                            self.lsel+=str(i3+1)+', '
                    if len(self.selected[i][i1][i2])>0:
                            self.lsel+='\n\n'                   
        self.textEdit_2.setText('Выделены ячейки: '+str(self.lsel))
        if len(self.selected[named][nameg][namek])==0:
            self.label1.setText('')
            self.label2.setText('')
            self.label3.setText('')
            self.label4.setText('')
            #self.label5.setText('')
        self.risov()
        #self.label1.setText(str(i))
        #self.but[i].setFont(QtGui.QFont("Times", 8))
        #time.sleep(1)
        #self.but[i].setFont(QtGui.QFont("Times", 14))
    def fdel(self):
        for i3 in range(2):
            for i2 in range(4):
                for i1 in range(10):                    
                    for i in self.selected[i3][i2][i1]:
                        kletki[i3][i2][i1][i-1][0]=''
                        kletki[i3][i2][i1][i-1][1]=''
                        kletki[i3][i2][i1][i-1][2]=''
                        kletki[i3][i2][i1][i-1][3]=''
        self.label1.setText('')
        self.label2.setText('')
        self.label3.setText('')
        self.label4.setText('')    
        self.risov()
        with open("base.json", "w", encoding="utf-8") as file:
            json.dump(kletki, file)
    def fred(self):
        for i3 in range(2):
            for i2 in range(4):
                for i1 in range(10):                    
                    for i in self.selected[i3][i2][i1]:
                        kletki[i3][i2][i1][i-1][0]=self.lin1.text()
                        kletki[i3][i2][i1][i-1][1]=self.lin2.text()
                        kletki[i3][i2][i1][i-1][2]=self.lin3.text()
                        kletki[i3][i2][i1][i-1][3]=self.lin4.text()

        self.label1.setText('Линия: ' +str(self.lin1.text()))
        self.label2.setText('Пассаж: '+str(self.lin2.text()))
        self.label3.setText('Дата: '  +str(self.lin3.text()))
        self.label4.setText('Имя: '   +str(self.lin4.text()))
            
        self.risov()
        with open("base.json", "w", encoding="utf-8") as file:
            json.dump(kletki, file)
    def fdcomb(self,text):
        global named
        named=int(text)-1
        self.risov()
    def fgcomb(self,text):
        global nameg
        nameg=int(text)-1
        self.risov()
    def fkcomb(self,text):
        global namek
        namek=int(text)-1
        self.risov()
    def risov(self):
        #print('risov')
        #print(str(self.selected))
        border=''        
        for i2 in range (1,82):
            if self.selected[named][nameg][namek].count(i2)>0:
                border='border:2px solid #000000'
            else:
                border='' 
            if kletki[named][nameg][namek][i2-1][0]=='':
                self.but[i2].setStyleSheet('background-color: #ffffff;'+border)
            elif kletki[named][nameg][namek][i2-1][0].count(namec)>0:
                self.but[i2].setStyleSheet('background-color: #00ff00;'+border)
            else:
                self.but[i2].setStyleSheet('background-color: #0fffff;'+border)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PassWindow()
    window.show()
    sys.exit(app.exec_())
