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