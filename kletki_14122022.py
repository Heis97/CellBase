import sys
import json
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QTableWidget, QComboBox, QTableWidgetItem)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt
a=5
ppls=['']
cellsline=['']
namep=""
namec=""
named=0
nameg=0
namek=0
selk=[]
kletki=[[[[]]]]
with open("base.json") as file:   
    res=json.load(file)
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
                kletki[i][i1][i2].append([res[i][i1][i2][i3][0],res[i][i1][i2][i3][1],res[i][i1][i2][i3][2],res[i][i1][i2][i3][3],res[i][i1][i2][i3][4],res[i][i1][i2][i3][5],res[i][i1][i2][i3][6]])
                if ppls.count(res[i][i1][i2][i3][3])==0 and res[i][i1][i2][i3][3]!='':
                    ppls.append(res[i][i1][i2][i3][3])
                if cellsline.count(res[i][i1][i2][i3][0])==0 and res[i][i1][i2][i3][0]!='':
                    cellsline.append(res[i][i1][i2][i3][0])
class PassWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setWindowTitle("Авторизация")
        self.resize(400, 300)
        self.Win2 = None
        self.build()
    def build(self):
        self.but1 = QtWidgets.QPushButton('Вход', self)
        self.but1.setGeometry(QtCore.QRect(130, 240, 120, 40))
        self.but1.clicked.connect(self.vhod)

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setGeometry(QtCore.QRect(10, 60, 200, 20))
        self.label1.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Medium))
        self.label1.setText('Выберете имя из списка:')
        

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setGeometry(QtCore.QRect(10, 120, 200, 20))
        self.label1.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Medium))
        self.label1.setText('либо впишите своё:')
        

        self.lin = QtWidgets.QLineEdit(self)
        self.lin.setGeometry(QtCore.QRect(170, 120, 160, 20))
        
        self.combo = QComboBox(self)
        self.combo.addItems(ppls)
        self.combo.move(200, 60)
        self.combo.activated[str].connect(self.fcombo)
        global namep
        namep=self.combo.currentText()
        #print(combo.currentText())
        #combo.setCurrentIndex(3)
    def vhod(self):  
        global namep  
        namep=self.lin.text()
        if not self.Win2:
            self.Win2 = MainWindow(self)
        self.Win2.show()
        #self.close()
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
        self.setWindowTitle("Клеточная база")
        self.resize(1000, 700)
        self.Win2 = None
        self.build()
    def build(self):
        self.but1 = QtWidgets.QPushButton('Найти', self)
        self.but1.setGeometry(QtCore.QRect(480, 80, 120, 30))
        self.but1.clicked.connect(self.ffind)
        
        self.but2 = QtWidgets.QPushButton('Карта', self)
        self.but2.setGeometry(QtCore.QRect(600, 80, 120, 30))
        self.but2.clicked.connect(self.fmap)

        self.label0 = QtWidgets.QLabel(self)
        self.label0.setGeometry(QtCore.QRect(100, 60, 200, 20))
        self.label0.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Medium))
        self.label0.setText('Поиск клеточной линии:')
        #self.label0.hasSelectedText(True)

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setGeometry(QtCore.QRect(830, 10, 150, 100))
        self.label1.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Medium))
        self.label1.setText('Вы вошли как:\n'+str(namep)+'\n\n'+'Текущая дата:\n'+str(datas))
        
        self.lin = QtWidgets.QLineEdit(self)
        self.lin.setGeometry(QtCore.QRect(100, 81, 380, 28))
        combo1 = QComboBox(self)
        combo1.addItems(cellsline)
        combo1.move(100, 28)
        combo1.activated[str].connect(self.fcombo)
        
        self.table = CustomTableWidget(self)
        self.table.setGeometry(QtCore.QRect(100, 120, 620, 400))
        self.table.setColumnCount(4)  
         
        self.table.setHorizontalHeaderLabels(["Пассаж", "Дата", "Человек","Расположение"])
 
        self.table.horizontalHeaderItem(0).setToolTip("Пассаж")
        self.table.horizontalHeaderItem(1).setToolTip("Дата")
        self.table.horizontalHeaderItem(2).setToolTip("Человек")
        self.table.horizontalHeaderItem(3).setToolTip("Расположение")
 
        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(3).setTextAlignment(Qt.AlignLeft)
        
        self.table.setRowCount(0) 
        self.table.resizeColumnsToContents()
        self.table.doubleClicked.connect(self.on_click)
        self.table.itemSelectionChanged.connect(self.activ)
        self.table.setSortingEnabled(True)
        #for cells1 in cellsline:
            #self.fcombo(cells1)
    def createItem(self, text, flags):
        tableWidgetItem = QTableWidgetItem(text)
        tableWidgetItem.setFlags(flags)
        return tableWidgetItem
    
    def ffind(self):
        if self.lin.text()!='':
            self.fcombo(self.lin.text())
    def fmap(self):
        if not self.Win2:
            self.Win2 = MapWindow(self)
        self.Win2.show()
    def fcombo(self,text):
        global namec
        namec=str(text)
        #find_cells = text.lower()
        self.table.setRowCount(0)
        k=0
        k1=0
        listk=[]
        listk1=[]
        listk2=[]
        listk3=[]
        listk4=[]
        k2 = 0
        for i in range(2):
            for i1 in range(4):
                for i2 in range(10):
                    k=0
                    listk=[]
                    for i3 in range(81):
                        if kletki[i][i1][i2][i3][0].count(namec)>0:
                        #cell_cur = kletki[i][i1][i2][i3][0].lower()
                        #if  cell_cur.count(find_cells)>0:
                            k+=1
                            k2+=1
                            listk.append([i,i1,i2,i3])
                    if k!=0:    
                        k1+=1
                        listk1.append(listk)
        #print(str(namec)+ " " + str(k2))                
        #sort data-----------------------------------------------------------
        #print(listk1)
        if listk1!=[]:
            left=0
            right=len(listk1)-1
            while left <= right:
                
                for i in range(left, right, +1):
                    datais = 0
                    datai1s = 0


                    datai=kletki[listk1[i][0][0]][listk1[i][0][1]][listk1[i][0][2]][listk1[i][0][3]][2]
                    if '.' in datai:
                        datai=datai.split('.')
                        if len(datai)>2:
                            datais=int(datai[0])+(int(datai[1])-1)*30+int(datai[2])*360


                    datai1=kletki[listk1[i+1][0][0]][listk1[i+1][0][1]][listk1[i+1][0][2]][listk1[i+1][0][3]][2]
                    if '.' in datai1:
                        datai1=datai1.split('.')
                        if len(datai1)>2:
                            datai1s=int(datai1[0])+(int(datai1[1])-1)*30+int(datai1[2])*360


                    if datais < datai1s:
                        listk1[i], listk1[i + 1] = listk1[i + 1], listk1[i]
                right -= 1

                for i in range(right, left, -1):
                    datais = 0
                    datai2s = 0



                    datai=kletki[listk1[i][0][0]][listk1[i][0][1]][listk1[i][0][2]][listk1[i][0][3]][2]
                    if '.' in datai:       
                        datai=datai.split('.')                 
                        if len(datai)>2:                         
                            datais=int(datai[0])+(int(datai[1])-1)*30+int(datai[2])*360


                    datai2=kletki[listk1[i-1][0][0]][listk1[i-1][0][1]][listk1[i-1][0][2]][listk1[i-1][0][3]][2]
                    if '.' in datai2:   
                        datai2=datai2.split('.')
                        if len(datai2)>2:
                            datai2s=int(datai2[0])+(int(datai2[1])-1)*30+int(datai2[2])*360



                    if datai2s < datais:
                        listk1[i], listk1[i - 1] = listk1[i - 1], listk1[i]
                left += 1
                #end--------------------------------------------------------
           
            self.table.setRowCount(k1)
            for i in range(len(listk1)):
                yach=""
                for i1 in range(len(listk1[i])):
                    selk.append(listk1[i][i1][3])
                    yach+=" "+str(listk1[i][i1][3]+1)+","
                self.table.setItem(i, 0, self.createItem(kletki[listk1[i][0][0]][listk1[i][0][1]][listk1[i][0][2]][listk1[i][0][3]][1], Qt.ItemIsSelectable | Qt.ItemIsEnabled ))
                self.table.setItem(i, 1, self.createItem(kletki[listk1[i][0][0]][listk1[i][0][1]][listk1[i][0][2]][listk1[i][0][3]][2], Qt.ItemIsSelectable | Qt.ItemIsEnabled ))
                self.table.setItem(i, 2, self.createItem(kletki[listk1[i][0][0]][listk1[i][0][1]][listk1[i][0][2]][listk1[i][0][3]][3], Qt.ItemIsSelectable | Qt.ItemIsEnabled ))
                self.table.setItem(i, 3, self.createItem('Дюар '+str(listk1[i][0][0]+1)+',Гнездо '+str(listk1[i][0][1]+1)+',Коробка '+str(listk1[i][0][2]+1)+',Ячейки: '+yach[:-1], Qt.ItemIsSelectable | Qt.ItemIsEnabled ))
                self.listk1=listk1
                self.listk1[i][0].append(selk)        
            self.table.resizeColumnsToContents()
    def on_click(self):
        for currentQTableWidgetItem in self.table.selectedItems():
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

class MapWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setWindowTitle("Карта")
        self.resize(1000, 600)
        self.Win2 = None
        self.build()
    def build(self):
        self.mod=''
        dcomb = QComboBox(self)
        dcomb.addItems(['1','2'])
        dcomb.move(60, 10)
        dcomb.setCurrentIndex(named)
        dcomb.activated[str].connect(self.fdcomb)
        gcomb = QComboBox(self)
        gcomb.addItems(['1','2','3','4'])
        gcomb.move(170, 10)
        gcomb.activated[str].connect(self.fgcomb)
        gcomb.setCurrentIndex(nameg)

        kcomb = QComboBox(self)
        kcomb.addItems(['1','2','3','4','5','6','7','8','9','10'])
        kcomb.move(300, 10)
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
        self.selected=[]
        for i in range (1,100):
            self.but+=[0]
            self.bsel+=[0]
        bsize=34
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
                self.but[i2].setAccessibleName(str(i)+','+str(i1)) 
                i2+=1
                #print('x= '+str(i-1))
                #print('y= '+str(i1))
                #print('n= '+str(i2-1))
                #print('---------------')
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
        self.but1.setGeometry(QtCore.QRect(830, 240+10, 120, 40))
        self.but1.clicked.connect(self.fred)
        
        self.but2 = QtWidgets.QPushButton('Удалить', self)
        self.but2.setGeometry(QtCore.QRect(830, 280+10, 120, 40))
        self.but2.clicked.connect(self.fdel)

        self.but3 = QtWidgets.QPushButton('Внести', self)
        self.but3.setGeometry(QtCore.QRect(830, 200+10, 120, 40))
        self.but3.clicked.connect(self.fvne)

        self.but4 = QtWidgets.QPushButton('Сохранить', self)
        self.but4.setGeometry(QtCore.QRect(830, 160+10, 120, 40))
        self.but4.clicked.connect(self.fsave)

        self.but5 = QtWidgets.QPushButton('Снять выделение', self)
        self.but5.setGeometry(QtCore.QRect(830, 320+10, 120, 40))
        self.but5.clicked.connect(self.fclr)

        self.but6 = QtWidgets.QPushButton('', self)
        self.but6.setGeometry(QtCore.QRect(489, 9, 22, 22))
        self.but6.clicked.connect(self.fsw1)

        self.but7 = QtWidgets.QPushButton('', self)
        self.but7.setGeometry(QtCore.QRect(489, 9, 22, 22))
        self.but7.clicked.connect(self.fsw2)

        self.comboc = QComboBox(self)
        self.comboc.addItems(cellsline)
        self.comboc.move(510, 10)
        self.comboc.activated[str].connect(self.fcomboc)
        self.comboc.setVisible(False)
        self.but6.setVisible(False)
        self.but7.setVisible(False)

        self.label0 = QtWidgets.QLabel(self)
        self.label0.setGeometry(QtCore.QRect(10, 8, 50, 20))
        self.label0.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Medium))
        self.label0.setText('Дюар:')

        self.label0 = QtWidgets.QLabel(self)
        self.label0.setGeometry(QtCore.QRect(110, 8, 60, 20))
        self.label0.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Medium))
        self.label0.setText('Гнездо:')

        self.label0 = QtWidgets.QLabel(self)
        self.label0.setGeometry(QtCore.QRect(225, 8, 70, 20))
        self.label0.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Medium))
        self.label0.setText('Коробка:')

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setGeometry(QtCore.QRect(430, 10, 530, 40))
        self.label1.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Medium))
        self.label1.setText('')#line

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setGeometry(QtCore.QRect(430, 50, 330, 40))
        self.label2.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Medium))
        self.label2.setText('')#passage
        
        self.label3 = QtWidgets.QLabel(self)
        self.label3.setGeometry(QtCore.QRect(430, 90, 330, 40))
        self.label3.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Medium))
        self.label3.setText('')#data

        self.label4 = QtWidgets.QLabel(self)
        self.label4.setGeometry(QtCore.QRect(430, 130, 330, 40))
        self.label4.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Medium))
        self.label4.setText('')#time

        self.label5 = QtWidgets.QLabel(self)
        self.label5.setGeometry(QtCore.QRect(430, 170, 330, 40))
        self.label5.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Medium))
        self.label5.setText('')#spher_f

        self.label6 = QtWidgets.QLabel(self)
        self.label6.setGeometry(QtCore.QRect(430, 210, 330, 40))
        self.label6.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Medium))
        self.label6.setText('')#source

        self.label7 = QtWidgets.QLabel(self)
        self.label7.setGeometry(QtCore.QRect(430, 250, 400, 500))
        self.label7.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Medium))
        self.label7.setText('')#env


        self.lin1 = QtWidgets.QLineEdit(self)
        self.lin1.setGeometry(QtCore.QRect(510, 10, 260, 20))

        self.lin2 = QtWidgets.QLineEdit(self)
        self.lin2.setGeometry(QtCore.QRect(510, 50, 60, 20))

        self.lin3 = QtWidgets.QLineEdit(self)
        self.lin3.setGeometry(QtCore.QRect(510, 90, 160, 20))

        self.lin4 = QtWidgets.QLineEdit(self)
        self.lin4.setGeometry(QtCore.QRect(510, 130, 160, 20))

        self.lin5 = QtWidgets.QLineEdit(self)
        self.lin5.setGeometry(QtCore.QRect(610, 170, 60, 20))

        self.lin6 = QtWidgets.QLineEdit(self)
        self.lin6.setGeometry(QtCore.QRect(510, 210, 160, 20))

        self.lin7 = QtWidgets.QTextEdit(self)
        self.lin7.setGeometry(QtCore.QRect(430, 290, 400, 300))


        
        self.label1.setWordWrap(True)
        self.label2.setWordWrap(True)
        self.label3.setWordWrap(True)
        self.label4.setWordWrap(True)
        self.label5.setWordWrap(True)
        self.label6.setWordWrap(True)
        self.label7.setWordWrap(True)
        self.label1.setAlignment(Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignLeft)
        self.label2.setAlignment(Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignLeft)
        self.label3.setAlignment(Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignLeft)
        self.label4.setAlignment(Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignLeft)
        self.label5.setAlignment(Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignLeft)
        self.label6.setAlignment(Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignLeft)
        self.label7.setAlignment(Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignLeft)
        self.lin1.setVisible(False)
        self.lin2.setVisible(False)
        self.lin3.setVisible(False)
        self.lin4.setVisible(False)
        self.lin5.setVisible(False)
        self.lin6.setVisible(False)
        self.lin7.setVisible(False)

        self.textEdit_2 = QtWidgets.QTextEdit(self)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 390, 350, 170))
        self.prelastkl=''
    def fclr(self):
        self.bsel=[]
        self.select=[]
        for i in range(2):
            self.select.append([])
            for i1 in range(4):
                self.select[i].append([])
                for i2 in range(10):
                    self.select[i][i1].append([])
                    for i3 in range(81):
                        self.select[i][i1][i2].append(0)
        self.selected=[]
        for i in range (1,100):
            self.bsel+=[0]
        for i in range(2):                
            self.selected.append([[[],[],[],[],[],[],[],[],[],[]],
                                  [[],[],[],[],[],[],[],[],[],[]],
                                  [[],[],[],[],[],[],[],[],[],[]],
                                  [[],[],[],[],[],[],[],[],[],[]]])
        self.textEdit_2.setText('Выделены ячейки: ')
        if len(self.selected[named][nameg][namek])==0:
            self.label1.setText('')
            self.label2.setText('')
            self.label3.setText('')
            self.label4.setText('')
            self.label5.setText('')
            self.label6.setText('')
            self.label7.setText('')
            self.lin1.setVisible(False)
            self.lin2.setVisible(False)
            self.lin3.setVisible(False)
            self.lin4.setVisible(False)
            self.lin5.setVisible(False)
            self.lin6.setVisible(False)
            self.lin7.setVisible(False)
            self.comboc.setVisible(False)
            self.but6.setVisible(False)
            self.but7.setVisible(False)
        
        self.risov()
    def keyPressEvent(self, e):
        if e.key()==Qt.Key_Shift:
            self.mod='shift'
        if e.key()==Qt.Key_Control:
            self.mod='control'
    def keyReleaseEvent(self, e):
        if e.key()==Qt.Key_Shift:
            self.mod=''
        if e.key()==Qt.Key_Control:
            self.mod=''
    def pbut(self):
        but=self.sender()
        i=int(but.text())-1
        if self.prelastkl=='':
            self.prelastkl=i
        else:                
            self.prelastkl=self.lastkl
        self.lastkl=i
               

        ###--------------------board
        if self.mod=='control':
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
        elif self.mod=='shift':
            koord1=self.but[self.prelastkl+1].accessibleName().split(',')
            x1=int(koord1[0])
            y1=int(koord1[1])
            koord=but.accessibleName().split(',')
            x2=int(koord[0])
            y2=int(koord[1])
            
            if x1<x2:
                s1=x1
                e1=x2+1
            else:
                s1=x2
                e1=x1+1
                
            if y1<y2:
                s2=y1
                e2=y2+1
            else:
                s2=y2
                e2=y1+1
                
            for i_h in range(s1,e1):
                for i_w in range(s2,e2):
                    self.select[named][nameg][namek][(i_h-1)*9+i_w-1]=1
                    self.selected[named][nameg][namek].append((i_h-1)*9+i_w)
        else:
            for i4 in range(2):
                for i1 in range(4):
                    for i2 in range(10):
                        self.selected[i4][i1][i2]=[]
                        for i3 in range(81):                            
                            self.select[i4][i1][i2][i3]=0
            self.select[named][nameg][namek][i]=1
            self.selected[named][nameg][namek].append(i+1)

            #------------
            
        self.lsel=''
        self.label1.setText('Линия:  ' +str(kletki[named][nameg][namek][i][0]))
        self.label2.setText('Пассаж: '+str(kletki[named][nameg][namek][i][1]))
        self.label3.setText('Дата: '  +str(kletki[named][nameg][namek][i][2]))
        self.label4.setText('Имя: '   +str(kletki[named][nameg][namek][i][3]))
        self.label5.setText('Формируют сфероиды: '   +str(kletki[named][nameg][namek][i][4]))
        self.label6.setText('Источник: '   +str(kletki[named][nameg][namek][i][5]))
        self.label7.setText('Условия культивации: '   +str(kletki[named][nameg][namek][i][6]))
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
        if len(self.selected[named][nameg][namek])==0 or self.but6.isVisible() or self.but7.isVisible():
            self.label1.setText('')
            self.label2.setText('')
            self.label3.setText('')
            self.label4.setText('')
            self.label5.setText('')
            self.label6.setText('')
            self.label7.setText('')
            self.label1.setGeometry(QtCore.QRect(430, 10, 530, 40))
            self.label2.setGeometry(QtCore.QRect(430, 50, 330, 40))
            self.label3.setGeometry(QtCore.QRect(430, 90, 330, 40))
            self.label4.setGeometry(QtCore.QRect(430, 130, 330, 40))
            self.lin1.setVisible(False)
            self.lin2.setVisible(False)
            self.lin3.setVisible(False)
            self.lin4.setVisible(False)
            self.lin5.setVisible(False)
            self.lin6.setVisible(False)
            self.lin7.setVisible(False)
            self.comboc.setVisible(False)
            self.but6.setVisible(False)
            self.but7.setVisible(False)
        self.risov()
    def fdel(self):
        i10=0
        for i3 in range(2):
            for i2 in range(4):
                for i1 in range(10):                    
                    for i in self.selected[i3][i2][i1]:
                        i10+=1
                        kletki[i3][i2][i1][i-1][0]=''
                        kletki[i3][i2][i1][i-1][1]=''
                        kletki[i3][i2][i1][i-1][2]=''
                        kletki[i3][i2][i1][i-1][3]=''
                        kletki[i3][i2][i1][i-1][4]=''
                        kletki[i3][i2][i1][i-1][5]=''
                        kletki[i3][i2][i1][i-1][6]=''
        if i10>0:
            self.label1.setText('')
            self.label2.setText('')
            self.label3.setText('')
            self.label4.setText('')
            self.label5.setText('')
            self.label6.setText('')
            self.label7.setText('')
            self.lin1.setVisible(False)
            self.lin2.setVisible(False)
            self.lin3.setVisible(False)
            self.lin4.setVisible(False)
            self.lin5.setVisible(False)
            self.lin6.setVisible(False)
            self.lin7.setVisible(False)
            self.comboc.setVisible(False)
            self.but6.setVisible(False)
            self.but7.setVisible(False)
            self.risov()
            with open("base.json", "w", encoding="utf-8") as file:
                json.dump(kletki, file)
    def fred(self):
        i10=0
        for i3 in range(2):
            for i2 in range(4):
                for i1 in range(10):                    
                    for i in self.selected[i3][i2][i1]:
                        i10+=1
                        lin=kletki[i3][i2][i1][i-1][0]
                        pas=kletki[i3][i2][i1][i-1][1]
                        dat=kletki[i3][i2][i1][i-1][2]
                        nam=kletki[i3][i2][i1][i-1][3]
                        sph=kletki[i3][i2][i1][i-1][4]
                        src=kletki[i3][i2][i1][i-1][5]
                        env=kletki[i3][i2][i1][i-1][6]
        if i10>0:
            self.cline=lin
            for i in range (len(cellsline)):
                #print(kletki[named][nameg][namek][self.lastkl][0])
                if kletki[named][nameg][namek][self.lastkl][0].count(cellsline[i])>0:
                    self.comboc.setCurrentIndex(i)
            self.label1.setText('Линия:  ')
            self.label2.setText('Пассаж: ')
            self.label3.setText('Дата:  ')
            self.label4.setText('Имя: ')
            self.label5.setText('Формируют сфероиды: ')
            self.label6.setText('Источник: ')
            self.label7.setText('Условия культивации: ')
            self.label1.setGeometry(QtCore.QRect(430, 10, 50, 40))
            self.label2.setGeometry(QtCore.QRect(430, 50, 80, 40))
            self.label3.setGeometry(QtCore.QRect(430, 90, 80, 40))
            self.label4.setGeometry(QtCore.QRect(430, 130, 80, 40))
            self.comboc.setVisible(True)
            self.but6.setVisible(True)
            self.but7.setVisible(False)
            self.lin1.setVisible(False)
            self.lin2.setVisible(True)
            self.lin3.setVisible(True)
            self.lin4.setVisible(True)
            self.lin5.setVisible(True)
            self.lin6.setVisible(True)
            self.lin7.setVisible(True)
            self.lin1.setText('')
            self.lin2.setText(pas)
            self.lin3.setText(dat)
            self.lin4.setText(nam) 
            self.lin5.setText(sph) 
            self.lin6.setText(src) 
            self.lin7.setText(env) 

            self.risov()
    def fsw1(self):
        self.but6.setVisible(False)
        self.but7.setVisible(True)
        self.lin1.setVisible(True)
        
        self.comboc.setVisible(False)
        self.lin1.setText(self.cline)
        
    def fsw2(self):
        self.but6.setVisible(True)
        self.but7.setVisible(False)
        self.lin1.setVisible(False)
        
        
        self.comboc.setVisible(True)
        for i in range (len(cellsline)):
            if self.lin1.text().count(cellsline[i])>0:
                self.comboc.setCurrentIndex(i)
        self.cline=self.comboc.currentText()
        self.lin1.setText('')
    def fcomboc(self,text):
        self.cline=text
    def fsave(self):
        global kletki
        self.cline=self.comboc.currentText()
        i10=0
        if self.lin1.isVisible()==True or self.comboc.isVisible()==True:
            for i3 in range(2):
                for i2 in range(4):
                    for i1 in range(10):                    
                        for i in self.selected[i3][i2][i1]:
                            i10+=1
                            if self.lin1.isVisible()==True:
                                kletki[i3][i2][i1][i-1][0]=self.lin1.text()
                            else:
                                kletki[i3][i2][i1][i-1][0]=self.cline
                            lin=kletki[i3][i2][i1][i-1][0]

                            kletki[i3][i2][i1][i-1][1]=self.lin2.text()
                                                       
                            if self.lin3.text()!='':
                                kletki[i3][i2][i1][i-1][2]=self.lin3.text()
                            else:
                                kletki[i3][i2][i1][i-1][2]=datas
                            dat=kletki[i3][i2][i1][i-1][2]
                            
                            if self.lin4.text()!='':
                                kletki[i3][i2][i1][i-1][3]=self.lin4.text()
                            else:
                                kletki[i3][i2][i1][i-1][3]=namep
                            nam=kletki[i3][i2][i1][i-1][3]

                            kletki[i3][i2][i1][i-1][4]=self.lin5.text()
                            kletki[i3][i2][i1][i-1][5]=self.lin6.text()
                            kletki[i3][i2][i1][i-1][6]=self.lin7.toPlainText()

        if i10>0:
            self.label1.setText('Линия:  ' +str(lin))
            self.label1.setGeometry(QtCore.QRect(430, 10, 530, 40))
            self.label2.setText('Пассаж: '+str(self.lin2.text()))
            self.label2.setGeometry(QtCore.QRect(430, 50, 330, 40))
            self.label3.setText('Дата: '  +str(dat))
            self.label3.setGeometry(QtCore.QRect(430, 90, 330, 40))
            self.label4.setText('Имя: '   +str(nam))
            self.label4.setGeometry(QtCore.QRect(430, 130, 330, 40))
            self.label5.setText('Формируют сфероиды: '+str(self.lin5.text()))
            self.label6.setText('Источник: '+str(self.lin6.text()))
            self.label7.setText('Условия культивации: '+str(self.lin7.toPlainText()))
            self.comboc.setVisible(False)
            self.but6.setVisible(False)
            self.but7.setVisible(False)
            self.lin1.setVisible(False)
            self.lin2.setVisible(False)
            self.lin3.setVisible(False)
            self.lin4.setVisible(False)
            self.lin5.setVisible(False)
            self.lin6.setVisible(False)
            self.lin7.setVisible(False)
            self.lin1.setText('')
            self.lin2.setText('')
            self.lin3.setText('')
            self.lin4.setText('')
            self.lin5.setText('')
            self.lin6.setText('')
            self.lin7.setText('')
            self.risov()
            len_cel=len(cellsline)
            with open("base.json", "w", encoding="utf-8") as file:
                json.dump(kletki, file)
                
            kletki=[[[[]]]]
            with open("base.json") as file:   
                res=json.load(file)

            for i in range(2):
                kletki.append([])
                for i1 in range(4):
                    kletki[i].append([])
                    for i2 in range(10):
                        kletki[i][i1].append([])
                        for i3 in range(81):
                            kletki[i][i1][i2].append([res[i][i1][i2][i3][0],res[i][i1][i2][i3][1],res[i][i1][i2][i3][2],res[i][i1][i2][i3][3],res[i][i1][i2][i3][4],res[i][i1][i2][i3][5],res[i][i1][i2][i3][6]])
                            if ppls.count(res[i][i1][i2][i3][3])==0 and res[i][i1][i2][i3][3]!='':
                                ppls.append(res[i][i1][i2][i3][3])
                            if cellsline.count(res[i][i1][i2][i3][0])==0 and res[i][i1][i2][i3][0]!='':
                                cellsline.append(res[i][i1][i2][i3][0])
            for i in range(len_cel):
                self.comboc.removeItem(0)
            self.comboc.addItems(cellsline)
            self.comboc.update()
    def fvne(self):
        i10=0
        for i3 in range(2):
            for i2 in range(4):
                for i1 in range(10):                    
                    for i in self.selected[i3][i2][i1]:
                        i10+=1
                        lin=kletki[i3][i2][i1][i-1][0]
                        pas=kletki[i3][i2][i1][i-1][1]
                        sph=kletki[i3][i2][i1][i-1][4]
                        src=kletki[i3][i2][i1][i-1][5]
                        env=kletki[i3][i2][i1][i-1][6]
        if i10>0:
            self.label1.setText('Линия:  ')
            self.label2.setText('Пассаж: ')
            self.label1.setGeometry(QtCore.QRect(430, 10, 55, 40))
            self.label2.setGeometry(QtCore.QRect(430, 50, 80, 40))
            self.cline=lin
            for i in range (len(cellsline)):
                if kletki[named][nameg][namek][self.lastkl][0].count(cellsline[i])>0:
                    self.comboc.setCurrentIndex(i)
            self.cline=self.comboc.currentText()
            self.comboc.setVisible(True)
            self.but6.setVisible(True)
            self.but7.setVisible(False)
            self.lin1.setVisible(False)
            self.lin2.setVisible(True)
            self.lin3.setVisible(False)
            self.lin4.setVisible(False)

            self.lin5.setVisible(True)
            self.lin6.setVisible(True)
            self.lin7.setVisible(True)

            self.lin3.setText('')
            self.lin4.setText('')
            self.lin1.setText('')
            self.lin2.setText(pas)  
            self.lin5.setText(sph)                         
            self.lin6.setText(src)
            self.lin7.setText(env)

            self.label3.setText('Дата: '  +str(datas))
            self.label3.setGeometry(QtCore.QRect(430, 90, 330, 40))
            self.label4.setText('Имя: '   +str(namep))
            self.label4.setGeometry(QtCore.QRect(430, 130, 330, 40))
            self.label5.setText('Формируют сфероиды: '+str(sph))
            self.label6.setText('Источник: '+str(src))
            self.label7.setText('Условия культивации: '+str(env))
            self.risov()
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
