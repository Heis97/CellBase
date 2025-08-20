
import json
from datetime import datetime
ppls=['']
cellsline=['']
namep=""
namec=""
named=0
nameg=0
namek=0
selk=[]
kletki=[[[[]]]]
kletki_cur=[[[[]]]]

file_cur = "base_cur.json"
file_old = "base_180725.json"

with open(file_old) as file:   
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


with open(file_cur) as file:   
    res=json.load(file)

for i in range(2):
    kletki_cur.append([])
    for i1 in range(4):
        kletki_cur[i].append([])
        for i2 in range(10):
            kletki_cur[i][i1].append([])
            for i3 in range(81):
                kletki_cur[i][i1][i2].append([res[i][i1][i2][i3][0],res[i][i1][i2][i3][1],res[i][i1][i2][i3][2],res[i][i1][i2][i3][3]])



for i in range(2):
    kletki_cur.append([])
    for i1 in range(4):
        kletki_cur[i].append([])
        for i2 in range(10):
            kletki_cur[i][i1].append([])
            for i3 in range(81):
                for i4 in range(4):
                    kletki[i][i1][i2][i3][i4] = kletki_cur[i][i1][i2][i3][i4]


with open("base_rep.json", "w", encoding="utf-8") as file:
    json.dump(kletki, file)





