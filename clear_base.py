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
base_misis = [2,4,10,81]
dimensions = base_misis

for i3 in range(dimensions[0]):
    c=[]
    for i2 in range(dimensions[1]):
        b=[]
        for i1 in range(dimensions[2]):
            a=[]
            for i in range(dimensions[3]):
                a.append(['','','',''])           
            b.append(a)
        c.append(b)
    d.append(c)

file='base.json'
kletki=d
with open("base.json", "w", encoding="utf-8") as file:
    json.dump(kletki, file)